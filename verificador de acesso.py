turnos = {"manha", "tarde", "noite"}

turno = input("digite o turno que voce estuda: ")

nome = input("digite o seu nome: ")

if turno == "tarde":
    print(f"acesso permitido, seja bem vindo {nome}!")

elif turno == "manha" or turno == "noite":
    print("em manutençao, volte mais tarde!")

else:
    print("acesso negado, turno invalido!")

    