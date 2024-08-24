
import streamlit as st
from feedback_api import endpoint_get_fechado, endpoint_post_fechado

st.write(st.session_state)

try:

    perfil = endpoint_get_fechado(
        url = '/perfil/consulta/' + st.session_state.usuario_logado,
        token = st.session_state.token
    )

    carteira = endpoint_get_fechado(
        url = '/carteira/consulta/' + st.session_state.usuario_logado,
        token = st.session_state.token
    )

    feedbacks_recebidos = endpoint_get_fechado(
        url = '/feedback/comentarios-destino/' + st.session_state.usuario_logado,
        token = st.session_state.token
    )

    feedbacks_enviados = endpoint_get_fechado(
        url = '/feedback/comentarios-remetente/' + st.session_state.usuario_logado,
        token = st.session_state.token
    )

    st.write('### Olá ' + perfil.get('nome'))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Saldo Carteira', value = carteira.get('saldoCarteira'))

    with col2:
        st.metric('Pontos Recebidos', value = carteira.get('pontosCarteira'))

    with col3:
        st.metric('Feedbacks Recebidos', value = len(feedbacks_recebidos))

    st.write('Feedbacks Recebidos')
    st.dataframe(feedbacks_recebidos)

    st.write('Feedbacks Enviados')
    st.dataframe(feedbacks_enviados)

except Exception as e:

    st.title('### Olá, você não possui um perfil cadastrado ainda!')

    st.page_link('configuracoes/perfil.py', label = 'Cadastrar seu Perfil')


