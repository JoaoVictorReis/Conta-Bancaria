menu = "[d] Depositar \n[s] Sacar \n[e] Extrato \n[q] Sair \n  \n =>\n  \n"

saldo = 0 
limite = 0 
extrato = " "
numero_saques = 0 
limite_saques = 3

while True:
    opcao = input(menu)



    if opcao =='d':
        print('Você escolheu a opção de deposito!')
        valor = float(input('Digite o valor depositado: '))
        
        if valor > 0 :
            saldo =+ valor
            extrato = 'Deposito de R${valor.f2}'
            print('Operação realizada com sucesso!!')
        else: 
            print("O valor digitado é invalido")
        

    elif opcao == 's':
        print('Você escolheu a opção de saque!')
        valor = input(float('Informe o valor que deseja sacar: '))

        if valor > saldo:
            print('Operação falhou! Saldo insulficiente!')
        
        elif valor > limite:
            print('Operação falhou! Limite insulficiente!')
        
        elif numero_saques > limite_saques:
            print('Operação falhou! Limite de saques excedido')
        
        elif valor > 0 :
            saldo =- valor
            numero_saques =+ 1
            print('Operação realizada com sucesso!') 

    elif opcao == 'e':
        print('Voce escolheu a opção de extrato!')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break
    else:
        print('Você digitou uma operação invalida!')