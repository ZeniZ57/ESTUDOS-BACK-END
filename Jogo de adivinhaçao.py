#jogo de adivinhação
import random
#biblioteca

print("bem vindo ao jogo de adivinhaçao!")
#mensagem de boas vindas

numero_aleatorio = random.randint(1, 10) #o usuario deve acertar o chute de 1 a 10
tentativas = 3 #ele tem tres tentativas
while tentativas > 0:
    chute = int(input("digite um numero entre 1 e 10:")) #o usuario vai digitar um numero para o chute
    if chute == numero_aleatorio:
        print("parabens, voce acertou!") #mensagem de vitoria
        break #se o usuario acertar, aparece a mensagem de vitoria e nisso o jogo termina
    else:
        print("voce errou, tente novamente!") #mensagem de aviso caso nao consiga acertar o numero durante o jogo
        tentativas -= 1 #vai perdendo 1 tentativa a cada erro
        print(f"voce tem {tentativas} tentativas restantes")
        #aqui ele avisa quantas tentativas o usuario tem
        
        if tentativas == 0:
            print(f"suas tentativas acabaram, o numero era {numero_aleatorio}")
            #quando as chances zeram aparece essa mensagem e o numero sorteado

