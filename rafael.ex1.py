n1 = int(input("Digite O Valor Da 1º Notas: "))
n2 = int(input("Digite o Valor Da 2º Nota: "))
n3 = int(input("Digite o Valor Da 3º Nota: "))
n4 = int(input("Digite o Valor Da 4º Nota: "))
lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.append(n4)
print(lista)

def array(lista):
    return  sum(lista) / len(lista) #Sum Para Somar Números Dentro Dos Vetores/Array, 
#len é a quantidade de elementos dentro Do array/vetor.
print(round(array(lista),2))