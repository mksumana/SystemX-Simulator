import streamlit as st
import time
import random

def show():
    st.header('⚙️ Algorithm Profiler')
    n = st.number_input('Array size (n)', min_value=1, max_value=20000, value=1000)
    algo = st.selectbox('Algorithm', ['bubble', 'merge', 'quick', 'heap'])
    if st.button('Run'):
        arr = list(range(n))
        random.shuffle(arr)
        start = time.time()
        if algo == 'bubble':
            bubble_sort(arr)
        elif algo == 'merge':
            arr = merge_sort(arr)
        elif algo == 'quick':
            arr = quick_sort(arr)
        else:
            import heapq
            heapq.heapify(arr); arr = [heapq.heappop(arr) for _ in range(len(arr))]
        elapsed = time.time() - start
        st.write(f'**{algo}** finished in **{elapsed:.4f} s**')

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def merge(l, r):
    i=j=0
    out=[]
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            out.append(l[i]); i+=1
        else:
            out.append(r[j]); j+=1
    out.extend(l[i:]); out.extend(r[j:])
    return out

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
