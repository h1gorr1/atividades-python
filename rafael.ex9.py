#Crie um sistema de calendário que use range para gerar datas
dia = int(input("Digite O Dia Desejado!: "))
mes = int(input("Digite O Mes Desejado Também!: "))
for x in range(1,mes + 1):
    print(f"Meses Gerados: {x}")
    for y in range(1,dia + 1):
       print(f" Dia {y} Do Mês {x}")