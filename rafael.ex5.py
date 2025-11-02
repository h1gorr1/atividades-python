#Implemente um gerador de coordenadas para grade 2D usando range aninhado.
x = int(input("Digite O Valor De X: "))
y = int(input("Digite O Valor De y: "))
arrayx = []
arrayy = []
contador = 0
i = 0
resultado = []

for i in range(0,x+1,1):
    arrayx.append(i)
for i in range(0,y+1,1):
    arrayy.append(i)

for i in arrayx:
    for j in arrayy:
        coordenadas = f"{i},{j}"
        resultado.append(coordenadas)
print(resultado)

        






        
    

        

