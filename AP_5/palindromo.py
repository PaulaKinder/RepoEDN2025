def is_palindromo(texto):
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalnum())

    return texto_limpo == texto_limpo[::-1]


frase = input("Forneça a frase ou expressão para verificação do palíndromo: ")
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"    

print(f"A frase '{frase}' é palíndromo? {resposta}.")    