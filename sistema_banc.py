
# Criação de sistema bancário

    
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = int(input('Informe uma opção:\n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n'))

    if opcao == 1:
        valor = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        excedeu_saque = numero_saques >= limite_saques
        excedeu_limite = valor > limite
        
        
        if excedeu_saldo:
            print('Operação falhou, voce não tem saldo suficiente')
        elif excedeu_limite:
            print('Operação falhou, saque acima do limite de R$500,00') 
        elif excedeu_saque:
            print('Operação falhou, numero de saques diários acima do permitido')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operção falhou, valor inválido.')
        
    elif opcao == 2:
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print('Operação falhou, valor inválido ')    
            
        
    elif opcao == 3:
        print('\n=============== EXTRATO ===============')
        print('Não há movimentação na conta' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=======================================')
        
    elif opcao == 4:
        break
    else:
        print('Operação inválida, digite novamente opção desejada')
    
