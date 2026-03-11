#Sistema que calcula a média de um aluno e diz se ele foi aprovado, reprovado ou de recuperaçao
continuar = "s"

while continuar == "s":

 media = float(input("digite a nota do aluno:"))
 #o usuario vai digitar a nota do aluno

 if media >= 7:
    print("aluno aprovado!!")
  #se a nota for maior ou igual a 7, o aluno é aprovado

 elif media >= 6:
    print("aluno de recuperaçao!!")
  #se o aluno tirar 6, ficou na recuperaçao
 else:
    print("aluno reprovado!!")
  #aqui se a nota for baixa, reprovaçao
    continuar = input("quer calcular a média de outro aluno? (s/n)")
  #o programa pergunta ao usuario se quer continuar a calcular as notas
print("obrigado por usar o sistema de notas!")
#essa mensagem aparece quando o usuario aperta N
    


