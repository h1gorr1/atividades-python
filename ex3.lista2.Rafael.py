# #3: Crie um sistema que analise dados de vendas de uma empresa, calculando
# estatísticas por período, vendedor e região. O sistema deve tratar dados inconsistentes e
# gerar relatórios detalhados.
# Requisitos técnicos:
#  Use for com range para iterar por períodos
#  Implemente try-except para tratar dados inválidos
#  Use if-elif-else para categorização de desempenho
#  Crie função para cálculos estatísticos
#  Use while para menu interativo 
funcao = 0
vendas =  []

while funcao != 5:
    funcao = int(input("Digite A Função Desejada!:"))
    print("Digite 1 Para Inserir Vendas! ")
    print("Digite 2 Para Carregar Relátorios Por periodo das vendas")
    print("Digite 3 Para Carregar Relatorios Dos Vendedores")
    print("Digite 4 Para Carregar Relatorios Das Regiões! ")
    match funcao:
        case 1:
            print("Inserir Vendas!")
            produto = input("Digite O Produto: ")
            mes = int(input("Digite O Mês Da Venda (1-12)"))
            vendedor = input("Digite O Nome Do Vendedor")
            regiao = input("Digite A Região !")
            venda = [produto,mes,vendedor,regiao,]
            vendas.append(venda)
            



        case 2:
            print("Gerar relatorio por periodo")
            print(f"Relátorio Com Todas As Vendas: {mes}")
        
        case 3:
            print("Gerar Relatorios Por Vendedor")
            if len(vendedor) == 0 :
                print("Nemhum Vendedor Registrado Ainda!")
            else:
                print(f"Relátorio Dos Vendedores: {vendedor}")

        case 4:
            print("Gerar Relatorios Por Região")
            print(f"Relátorio Da Região Da Venda: {regiao} ")
        case _:
            print("Valor Inválido,Tente Uma Função De 1 A 4! ")