#Desenvolva um sistema de paginação usando range para dividir listas grandes.
partida = int(input("Digite A Partir De Qual Página Começa: "))
final = int(input("Digite Qual Vai Ser A Última Página: "))
lista = []
for i in range(partida,final + 1):
    lista.append(i)


print(lista)
pg = int(input("Digite Quais Das Páginas vai ser acessada!: "))
print("Na Página ", pg, "Tem O Contéudo: ",lista[pg - 1] )