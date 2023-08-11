'''Objetivo: Criar um sistema bancário que permita sacar, depositar e visualizar extrato.'''

from time import sleep

cont = 'S'
deposito = 0
saque = 0
saldo = 0
saque_diario = 0
limite_diario = 0

while True:
    print('--'*40)
    print('''Olá! Eu sou assistente virtual do Banco PY,digite o que deseja para continuarmos:
          
[ 0 ] VISUALIZAR EXTRATO
[ 1 ] SACAR
[ 2 ] DEPOSITAR
[ 3 ] SAIR''')
    
    selecao = int(input("Cliente: "))
    
    if selecao == 0:
        print('SEU EXTRATO BANCÁRIO:')
        sleep(0.5)
        print(f'DEPOSITO: R${deposito} ')
        print(f'SAQUE: R${saque} ')
        print(f'SALDO ATUAL: R$ {deposito - saque}')
        
    elif selecao == 1:
        
       saque = int(input('Digite o valor que deseja sacar: R$'))
       print(f'Saque de R${saque} realizado com sucesso.')
       
       saque_diario += 1
       saldo -= saque
       
                              
       if saque_diario > 3:  
           print('Limite de saque diário excedido!')
           
       if limite_diario == 1500:
           print('Limite diário excedido!')
    
       if saque > saldo:
           print('Você não tem saldo suficiente!')
           
                                 
    elif selecao == 2:
        deposito = float(input('Digite o valor que você deseja depositar: R$'))
        print(f'O Depósito de {deposito} foi realizado com sucesso.')
        saldo += deposito
        sleep(1)
                   
    
    elif selecao == 3:
        break
