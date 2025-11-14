import streamlit as st
import requests
import json

API_URL = 'http://localhost:8080/api/os/schedule'  # Java backend placeholder

def show():
    st.header('🧠 OS Scheduler Simulator')
    st.write('Input processes (one per line) as: pid,arrival,burst,priority')

    default = '1,0,5,1\n2,1,3,2\n3,2,8,1'
    text = st.text_area('Processes', value=default, height=180)
    algo = st.selectbox('Algorithm', ['FCFS','SJF','RoundRobin','Priority'])
    quantum = None
    if algo == 'RoundRobin':
        quantum = st.number_input('Quantum', min_value=1, value=2, step=1)

    if st.button('Run Simulation'):
        # parse processes
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        processes = []
        for ln in lines:
            parts = [p.strip() for p in ln.split(',')]
            if len(parts) < 3:
                st.error('Each line needs at least pid,arrival,burst')
                return
            pid = int(parts[0]); arrival = int(parts[1]); burst = int(parts[2])
            priority = int(parts[3]) if len(parts) > 3 else 0
            processes.append({'pid': pid, 'arrival': arrival, 'burst': burst, 'priority': priority})

        payload = {'algorithm': algo, 'processes': processes}
        if quantum:
            payload['quantum'] = int(quantum)

        st.info('Sending request to backend...')
        try:
            res = requests.post(API_URL, json=payload, timeout=10)
            if res.ok:
                data = res.json()
                st.success('Simulation returned.')
                st.json(data)
                # Example: show Gantt or metrics if backend returns them
                if 'metrics' in data:
                    st.write('**Metrics**')
                    st.json(data['metrics'])
            else:
                st.error(f'Backend error: {res.status_code} {res.text}')
        except Exception as e:
            st.error(f'Failed to call backend. Make sure Java backend is running at {API_URL}. Error: {e}')
