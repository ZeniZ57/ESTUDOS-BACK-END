# vamos fazer uma calculadora
continuar = "s"

while continuar == "s":

             
 num1 = float(input("digite o primeiro numero:"))
 num2 = float(input("digite o segundo numero:"))
 operaçao = input("digite a operaçao que deseja realizar (+, -, *, /):")

 if operaçao == "+":
    resultado = num1 + num2
    print(f"o resultado de {num1} + {num2} é {resultado}")

 elif operaçao == "-":
    resultado = num1 - num2
    print(f"o resultado de {num1} - {num2} é {resultado} ")

 elif operaçao == "*":
    resultado = num1 * num2
    print(f"o resultado de {num1} * {num2} é {resultado}")

 elif operaçao == "/":
    resultado = num1 / num2
    print(f"o resultado de {num1} / {num2} é {resultado}")
    
 else: 
    print("operaçao invalida, tente novamente!")

 continuar = input("deseja realizar outra operaçao? (s/n):")

print("ate a proxima!")










