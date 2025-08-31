nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / 10

print(f"\nMédia: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado")
elif media < 5.0:
    print("Aluno reprovado")    
else:
    print("Aluno em exame")
    exame = float(input("Digite a nota do novo exame: "))
    print(f"Nota do Exame: {exame:.1f}")

    media_final = (media + exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")    

    print(f"Média final: {media_final:.1f}")    
    
