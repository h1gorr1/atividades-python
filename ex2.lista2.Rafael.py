# #2: Desenvolva um sistema de autenticação que permita ao usuário fazer login com
# #tentativas limitadas. O sistema deve ter diferentes níveis de usuário e implementar
# bloqueio temporário após falhas consecutivas.
# Requisitos técnicos:
#  Use while para controlar o loop de tentativas
#  Implemente try-except para tratamento de entrada
#  Use if-elif-else para diferentes níveis de acesso
#  Use range para controlar tempo de bloqueio
#  Crie função para validação de credenciais 
import time
liderdaloja = 1 
gerentedaloja = 2 
funcionariodaloja = 3
senha = 123


def validar():
    contador = 0
    while contador < 3:
        
        
        funcao = input("Digite O número de 1 a 3 que represente a sua função!: (1 para acessar como dono,2 para gerente e 3 para funcionario Público.) ")
        senhauser = input("Digite A Senha Para Ter Acesso!: (dica,123) ")
        
        try:
            funcao = int(funcao)
            senhauser = int(senhauser)
        
        except:
            print("Entrada Inválido ou inexistente,Revise O Usuario ou a senha e use apenas Números! ")
            contador += 1

        if funcao == liderdaloja and senhauser == senha: 
            print("Bem Vindo Dono Da Loja!!! ")
            
            return True
            
        elif funcao == gerentedaloja and senhauser == senha:
            print("Bem Vindo Gerente Da Loja! ")
           
            return True
        
        elif funcao == funcionariodaloja and senha == senhauser:
            print("Olá Funcionário Público Da Loja! ")
            
            return True
        else:
            print("usuário ou senha incorreta! ")
            contador += 1
    
    
        if contador == 3:
            print("Tentativas Esgotadas,Bloqueio Temporario De 30 Segundos! ")
            for i in range(30,-1,-1):
                
                print(i)
                time.sleep(1)
            contador = 0

validar()


    

