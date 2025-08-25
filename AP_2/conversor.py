valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Conversões
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Saída
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {valor_dolar:.2f}")
print(f"Em euros: € {valor_euro:.2f}")
