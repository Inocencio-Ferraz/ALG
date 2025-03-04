import time
import funcoes 
# Funções do programa

opcao = 0
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
        print('[ 1 ] [Monteiro => João Pessoa] \n 1 pessoa -> 100R$ - 06:00 => 12:00 ')
        time.sleep(0.5)
        print('='*40)
        print('[ 2 ] [Monteiro => Campina Grande]\n 1 pessoa -> 55R$ - 07:00 => 11:15')
        print('=' * 40)
        time.sleep(0.5)
        print('[ 3 ] [Monteiro => Sumé]\n 1 pessoa -> 13R$  07:30 => 08:10')
        print('=' * 40)
        time.sleep(0.5)
        print('[ 4 ] [Monteiro => Serra Brabca]\n 1 pessoa -> 25R$ - 08:00 => 09:20')
        print('=' * 40)

        linha = int(input('Qual linha você deseja: '))
        if linha == 1:
            n_passagem = int(input('Quantas passagens: '))
            crian = int(input('Há crianças: [ 1 ] sim [ 2 ] não: '))
            if crian == 1: 
                idade = int(input('A(s) Crianças são menores? [ 1 ] sim [ 2 ] não: '))
                if idade == 1:
                    c_passagem = int(input('Quantas crianças: '))
                    valor_total = funcoes.valor1(n_passagem, c_passagem, linha)
                else:
                    print('Sem desconto!')                   
            linha = 100
            valor_total = funcoes.valorint(n_passagem,  linha)
            pagar = int(input(f'Valor a ser pago Sem desconto é {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            if pagar == 1:
                pagar = valor_total
                pagamento.append(pagar)
            else:
                print('Compra cancelada.')
            print('Passagem comprada com sucesso.')

        elif linha == 2:
            n_passagem = int(input('Quantas passagens você deseja: '))
            crian = int(input('Há crinaças: [ 1 ] sim [ 2 ] não: '))
            if crian == 1:
                idade = int(input('A(s) Crianças são menores de idade? [ 1 ] sim [ 2 ] não: '))
                if idade == 1:
                     c_passagem = int(input('Quantas crianças: '))
                     valor_total = funcoes.valor1(n_passagem, c_passagem, linha)
                if idade == 2:
                    print('Sem desconto!')
                    valor_total = funcoes.valorint(n_passagem, linha)
            linha = 55
            pagar = int(input(f'Valor a ser pago {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
            if pagar == 1:
                pagar = valor_total
                pagamento.append(pagar)
            else:
                print('Compra cancelada.')
            pagamento.append(pagar)
            print('Passagem comprada com sucesso.')

        elif linha == 3:
            n_passagem = int(input('Quantas passagens você deseja: '))
            c_passagem = int(input('Quantas crianças: '))
            linha = 13
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
            n_passagem = int(input('Quantas passagens você deseja: '))
            c_passagem = int(input('Quantas crianças: '))
            linha = 25
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

    elif opcao == 3:
        funcoes.cls()
        sen = 0000
        senha = int(input('Digite a senha de acesso: '))
        if senha == sen:
            print('Senha Correta!')
            print('O que o funcionario deseja visualizar:\n [ 1 ] historico de passagem\n [ 2 ] Caixa da empresa')
            resp = int(input())
            if resp == 2: 
                soma = sum(pagamento)
                print(f'Caixa da empresa: {soma}R$')
        else:
            print('Senha incorreta!!')

    elif opcao == 4:
        funcoes.cls()
        print('Volte sempre.')
        break

    else:
        print('Valor inválido. Por favor, digite novamente um valor válido.')