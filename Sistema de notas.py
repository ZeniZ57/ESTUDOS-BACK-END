#Sistema que calcula a média de um aluno e diz se ele foi aprovado, reprovado ou de recuperaçao
continuar = "s"

while continuar == "s":

 media = float(input("digite a nota do aluno:"))

 if media >= 7:
    print("aluno aprovado!!")

 elif media >= 6:
    print("aluno de recuperaçao!!")

 else:
    print("aluno reprovado!!")
    continuar = input("quer calcular a média de outro aluno? (s/n)")

print("obrigado por usar o sistema de notas!")
    

