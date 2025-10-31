# partida = int(input("Digite O Valor Que Começa: "))
# final = int(input("Digite O Valor A Ser Finalizado!: "))
# razao = int(input("Digite O Valor Da Razão: "))
# pa = []

# for i in range (partida,final +1 ,razao):
#     pa.append(i)
   
# print(pa)

partida = int(input("Digite O Valor Que Começa: "))
final = int(input("Digite O Valor A Ser Finalizado!: "))
razao = int(input("Digite O Valor Da Razão: "))
pg = []

while partida <= final:
    pg.append(partida)
    partida = partida * razao
    
print(pg)


