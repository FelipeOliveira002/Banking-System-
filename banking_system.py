

menu = '''
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Qual o valor do depósito?\n'))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito de R${deposito:.2f} realizado\n'
            print('Depósito realizado!')
        else:
            print('Valor inválido!')
    
    elif opcao == 's':
        if numero_saques == LIMITE_SAQUES:
            print('Você já alcançou o limite diário de saques') 
            
        else:
            saque = float(input('Qual valor deseja sacar?\n'))
            if saque <= 0:
                print('Valor inválido!')
            
            elif saque > saldo:
                print('Saldo indisponível')
            
            elif saque > 500:
                print('Limite de saque de até R$500,00')
             
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f'Saque de R${saque:.2f} realizado\n'
                print('Saque realizado!')
    
    elif opcao == 'e':
        print()
        print(extrato)
        print(f'\nSaldo total: R${saldo:.2f}')
    
    elif opcao == 'q':
        print('Obrigado!')
        break 

    else:
        print('Opção inválida!')












