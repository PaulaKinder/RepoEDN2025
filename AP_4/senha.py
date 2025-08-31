while True:
    senha = input("Digite a senha ou 'sair' para encerrar: ")

    # Verifica se o usuário quer sair
    if senha.lower() == "sair":
        break

    # verifica o comprimento da senha    
    if len(senha) < 8:
        print("Senha fraca. A senha precisa conter pelo menos 8 caracteres.")
        continue

    # verifica se a senha contém um número
    if not any(caracter.isdigit() for caracter in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    # verifica se a senha contém uma letra
    if not any(caracter.isalpha() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra.")
        continue

    # verifica se a senha contém um maiúscula
    if not any(caracter.isupper() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
        continue

    # se chegou até aqui, a senha é válida.
    print("Senha é forte e válida.")
    break    