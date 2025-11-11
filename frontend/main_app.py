import streamlit as st

st.set_page_config(page_title='SystemX Simulator', layout='wide')

st.sidebar.title('SystemX Modules')
choice = st.sidebar.radio('Select a Module', 
    ['OS Scheduler', 'Network Routing', 'Cloud Load Balancer', 'Cache Simulator', 'Algorithm Profiler'])

if choice == 'OS Scheduler':
    st.title('🧠 OS Scheduler Simulator')
    st.write('Simulate CPU scheduling algorithms like FCFS, Round Robin, and Priority Scheduling.')
elif choice == 'Network Routing':
    st.title('🌐 Network Routing Simulator')
    st.write('Visualize shortest paths using algorithms like Dijkstra or Bellman-Ford.')
elif choice == 'Cloud Load Balancer':
    st.title('☁️ Cloud Load Balancer Simulator')
    st.write('Simulate load balancing strategies such as Round Robin and Least Connections.')
elif choice == 'Cache Simulator':
    st.title('💾 Cache Management Simulator')
    st.write('Understand caching algorithms like LRU, LFU, and FIFO.')
else:
    st.title('⚙️ Algorithm Profiler')
    st.write('Visualize sorting, searching, and runtime comparisons.')