#SISTEMA DE HABILIDADES DOS ALIENS DO OMNITRIX

aliens = {
    #AQUI ESTAO OS NOMES E HABILIDADES DOS ALIENS DO OMNITRIX
    "Chama": "tem habilidades de fogo",
    "Diamante": "tem habilidades de diamante",
    "Quatro braços": "tem super força",
    "Besta": "tem garras afiadas e é cego",
    "Aquatico": "tem poderes aquaticos",
    "Fantasmatico": "tem poderes de fantasma",
    "Idem": "habilidade de clonagem",
    "Ultra t": "tem habilidade de tecnologia",
    "Massa cinzenta": "tem um grande intelecto",
    "Cipo selvagem": "tem habilidade de planta",
    "Xlr8": " tem super velocidade",
    "Bala de canhao": "pode se tornar uma bala de canhao",
    "Frankenstrike": "tem poderes eletricos",
    "Mega olhos": "tem muitos olhos e solta laser por eles",
    "Blitzwolfer": "tem habilidades de lobo",
    "Feedback": "tem poderes de eletricidade",
    "Insectoide": "tem habilidades de inseto",
    "Gigante": "tem super força e é gigante",
    "Glutao": "o que ele come, dispara esferas explosivas"
}

print("bem vindo ao sistema de habilidade dos aliens do omnitrix!!")
#AQUI É UMA MENSAGEM DE BOAS VINDAS AO USUARIO

nome = input("digite o nome do alien que deseja saber a habilidade:").strip().capitalize()
#AQUI O USUARIO VAI DIGITAR O NOME DO ALIEN QUE ELE QUER SABER A HABILIDADE, E O PROGRAMA VAI PROCURAR NO DICIONARIO E MOSTRAR A HABILIDADE DO ALIEN, CASO O NOME DO ALIEN NAO ESTEJA NO DICIONARIO, O PROGRAMA VAI MOSTRAR UMA MENSAGEM DE ERRO

resultado = aliens.get(nome)
#AQUI O PROGRAMA VAI VERIFICAR SE O NOME DO ALIEN DIGITADO PELO USUARIO EXISTE NO DICIONARIO, SE EXISTIR ELE VAI MOSTRAR A HABILIDADE DO ALIEN, CASO CONTRARIO ELE NAO VAI MOSTRAR NADA

if resultado:
    print(f"a habilidade do alien {nome} é: {resultado}")
    #NESSA PARTE, VAI MOSTRAR O NOME DO ALIEN E A HABILIDADE

else:
    print("alien nao encontrado!")
    #SE O USUARIO ESCOLHER UM ALIEN QUE NAO ESTEJA NO DICIONARIO, RESULTARÁ COMO ALIEN NAO ENCONTRADO


