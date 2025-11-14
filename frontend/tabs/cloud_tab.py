import streamlit as st
import requests

API_URL = 'http://localhost:8000/cloud/simulate'  # placeholder

def show():
    st.header('☁️ Cloud Load Balancer Simulator')
    servers = st.number_input('Number of servers', min_value=1, max_value=20, value=3)
    requests_per_sec = st.number_input('Incoming requests per second', min_value=1, value=10)
    strategy = st.selectbox('Load balancing strategy', ['round_robin', 'least_connections', 'weighted'])

    if st.button('Simulate Load Balancing'):
        payload = {'servers': int(servers), 'rps': int(requests_per_sec), 'strategy': strategy}
        st.info('Calling cloud simulator...')
        try:
            res = requests.post(API_URL, json=payload, timeout=10)
            if res.ok:
                st.success('Simulation returned')
                st.json(res.json())
            else:
                st.error(f'Backend error: {res.status_code}')
        except Exception as e:
            st.error(f'Failed to call cloud API at {API_URL}. Error: {e}')
