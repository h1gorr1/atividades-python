#Crie um sistema de indexação reversa usando range para processar dados em diferentes direções.
partida = int(input("Digite A Partir De Qual Página Começa: "))
final = int(input("Digite Qual Vai Ser A Última Página: "))
lista = []

for i in range(partida,final +1):
    lista.append(i)

pg = int(input("Digite A Página (Aviso,A Ordem Está Do Final Para O  Começo!!!) : "))
print("Na Página:", -pg, "Tem o Conteúdo: ", lista[-pg])