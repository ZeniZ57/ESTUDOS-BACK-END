categorias = {"Bronze":0.05, "Prata":0.10, "Ouro":0.20}

valor_total = float(input("digite o valor total da compra:"))
categoria_cliente = input("digite a categoria do cliente: ").capitalize().strip()

if categoria_cliente in categorias:
    desconto = valor_total * categorias[categoria_cliente]
    valor_final = valor_total - desconto
    print(f"categoria: {categoria_cliente}, valor do desconto: {desconto:.2f}, valor final: {valor_final:.2f}")


else:
    print("categoria invalida, sem desconto, valor final:", valor_total)

   




