import streamlit as st
from tabs import os_tab, network_tab, cloud_tab, cache_tab, algo_tab

st.set_page_config(page_title='SystemX Simulator', layout='wide')
st.title('SystemX — Unified Core CS Simulator')

st.sidebar.title('Modules')
module = st.sidebar.radio('Choose module', ['OS Scheduler', 'Network Routing', 'Cloud Load Balancer', 'Cache Simulator', 'Algorithm Profiler'])

if module == 'OS Scheduler':
    os_tab.show()
elif module == 'Network Routing':
    network_tab.show()
elif module == 'Cloud Load Balancer':
    cloud_tab.show()
elif module == 'Cache Simulator':
    cache_tab.show()
else:
    algo_tab.show()
