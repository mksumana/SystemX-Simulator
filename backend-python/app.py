from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Tuple, Any, Dict
import networkx as nx
import random
import time
import math

app = FastAPI(title='SystemX Python Simulators')

# ---------------------------
# Pydantic models (request)
# ---------------------------
class EdgeItem(BaseModel):
    src: str
    dst: str
    weight: float

class NetworkRequest(BaseModel):
    edges: List[Tuple[Any, Any, float]]  # list of [src, dst, weight]
    source: str
    destination: str
    algorithm: str = 'dijkstra'

class CloudRequest(BaseModel):
    servers: int
    rps: int  # requests per second
    strategy: str  # 'round_robin', 'least_connections', 'weighted'


# ---------------------------
# Network simulation endpoint
# ---------------------------
@app.post('/simulate')
def simulate_network(req: NetworkRequest):
    # Build graph
    try:
        G = nx.DiGraph()
        for e in req.edges:
            # edges maybe list or tuple like ['A','B',4]
            if isinstance(e, (list, tuple)) and len(e) >= 3:
                src, dst, w = e[0], e[1], float(e[2])
                G.add_edge(src, dst, weight=w)
            else:
                raise ValueError('Edge format invalid')
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f'Invalid edges: {ex}')

    if req.source not in G or req.destination not in G:
        raise HTTPException(status_code=400, detail='Source or destination node not in graph')

    if req.algorithm.lower() == 'dijkstra':
        try:
            path = nx.shortest_path(G, source=req.source, target=req.destination, weight='weight')
            cost = nx.shortest_path_length(G, source=req.source, target=req.destination, weight='weight')
            return {'shortest_path': path, 'cost': float(cost)}
        except nx.NetworkXNoPath:
            return {'shortest_path': [], 'cost': math.inf, 'message': 'No path found'}
    else:
        raise HTTPException(status_code=400, detail='Unsupported algorithm')

# ---------------------------
# Cloud load balancer simulation
# ---------------------------
@app.post('/cloud/simulate')
def simulate_cloud(req: CloudRequest):
    servers = max(1, int(req.servers))
    rps = max(1, int(req.rps))
    strategy = req.strategy

    # simple server state: each server has current connections (random start)
    server_states = [{'id': i, 'connections': random.randint(0, 3), 'load': random.uniform(0, 0.3)} for i in range(servers)]

    # Weighted example: assign weights proportional to server capacity (simulate)
    weights = [1 + random.random() for _ in range(servers)]
    total_assigned = [0]*servers

    assignments = []
    # simulate rps requests arriving in one second
    rr_index = 0
    for req_i in range(rps):
        if strategy == 'round_robin':
            target = rr_index % servers
            rr_index += 1
        elif strategy == 'least_connections':
            target = min(range(servers), key=lambda i: server_states[i]['connections'])
        elif strategy == 'weighted':
            # weighted random choice
            s = sum(weights)
            pick = random.random() * s
            acc = 0
            target = 0
            for i,w in enumerate(weights):
                acc += w
                if pick <= acc:
                    target = i
                    break
        else:
            # default round robin
            target = rr_index % servers
            rr_index += 1

        # update simulated server state
        server_states[target]['connections'] += 1
        server_states[target]['load'] += random.uniform(0.01, 0.05)
        total_assigned[target] += 1
        assignments.append({'request': req_i, 'server': target})

    # metrics
    avg_load = sum(s['load'] for s in server_states)/servers
    max_load = max(s['load'] for s in server_states)
    distribution = [{'server': s['id'], 'assigned_requests': total_assigned[s['id']], 'connections': s['connections'], 'load': round(s['load'],4)} for s in server_states]

    return {
        'strategy': strategy,
        'servers': servers,
        'requests_simulated': rps,
        'avg_load': round(avg_load,4),
        'max_load': round(max_load,4),
        'distribution': distribution
    }

# Health
@app.get('/health')
def health():
    return {'status': 'ok'}
