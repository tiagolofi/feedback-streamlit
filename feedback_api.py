
import requests
from env import TOKEN_AUTORIZACAO

BASE_URL = 'https://feedback-ma-44f125c8ffb7.herokuapp.com'
HEADERS = {
    'Token-Autorizacao': TOKEN_AUTORIZACAO,
    'Content-Type': 'application/json'
}

def endpoint_login(cpf, senha):
    response = requests.post(
        BASE_URL + '/autenticacao/token',
        headers = HEADERS,
        json = {
            'cpf': cpf,
            'senha': senha
        }
    )
    if response.status_code == 201:
        return response.content.decode()
    return response.json()

def endpoint_foto(url, contrato, arquivo, token):
    response = requests.post(
        BASE_URL + url,
        headers = {
            'Authorization': 'Bearer ' + token,
            'Token-Autorizacao': TOKEN_AUTORIZACAO,
            'Content-Type': 'multipart/form-data'
        },
        json = contrato,
        data = arquivo
    )
    return response.json()

def endpoint_post_aberto(url, contrato):
    response = requests.post(
        BASE_URL + url,
        headers = HEADERS,
        json = contrato
    )
    return response.json()

def endpoint_put_aberto(url, contrato):
    response = requests.put(
        BASE_URL + url,
        headers = HEADERS,
        json = contrato
    )
    return response.json()

def endpoint_get_fechado(url, token):
    response = requests.get(
        BASE_URL + url,
        headers = {
            'Authorization': 'Bearer ' + token,
            'Token-Autorizacao': TOKEN_AUTORIZACAO,
            'Content-Type': 'application/json'
        }
    )
    return response.json()

def endpoint_post_fechado(url, contrato, token):
    response = requests.post(
        BASE_URL + url,
        headers = {
            'Authorization': 'Bearer ' + token,
            'Token-Autorizacao': TOKEN_AUTORIZACAO,
            'Content-Type': 'application/json'
        },
        json = contrato
    )
    return response.json()

def endpoint_put_fechado(url, contrato, token):
    response = requests.post(
        BASE_URL + url,
        headers = {
            'Authorization': 'Bearer ' + token,
            'Token-Autorizacao': TOKEN_AUTORIZACAO,
            'Content-Type': 'application/json'
        },
        json = contrato
    )
    return response.json()
