a = int(input("Digite O Valor De A: "))
b = int(input("Digite O Valor De A: "))
c = int(input("Digite O Valor De A: "))
d = int(input("Digite O Valor De A: "))
lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
print(lista)

for i in range(len(lista)):
    for j in range(i +1,len(lista)):
        if lista[i] >  lista[j]:
            troca = lista[i]
            lista[i] = lista[j]
            lista[j] = troca
    print(lista)
