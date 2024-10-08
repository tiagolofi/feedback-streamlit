import streamlit as st
from feedback_api import endpoint_post_aberto, endpoint_login

if 'token' not in st.session_state:
    st.session_state.token = ''

def login():
    cpf = st.text_input('CPF', max_chars = 11)
    senha = st.text_input('Senha', type = 'password')

    if st.button('Log in'):
        st.session_state.token = endpoint_login(cpf, senha)
        st.session_state.usuario_logado = cpf
        st.rerun()

def register():
    cpf = st.text_input('CPF', max_chars = 11)
    senha = st.text_input('Senha', type = 'password')
    acessos = st.multiselect('Acessos', ['admin', 'user', 'moderator']) 

    if st.button('Cadastrar'):
        resultado = endpoint_post_aberto(
            url = '/usuario/novo',
            contrato = {
                'cpf': cpf,
                'senha': senha,
                'acessos': acessos  
            }    
        )
        st.info(resultado)
        st.rerun()

def logout():
    if st.button('Log out'):
        st.session_state.token = ''
        st.rerun()

login_page = st.Page(login, title='Log in', icon=':material/login:')
register_page = st.Page(register, title='Register', icon=':material/login:')
logout_page = st.Page(logout, title='Log out', icon=':material/logout:')

dashboard = st.Page('dashboard/inicio.py', title='Início', icon=':material/search:', default=True)
feedbacks = st.Page('feedback/comentarios.py', title='Comentários', icon=':material/bug_report:')
perfil = st.Page('configuracoes/perfil.py', title='Perfil', icon=':material/history:')
credenciais = st.Page('configuracoes/credenciais.py', title='Gestão de Credenciais', icon=':material/notification_important:')

if st.session_state.token != '':
    pg = st.navigation(
        {
            'Início': [dashboard],
            'Feedback': [feedbacks],
            'Configurações': [perfil, credenciais],
            'Sair': [logout_page]
        }
    )
else:
    pg = st.navigation([login_page, register_page])

pg.run()