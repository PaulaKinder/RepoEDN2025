lista_notas = []

while True: 

    try:
        entrada = input("Digite uma nota do aluno (ou digite 'fim' para encerrar): ")
        if entrada.lower() == "fim":
            break
        nota = float(entrada)    
        if 0 <= nota <= 10:
            lista_notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            continue    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim' para encerrar.")        

if lista_notas:
    media = sum(lista_notas) / len(lista_notas)
    print(f"Média da turma: {media:.2f}")
    print(f"Total de notas válidas registradas: {len(lista_notas)}")
else:
    print("Nenhuma nota foi lançada.")    