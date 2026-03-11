# vamos fazer uma calculadora
continuar = "s"

while continuar == "s":

             
 num1 = float(input("digite o primeiro numero:")) #aqui nessa parte, eu coloquei para o usuario escolher um numero
 num2 = float(input("digite o segundo numero:")) #aqui nessa parte, eu coloquei para o usuario escolher um numero 
 operaçao = input("digite a operaçao que deseja realizar (+, -, *, /):") #aqui o usuario vai escolher dentre as 4 operaçoes basicas

 if operaçao == "+":
    resultado = num1 + num2
    print(f"o resultado de {num1} + {num2} é {resultado}")
   #nessa parte irá mostrar o resultado do calculo se o usuario escolheu a operaçao acima

 elif operaçao == "-":
    resultado = num1 - num2
    print(f"o resultado de {num1} - {num2} é {resultado} ")
   #nessa parte irá mostrar o resultado do calculo se o usuario escolheu a operaçao acima

 elif operaçao == "*":
    resultado = num1 * num2
    print(f"o resultado de {num1} * {num2} é {resultado}")
   #nessa parte irá mostrar o resultado do calculo se o usuario escolheu a operaçao acima

 elif operaçao == "/":
    resultado = num1 / num2
    print(f"o resultado de {num1} / {num2} é {resultado}")
   #nessa parte irá mostrar o resultado do calculo se o usuario escolheu a operaçao acima
    
 else: 
    print("operaçao invalida, tente novamente!")
   #essa parte será ativada se o usuario escolher uma operaçao que nao seja uma das 4

 continuar = input("deseja realizar outra operaçao? (s/n):")
  #aqui é uma mensagem perguntando ao usuario se ele gostaria de continuar a calcular

print("ate a proxima!")











