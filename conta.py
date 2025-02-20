menu = "[d] Depositar \n[s] Sacar \n[e] Extrato \n[q] Sair \n[cru] Criar Usuario \n[co] Criar Conta \n  \n =>\n  \n"



def depositar(valor, saldo, extrato):
        if valor > 0 :
            saldo =+ valor
            extrato = 'Deposito de R${valor.f2}'
            print('Operação realizada com sucesso!!')
        else: 
            print("O valor digitado é invalido")
        return saldo, extrato

def sacar(*,valor, saldo, extrato, numero_saques, limite_saques, limite):
    if valor > saldo:
            print('Operação falhou! Saldo insulficiente!')
        
    elif valor > limite:
        print('Operação falhou! Limite insulficiente!')
        
    elif numero_saques > limite_saques:
        print('Operação falhou! Limite de saques excedido')
        
    elif valor > 0 :
        saldo =- valor
        numero_saques =+ 1
        extrato = f'Foram sacados {valor} da sua conta'
        print('Operação realizada com sucesso!')
        
    return extrato 
    
    #Adicionar um elif de extrato
    #retornar valores

def extrator(saldo,/, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    usuario = ValidarUsuario()


def CriarUsuario(usuarios):
    cpf = input('Informe por favor o seu CPF: ')
    usuario = ValidarUsuario(usuarios, cpf)
    
    if usuario:
        print('Esse CPF já possui cadastro em nosso banco!!')
    
    nome = input('Digite seu nome: ')
    dtn = input('Qual sua data de nascimento? ')
    logr = input('Digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    
    usuarios.append({"cpf":cpf,"nome":nome, "dnasc":dtn, "logr":logr, "agencia":'0001', "conta": None })
    
    print('Usuario Criado!')
    print(usuarios)
    
    return "Usuario cadastrado com Sucesso!!", usuarios

def ValidarUsuario(usuarios, cpf):
    filtro_usuario= [usuario for usuario in usuarios if usuarios["cpf"] == cpf ]
    return filtro_usuario[0] if filtro_usuario else None

def CriarConta(usuarios):
    cpf = input('Digite o seu CPF: ')
    buscando_usuario = ValidarUsuario(usuarios, cpf)
    
    if buscando_usuario:
        print('Não existe usuario cadastrado!')
        return
        
    
   
    numConta = 1
    while numConta in usuarios:
        numConta = numConta + 1
            
    contas = []
    contas.append(numConta)
    contascopy = contas.copy()
    contas.clear()
        
    print(contascopy)
        
    usuarios[cpf]["conta"] = contascopy
    print(usuarios)
        
    return usuarios
    

def main():

    saldo = 0 
    extrato = " "
    usuarios = []
    
    while True:
        opcao = input(menu)

        if opcao =='d':
            print('Você escolheu a opção de deposito!')
            valor = float(input('Digite o valor depositado: '))
            depositar(valor, saldo, extrato)
            
        elif opcao == 's':
            print('Você escolheu a opção de saque!')
            valor = float(input('Informe o valor que deseja sacar: '))
            sacar(valor = valor,saldo = saldo, extrato = extrato, numero_saques = 0, limite_saques = 3, limite = 500)

        elif opcao == 'e':
            print('Voce escolheu a opção de extrato!')   
            extrator(saldo, extrato = " ")
        
        elif opcao == 'cru':
            esc = input('Você é um novo usuario? S -sim & N -não')
            if esc == "S":
                CriarUsuario(usuarios)
            elif esc == 'N':
                print('Okay!!')
                break
            
        elif opcao == 'co':
            print('Voce deseja criar uma nova conta?')
            CriarConta(usuarios)
        
        elif opcao == 'q':
            break
        
        else:
            print('Você digitou uma operação invalida!')
        
        
main()