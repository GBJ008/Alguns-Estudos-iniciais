
import requests
import json




host_login = "https://api.plugestoque.com.br/auth/login"


def login(email, password):
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json" 
        }
    payload = json.dumps({
        "email": email,
        "password": password
    })

    response = requests.request("POST", host_login, data=payload,  headers=headersList)
    return response.json()


def skus(token, page):

    host = "https://api.plugestoque.com.br/catalog-products?term=&per_page=1000&supplier_id=4&page="+ str(page)

    headersList = {
    "Accept": "*/*",
    "Authorization": "Bearer " + token 
    }

    payload = ""

    response = requests.request("GET", host, data=payload,  headers=headersList)

    return response.json()


def qtd_skus(token):

    host = "https://api.plugestoque.com.br/catalog-products?term=&per_page=1000&supplier_id=4&page=14"

    headersList = {
    "Accept": "*/*",
    "Authorization": "Bearer " + token 
    }

    payload = ""

    response = requests.request("GET", host, data=payload,  headers=headersList)

    return response.json()['from']


def publishs(data):

    data = []
    for row in data:

        publish = row['publish']
        if publish == []:
            data.append(row)

    return data


def sku_product(sku, token):

    host = f'https://api.plugestoque.com.br/catalog-ads?per_page=50&sku={sku}&supplier_id=4'
    headersList = {
        "Accept": "*/*",
        "Authorization": "Bearer " + token 
    }
    payload = ""
    response = requests.request("GET", host, data=payload,  headers=headersList)
    return response.json()


if __name__ == "__main__":

    data = []

    auth = login(
        email = "lekantatransportes@hotmail.com",
        password = "1234"
    )

    if not auth.get('token_type'):
        print("Erro")

    
    bearer = auth['access_token']


    qtd = qtd_skus(bearer)

    qtd = round(qtd/1000) + 1

    for row in range(qtd + 1):
        data_skus = skus(bearer, row)
        response = publishs(data_skus['data'])

    a=1
