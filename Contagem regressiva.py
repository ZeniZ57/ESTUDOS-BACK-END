#Hora da contagem regressiva e vou estar usando e entendendo as funçoes

import time
#aqui é a biblioteca que tem a funçao de esperar o proximo numero

for i in range(20, 0, -1): #aqui ele vai começar a contagem em 20 e vai diminuir de 1 em 1, 20 e 0 pode ser qualquer numero
    print(i) #na parte desse "i" pode ser qualquer letra
    time.sleep(1) #aqui ele vai esperar 1 segundo para mostrar o proximo numero, e o "1" pode ser qualquer numero
print("Feliz ano novo!")