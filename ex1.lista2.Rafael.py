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


n = int
while n != 0:
    n = input("Digite Valores,Coloque 0 Para Finalizar!: ")
    try:
        n = int(n)
        lista.append(n)
        print(lista)
    
    except:
        print(f" Valor Inserido Inválido({n}) Logo, Será Ignorado! ")
        print(lista)
        continue

def primos(lista):
    lprimos = []
    for i in (lista):
        contador = 0
    
        for j in range(1,i + 1):
            if i % j == 0: 
                contador = contador + 1
    
            else:
                continue
        if contador == 2:
            lprimos.append(i)
    return(lprimos)
            
    
print(primos(lista))


        







