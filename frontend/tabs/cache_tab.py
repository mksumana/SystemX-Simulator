import streamlit as st
import requests

API_URL = 'http://localhost:8080/api/cache/run'  # Java backend placeholder

def show():
    st.header('💾 Cache Management Simulator')
    policy = st.selectbox('Eviction Policy', ['LRU', 'LFU', 'FIFO'])
    capacity = st.number_input('Cache capacity', min_value=1, value=3)
    stream = st.text_area('Request stream (comma-separated)', value='1,2,3,2,4,1,5')

    if st.button('Run Cache Simulation'):
        data_stream = [s.strip() for s in stream.split(',') if s.strip()]
        payload = {'policy': policy, 'capacity': int(capacity), 'stream': data_stream}
        st.info('Calling cache API...')
        try:
            res = requests.post(API_URL, json=payload, timeout=10)
            if res.ok:
                st.success('Simulation returned')
                st.json(res.json())
            else:
                st.error(f'Backend error: {res.status_code}')
        except Exception as e:
            st.error(f'Failed to call cache API at {API_URL}. Error: {e}')
