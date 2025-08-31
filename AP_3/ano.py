ano = int(input("Digite um ano: "))

if ano % 4 == 0: # Se o ano for divisível por 4, ele poderá ser bissexto
    if ano % 100 == 0: # Se ano for divisível por 100, precisa ser analisado
        if ano % 400 == 0: # Se for divisível por 400, é bissexto.
            print(f"{ano} é ano bissexto.")
        else:
            print(f"{ano} não é ano bissexto.")
    else: 
        print(f"{ano} é ano bissexto.")           
else:
    print(f"{ano} não é ano bissexto.")
    