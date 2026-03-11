#sistema de desconto de uma loja
categorias = {"Bronze":0.05, "Prata":0.10, "Ouro":0.20}
#aqui sao as categorias 

valor_total = float(input("digite o valor total da compra:")) 
#aqui o cliente vai dar o valor totla da compra
categoria_cliente = input("digite a categoria do cliente: ").capitalize().strip()
#o cliente vai digitar a categoria dele

if categoria_cliente in categorias:
    desconto = valor_total * categorias[categoria_cliente]
    valor_final = valor_total - desconto
    print(f"categoria: {categoria_cliente}, valor do desconto: {desconto:.2f}, valor final: {valor_final:.2f}")
    #aqui o programa vai mostrar o valor total da compra, a categoria do cliente e o valor final


else:
    print("categoria invalida, sem desconto, valor final:", valor_total)
    #se nao for nenhuma das tres categorias, vai ser invalido

   






