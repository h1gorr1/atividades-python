#1: Crie uma função que receba uma lista de valores (que podem ser números, strings ou 
#outros tipos) e retorne uma nova lista contendo apenas os números primos válidos. A 
#função deve tratar exceções para valores inválidos e usar estruturas condicionais para 
#validação. 
#Requisitos técnicos:
# Use try-except para tratar conversões inválidas 
# Implemente verificação de primo com for e range 
# Use if-elif-else para diferentes casos de validação 
# A função deve aceitar qualquer iterável como entrada 
#Exemplo:
#entrada = [2, 3, \"4\", 5, \"abc\", 7.0, 11, \"13\", None, 17] 
#saida_esperada = [2, 3, 5, 7, 11, 13, 17] 
lista = []
primos = []
contador = 0
n = int
while n != 0:
    n = input("Digite Valores,Coloque 0 Para Finalizar!: ")
    lista.append(n)
    print(lista)
    try:
        n = int(n)
    except:
        print(lista)
        continue
    
for i in (lista):
    for j in range(1,n + 1):
        if i % j == 0:
            contador = contador + 1
            if contador == 2:
                primos.append(i)
print(primos)


        




# for i in range
# def primos(lista):
#     for i in lista(i,)


