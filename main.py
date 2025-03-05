import time
import funcoes
  
# Funções do programa

opcao = 0
linhas = [['Monteiro', 'João Pessoa', 100, '06:00', '12:00'],['Monteiro', 'Campina Grande', 55, '07:00', '11:15'],['Monteiro', 'Sumé', 13, '07:30', '08:10'],['Monteiro', 'Serra Branca', 25, '08:00', '09:00']]  #lista para as linhas de onibus 
passagem = []  # Número de passagens compradas
pagamento = []  # Receita da empresa

while opcao != 5:
    print('Viação Santa Cruz FC')
    print('[1] Linhas')
    print('[2] Limpar o terminal')
    print('[3] Modo Administrador')
    print('[4] Sair do sistema')

    opcao = int(input('Digite a opção que você deseja: '))

    if opcao == 1:
        time.sleep(0.5)
        funcoes.cls()  # Limpa a tela após a operação
        print('=' * 40)
        print(f'[ 1 ] {linhas[0][0]} => {linhas[0][1]} \n 1 pessoa -> {linhas[0][2]}R$ - Horário: {linhas[0][3]} => {linhas[0][4]}')
        time.sleep(0.5)
        print('='*40)
        print(f'[ 2 ] {linhas[1][0]} => {linhas[1][1]} \n 1 pessoa -> {linhas[1][2]}R$ - Horário: {linhas[1][3]} => {linhas[1][4]}')
        print('=' * 40)
        time.sleep(0.5)
        print(f'[ 3 ] {linhas[2][0]} => {linhas[2][1]}]\n 1 pessoa -> {linhas[2][2]}R$ - Horário: {linhas[2][3]} => {linhas[2][4]}')
        print('=' * 40)
        time.sleep(0.5)
        print(f'[ 4 ] {linhas[3][0]} => {linhas[3][1]}\n 1 pessoa -> {linhas[3][2]}R$ - Horário: {linhas[3][3]} => {linhas[3][4]}')
        print('=' * 40)

        linha = int(input('Qual linha você deseja: '))
        if linha == 1:
            linha = 100
            n_passagem = int(input('Quantas passagens: '))
            crian = int(input('Há crianças: [ 1 ] sim [ 2 ] não: '))
            if crian == 1:
                    c_passagem = int(input('Quantos menores de idade: '))
                    valor_total = funcoes.desconto(n_passagem, c_passagem, linha)
                    pagar = int(input(f'Valor a ser pago Sem desconto é {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            else:
                print('Sem desconto!')                   
            valor_total = funcoes.valorint(n_passagem,  linha)
            pagar = int(input(f'Valor a ser pago Sem desconto é {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            if pagar == 1:
                pagar = valor_total
                pagamento.append(pagar)
            else:
                print('Compra cancelada.')
            print('Passagem comprada com sucesso.')

        elif linha == 2:
            linha = 55
            n_passagem = int(input('Quantas passagens você deseja: '))
            crian = int(input('Há crinaças: [ 1 ] sim [ 2 ] não: '))
            if crian == 1:
                idade = int(input('A(s) Crianças são menores de 12 anos? [ 1 ] sim [ 2 ] não: '))
                if idade == 1:
                     c_passagem = int(input('Quantas crianças: '))
                     valor_total = funcoes.valor1(n_passagem, c_passagem, linha)
                if idade == 2:
                    print('Sem desconto!')
                    valor_total = funcoes.valorint(n_passagem, linha)
           
            pagar = int(input(f'Valor a ser pago {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            if pagar == 1:
                pagar = valor_total
                pagamento.append(pagar)
            else:
                print('Compra cancelada.')
            pagamento.append(pagar)
            print('Passagem comprada com sucesso.')

        elif linha == 3:
            linha = 13
            n_passagem = int(input('Quantas passagens você deseja: '))
            c_passagem = int(input('Quantas crianças: '))
            valor_total = funcoes.valor(n_passagem, c_passagem, linha)
            pagar = int(input(f'Valor a ser pago {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            if pagar == 1:
                pagar = valor_total
                pagamento.append(pagar)
            else:
                print('Compra cancelada.')
            pagamento.append(pagar)
            print('Passagem comprada com sucesso.')

        elif linha == 4:
            linha = 25
            n_passagem = int(input('Quantas passagens você deseja: '))
            c_passagem = int(input('Quantas crianças: '))
            valor_total = funcoes.valor(n_passagem, c_passagem, linha)
            pagar = int(input(f'Valor a ser pago {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            if pagar == 1:
                pagar = valor_total
                pagamento.append(pagar)
            else:
                print('Compra cancelada.')
            pagamento.append(pagar)
            print('Passagem comprada com sucesso.')

        else:
            print('Digite um valor válido.')
        funcoes.cls()


    elif opcao == 2:
      funcoes.cls()  # Limpa a tela após a operação

    elif opcao == 3:   #modo adm
        funcoes.cls()
        sen = 0000      #senha de acesso
        senha = int(input('Digite a senha de acesso: '))
        if senha == sen:
            while True: 
                print('Senha Correta!')
                print('O que o funcionario deseja visualizar:\n [ 1 ] historico de passagem\n [ 2 ] Caixa da empresa\n [ 3 ] Editar linhas de Onibus\n [ 4 ] Sair do modo adimin')
                resp = int(input())
                if resp == 2: 
                    soma = sum(pagamento)
                    print(f'Caixa da empresa: {soma}R$')
                if resp ==3:  #opção para adicionar e excluir linhas de onibus na lista. 
                    funcoes.cls()
                    print('O que o funcionario deseja editar?\n [ 1 ] para adicionar novas linhas\n [ 2 ] para excluir linhas antigas')
                    op = int(input())
                    if op == 1: #opção para adicionar linhas de ônibus na lista principal
                        print('Para adicionar novas linhas faça o que se pede:')
                        nova_linha = []
                        saida = str(input('Coloque a seguir a cidade de saída do ônibus: '))
                        nova_linha.append(saida)
                        chegada = str(input('Coloque a seguir a cidade de chegada do ônibus: '))
                        nova_linha.append(chegada)
                        preco = float(input('Coloque a seguir o preço da passagem: '))
                        nova_linha.append(preco)
                        hora1 = str(input('Coloque a seguir o horário de saida do ônibus em formato 00:00 : '))
                        nova_linha.append(hora1)
                        hora2 = str(input('Coloque a seguir o horario de chegada do ônibus em formato 00:00 : '))
                        nova_linha.append(hora2)
                        linhas.append(nova_linha)
                        print('Essas são as linhas de ônibus atuais:')
                        print(linhas)
                    if op == 2:  #opção para excluir linhas de ônibus na lista principal
                        print('Para excluir linhas de ônibus faça o que se pede:\nEssas são as linhas de ônibus disponiveis no catalogo:')
                        print(linhas)
                        print('Essas linhas são listas que possuem as informações de cada linha de ônibus, de 0 a x(quantidade de linhas de ônibus no total), selecione a lista que você deseja excluir.')
                        excluir = int(input())
                        linhas.pop(excluir)
                        print('linha de ônibus excluida!\nEssas são as linhas que continuaram no catalogo.')
                        print(linhas)
                    else: 
                        print('opção invalida, tente novamente.')
                if resp == 4:
                    print('Saindo do modo adimin')
                    break
        else:
            print('Senha incorreta!!')
        #Criar a receita da empresa
    
    elif opcao == 4:
        funcoes.cls()
        print('Volte sempre.')
        break

    else:
        print('Valor inválido. Por favor, digite novamente um valor válido.')
