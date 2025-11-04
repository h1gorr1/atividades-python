#Desenvolva um algoritmo de busca binária usando range para otimizar a busca.
partida = int(input("Digite A Partir De Qual Página Começa: "))
final = int(input("Digite Qual Vai Ser A Última Página: "))
n = int(input("Digite O Valor A Ser Encontrado Dentro Do Intervalo:"))
contador = 1
lista = []
for i in range (partida,final + 1):
    lista.append(i)

indice_partida = 0
indice_final = len(lista) - 1
meio = (indice_partida + indice_final) // 2

while lista[meio] != n:
    


    contador = contador + 1
    if lista[meio] < n:
        indice_partida = meio + 1
    else:
        indice_final = meio - 1

    meio = (indice_partida + indice_final) // 2
    print(f"indice_partida= {indice_partida} , meio= {meio}, indice_final= {indice_final}")

    

print("O Número N Leva Até: ", contador, "Casos para Ser Encontrado Na Lista!")
            


        
    