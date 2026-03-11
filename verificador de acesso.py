#verificador de acesso por turnos
turnos = {"manha", "tarde", "noite"}
#aqui sao os turnos 

turno = input("digite o turno que voce estuda: ")
#o usuario vai digitar o turno

nome = input("digite o seu nome: ")
#aqui o usuario vai digitar o nome 

if turno == "tarde":
    print(f"acesso permitido, seja bem vindo {nome}!")
    #se o turno for da tarde, o usuario tem acesso ao laboratorio

elif turno == "manha" or turno == "noite":
    print("em manutençao, volte mais tarde!")
    #aqui se o turno for da manhã ou a noite, o laboratorio está em manutenção

else:
    print("acesso negado, turno invalido!")
    #se for outro turno sem ser esses tres, vai dar turno invalido


    

