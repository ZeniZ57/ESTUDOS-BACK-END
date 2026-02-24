import random

print("bem vindo ao jogo de adivinhaçao!")

numero_aleatorio = random.randint(1, 10)
tentativas = 3
while tentativas > 0:
    chute = int(input("digite um numero entre 1 e 10:"))
    if chute == numero_aleatorio:
        print("parabens, voce acertou!")
        break
    else:
        print("voce errou, tente novamente!")
        tentativas -= 1
        print(f"voce tem {tentativas} tentativas restantes")
        
        if tentativas == 0:
            print(f"suas tentativas acabaram, o numero era {numero_aleatorio}")
