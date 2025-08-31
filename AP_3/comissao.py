nome_vendedor = input("Insira o nome do vendedor: ")
salario_fixo = float(input("Insira o salário fixo (Ex: 2500.00): "))
total_vendas = float(input("Insira o total de vendas (Ex: 50000.00): "))


comissao = total_vendas * 0.15

salario_total = salario_fixo + comissao


print(f"""
Nome do funcionário: {nome_vendedor}
Salário total: R$ {salario_total:.2f}
""")