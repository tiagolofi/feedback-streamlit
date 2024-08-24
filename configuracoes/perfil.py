import streamlit as st
from io import BytesIO
import base64
from feedback_api import endpoint_post_fechado, endpoint_foto

st.write('### Cadastrar Novo Perfil')

with st.form('cadastro'):
    matricula = st.text_input('Matrícula', max_chars=8)
    nome = st.text_input('Nome:')
    apelido = st.text_input('Apelido:')
    adjunta = st.selectbox('Adjunta:', ['SAF', 'SAAS', 'SAAD', 'SAPAPVS', 'SAAJ', 'Gabinete'])
    cargo = st.text_input('Cargo')
    setor = st.text_input('Setor')
    cadastrar = st.form_submit_button('Cadatrar Perfil')
    if cadastrar:
        endpoint_post_fechado(
            url = '/perfil/novo',
            contrato = {
                'cpf': st.session_state.usuario_logado,
                'matricula': matricula,
                'nome': nome.title(),
                'apelido': apelido,
                'adjunta': adjunta,
                'cargo': cargo.title(),
                'setor': setor.title()
            },
            token = st.session_state.token
        )

with st.form('foto'):
    file = st.file_uploader('Imagem', type = ['png', 'jpeg', 'jpg'])
    enviar = st.form_submit_button('Enviar')

    if enviar:
        endpoint_foto(
            url = '/foto/nova/',
            contrato = {
                'cpf': st.session_state.usuario_logado,
                'filename': file.name
            },
            arquivo = {'data': file.read()},
            token = st.session_state.token
        )

if file is not None:
    st.image(file)
