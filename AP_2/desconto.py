nome_produto = "Camiseta"
preco_original = 50.00
desconto = 20  # %

# Cálculo
valor_desconto = preco_original * (desconto / 100)
preco_final = preco_original - valor_desconto

# Saída
print("Produto:", nome_produto)
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto}% (R$ {valor_desconto:.2f})")
print(f"Preço final: R$ {preco_final:.2f}")
