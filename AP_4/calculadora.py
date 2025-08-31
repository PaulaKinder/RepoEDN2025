while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, * ou /): ").strip()
        

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
       
        # Verifica divisão por zero
            if operacao == '/' and num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                continue
            else:
                resultado = num1 / num2      
        else:
            raise ValueError("Operação Inválida")

        print(f"Resultado: {resultado}")
        break

    except ValueError as e:
        print(f"Erro {e}. Favor, tente novamente com valores numéricos.")    
   