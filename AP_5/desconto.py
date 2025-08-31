def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

while True:
    try:
        preco_original = float(input("Digite o preço do produto (exemplo: 250.75): "))
        desconto = float(input("Digite o percentual de desconto (exemplo: 10): "))

        if preco_original < 0 or desconto < 0:
            print("Erro: o preço e o desconto precisam ser positivos")
            continue
        break

    except ValueError:
        print("Por favor, insira um valor numérico")
        continue

preco_com_desconto = calcular_desconto(preco_original, desconto)    
print(f"O preço final com {desconto}% de desconto é: R$ {preco_com_desconto:.2f}")