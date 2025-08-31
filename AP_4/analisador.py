def analisador_numero():

    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou digite 'fim' para encerrar): ")

        if entrada.lower() == "fim":
            print("Programa encerrado.")
            break

        try:    
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é par.")
                pares = pares + 1 # pares += 1
            else:
                print(f"O número {numero} é ímpar.")    
                impares += 1 
        except ValueError:
            print("Erro encontrado. Por favor, digite apenas números inteiros.")        

    print("\nResultado Final")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")                
        
analisador_numero()