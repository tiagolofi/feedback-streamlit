
import requests
from env import TOKEN_AUTORIZACAO

BASE_URL = 'https://feedback-ma-44f125c8ffb7.herokuapp.com'

def token(cpf, senha):
    response = requests.post(
        BASE_URL + '/autenticacao/token',
        headers = {
            'Token-Autorizacao': TOKEN_AUTORIZACAO,
            'Content-Type': 'application/json'
        },
        json = {
            'cpf': cpf,
            'senha': senha
        }
    )
    if response.status_code != 201:
        return response.json()
    return response.content.decode()

def novo(cpf, senha, acessos: list):
    response = requests.post(
        BASE_URL + '/usuario/novo',
        headers = {
            'Token-Autorizacao': TOKEN_AUTORIZACAO,
            'Content-Type': 'application/json'
        },
        json = {
            'cpf': cpf,
            'senha': senha,
            'acessos': acessos
        }
    )
    return response.json()
