import streamlit as st
import requests

API_URL = 'http://localhost:8000/simulate'  # Python backend placeholder

def show():
    st.header('🌐 Network Routing Simulator')
    st.write('Provide edges as: src,dst,weight (one per line). Nodes can be strings or ints.')

    default = 'A,B,4\nA,C,2\nC,B,1\nB,D,5\nC,D,8'
    edges_text = st.text_area('Edges', value=default, height=180)
    source = st.text_input('Source', value='A')
    dest = st.text_input('Destination', value='D')
    algo = st.selectbox('Algorithm', ['dijkstra'])  # extend later

    if st.button('Find Shortest Path'):
        edges = []
        for line in edges_text.splitlines():
            line = line.strip()
            if not line:
                continue
            s,d,w = [p.strip() for p in line.split(',')]
            try:
                w = float(w)
            except:
                w = 1.0
            edges.append((s,d,w))

        payload = {'edges': edges, 'source': source, 'destination': dest, 'algorithm': algo}
        st.info('Calling network API...')
        try:
            res = requests.post(API_URL, json=payload, timeout=10)
            if res.ok:
                st.success('Path found')
                st.json(res.json())
            else:
                st.error(f'Backend error: {res.status_code}')
        except Exception as e:
            st.error(f'Failed to call network API at {API_URL}. Error: {e}')
