
import streamlit as st
from pandas import DataFrame
import plotly.graph_objects as go
import numpy as np

def cria_dataframe(trigger, minr, maxr):
    cpu = range(1, 101)
    memory = range(1, 101)
    tx_scale_pods = (maxr / (100 - trigger))
    
    pods = np.full(101, minr).tolist()

    for i in range(len(pods)):
        if (i > trigger):
            pods[i] = pods[i - 1] + tx_scale_pods

    df = DataFrame(data = [cpu, memory, pods]).transpose()

    return df


st.title('análise de recursos')

col1, col2, col3, col4 = st.columns(4)

with col1:

    min_replicas = st.number_input('minReplicas', min_value=1, value=1)

with col2:

    max_replicas = st.number_input('maxReplicas', min_value=2, value=5)

with col3:

    cpu_limit = st.number_input('cpuLimit', min_value=100, value=100, step = 50)

with col4:

    memory_limit = st.number_input('memoryLimit', min_value=100, value=100, step = 50)

col4_1, col4_2, col4_3, col4_4 = st.columns(4)

with col4_1:
    cpu_usage = st.number_input('cpuUsage', min_value=100, value=100, step = 50)

with col4_2:
    cpu_trigger = st.number_input('cpuTrigger', min_value=50, max_value=100, value=50, step=1)

with col4_3:
    memory_usage = st.number_input('memoryUsage', min_value=100, value=100, step = 50)

with col4_4:
    memory_trigger = st.number_input('memoryTrigger', min_value=50, max_value=100, value=50, step=1)

col5_1, col5_2 = st.columns(2)

with col5_1:

    df1 = cria_dataframe(memory_trigger, min_replicas, max_replicas)
    bola1 = int(round((cpu_usage / cpu_limit) * 100, 0))
    z1 = int(df1[(df1[1] == bola1)][2])

    fig1 = go.Figure(data=[go.Scatter3d(z=df1[2].values, x=df1[0].values, y=df1[1].values, mode='lines')])

    fig1.add_trace(go.Scatter3d(
        x=[bola1],
        y=[bola1],
        z=[z1],
        mode='markers',
        marker=dict(
            size=10,
            color='blue'
        ),
        name='Você está aqui'
    ))

    fig1.update_layout(title='CPU',
                  scene=dict(
                      xaxis_title='Memória',
                      yaxis_title='CPU',
                      zaxis_title='Pods'))


    st.plotly_chart(fig1, use_container_width=True)

with col5_2:

    df2 = cria_dataframe(cpu_trigger, min_replicas, max_replicas)
    bola2 = int(round((memory_usage / memory_limit) * 100, 0))
    z2 = int(df2[(df2[0] == bola2)][2])

    fig2 = go.Figure(data=[go.Scatter3d(z=df2[2].values, x=df2[0].values, y=df2[1].values, mode='lines')])

    fig2.add_trace(go.Scatter3d(
        x=[bola2],
        y=[bola2],
        z=[z2],
        mode='markers',
        marker=dict(
            size=10,
            color='red'
        ),
        name='Você está aqui'
    ))

    fig2.update_layout(title='Memória',
                  scene=dict(
                      xaxis_title='Memória',
                      yaxis_title='CPU',
                      zaxis_title='Pods'))

    st.plotly_chart(fig2, use_container_width=True)
