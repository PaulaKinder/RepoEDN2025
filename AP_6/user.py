import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/' 

    try: 
        response = requests.get(url)
        response.raise_for_status()
        usuario = response.json()['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter usuário: {e}")

def main ():
    print("Gerando um usuário aleatório...")
    usuario = obter_usuario_aleatorio()
    print(usuario)

if __name__ == "__main__":
    main()