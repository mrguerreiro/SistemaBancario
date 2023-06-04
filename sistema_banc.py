'''saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Realizando saque!...')
else:
    print('Saldo insuficiente!')    
    
saldo = saldo - saque
print (f'Seu saldo é {saldo}') '''




'''opcao = int(input('Informe uma opção:\n[1] Sacar \n[2] Saldo \n[3] Depositar'))

if opcao == 1:
    valor = float(input('Informe o valor do saque: '))
elif opcao == 2:
    print ('Seu saldo é: ') 
elif opcao == 3:
    deposito = float(input('Informe o valor do deposito: '))
else:
    print('Opção invalida')'''
    
    
    
    
#Métodos da classe string   

'''curso = 'Python'

print(curso.upper()) #tudo maiusculo
print(curso.lower()) #tudo minusculo
print(curso.title()) #Primeira maiuscula e o resto minuscula
print(curso.strip()) #retira os espaçoes em branco digitados pelo o usuário a direita e a esq.
print(curso.lstrip())#remove somente espaço da esquerda
print(curso.rstrip())#remove somente espaço da esquerda
print(curso.center(10, '#'))#centraliza a palavra preenchendo os espaços em brancos com o 
                            #caracter informado, (#)caracter informado, (10)espaço total da string
print('.'.join(curso)) #retorna P.y.t.h.o.n

print(curso.upper().center(10, '#'))
print(' '.join(curso))'''





'''nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
profissão = input('Dgite sua profissão: ' )

print(f'Meu nome é {nome}, tenho {idade} anos e trabalho como {profissão}.')'''





'''nome = 'Marcos Rogério Guerreiro'

print(nome[0])
print(nome[-2])
print(nome[:14])
print(nome[15:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])'''





'''nome = "Marcos Rogério Guerreiro"

mensagem = f

Olá meu nome é {nome},
Eu estou aprendendo Python.



print(mensagem)


nome = "Marcos Rogério Guerreiro"

mensagem =

    Olá meu nome é {nome},
Eu estou aprendendo Python.
        Esta mensagem tem diferentes recuos



print(mensagem)'''







#desafios

'''def obter_nome_mes(numero):
    meses = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return meses.get(numero, "Invalid month")

# Exemplo de uso:
numero = int(input("Digite o número do mês: "))
nome_mes = obter_nome_mes(numero)
print(nome_mes)'''







'''Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe 
pediu que construísse um programa para verificar, à partir de dois valores
muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada 
contém um inteiro N que indica a quantidade de casos de teste. 
Cada caso de teste consiste de dois valores A e B maiores que zero, c
ada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo 
valor encaixa no primeiro valor'''


'''def encaixa(a, b):
    if len(b) > len(a):
        return "nao encaixa"
    if a[-len(b):] == b:
        return "encaixa"
    else:
        return "nao encaixa"

n = int(input())  # Quantidade de casos de teste

for _ in range(n):
    a, b = input().split()  # Entrada dos valores A e B
    resultado = encaixa(a, b)
    print(resultado)'''
    
    
    
    
    
# Criação de sistema bancário

    
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = int(input('Informe uma opção:\n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair'))

    if opcao == 1:
        valor = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        excedeu_saque = numero_saques > 3
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
    
