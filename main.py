import time
import funcoes

opcao = 0
linhas = [['Monteiro', 'João Pessoa', 100.0, '06:00', '12:00'],
        ['Monteiro', 'Campina Grande', 55.0, '07:00', '11:15'],
        ['Monteiro', 'Sumé', 13.0, '07:30', '08:10'],
        ['Monteiro', 'Serra Branca', 25.0, '08:00', '09:00']]  # lista para as linhas de onibus
passagem = []   # Número de passagens compradas
pagamento = []  # Receita da empresa
historico = []  # Histórico de passagens

while opcao != 5:
    funcoes.cls()
    try:
        print('Viação Santa Cruz FC')
        print('[1] Linhas')
        print('[2] Limpar o terminal')
        print('[3] Modo Administrador')
        print('[4] Sair do sistema')
        

        opcao = int(input('Digite a opção que você deseja: '))

        if opcao == 1:
            funcoes.cls()  # Limpa a tela após a operação
        
            for linha in linhas:
              funcoes.pula_linha()
              print(f"{linha[0]} => {linha[1]}, {linha[2]:.2f} R$, {linha[3]} => {linha[4]}")
            time.sleep(0.5)    

            linha = int(input('Qual linha você deseja: '))

            if 1 <= linha <= len(linhas):  # Verifica se a linha escolhida é válida
                funcoes.cls()
                linha_selecionada = linhas[linha - 1] #Seleciona o número correto da linha, excluindo a linha 0
                linha01 = f'{linha_selecionada[0]} => {linha_selecionada[1]}' #Saí e chega
                preco = linha_selecionada[2] #Preço da passagem
                funcoes.compra(preco, pagamento, historico, linha01)
            
            else:
                print('Digite um valor válido.')


        elif opcao == 2:
            funcoes.cls()  # Limpa a tela após a operação

        elif opcao == 3:  # modo adm
            funcoes.cls()
            sen = '1234'  # senha de acesso
            senha = input('Digite a senha de acesso: ')
            if senha == sen:
                print('Senha Correta!')
                while True:
                    print(
                        'O que o funcionario deseja visualizar:\n [ 1 ] historico de passagem\n [ 2 ] Caixa da empresa\n [ 3 ] Editar linhas de Onibus\n [ 4 ] Sair do modo adimin')
                    resp = int(input('Qual a opção desejada: '))
                    if resp == 1:
                        print(' ---- HISTORICO DE PASSAGENS ----') 
                        for e in historico:
                            funcoes.pula_linha()
                            for k, v in e.items():
                                print(f'{k} = {v}')
                            funcoes.pula_linha()


                    if resp == 2:
                        soma = sum(pagamento)
                        print(f'Caixa da empresa: {soma}R$')
                    if resp == 3:  # opção para adicionar e excluir linhas de onibus na lista.
                        funcoes.cls()
                        print(
                            'O que o funcionario deseja editar?\n [ 1 ] para adicionar novas linhas.\n [ 2 ] para excluir linhas antigas.')
                        op = int(input('Qual a opção desejada: '))
                        if op == 1:  # opção para adicionar linhas de ônibus na lista principal
                            print('Para adicionar novas linhas faça o que se pede: ')
                            nova_linha = []
                            saida = str(input('Coloque a seguir a cidade de saída do ônibus: '))
                            nova_linha.append(saida)
                            chegada = str(input('Coloque a seguir a cidade de chegada do ônibus: '))
                            nova_linha.append(chegada)
                            preco = float(input('Coloque a seguir o preço da passagem: '))
                            nova_linha.append(preco)
                            hora1 = str(input('Coloque a seguir o horário de saida do ônibus em formato 00:00: '))
                            nova_linha.append(hora1)
                            hora2 = str(input('Coloque a seguir o horario de chegada do ônibus em formato 00:00: '))
                            nova_linha.append(hora2)
                            linhas.append(nova_linha)
                            print('Essas são as linhas de ônibus atuais: ')
                            op = int(input(f'{linhas}\nConfirmar comprar dessa nova linha [1] SIM [2] NÃO: '))
                            if op == 1:
                                linha01 = f'[{saida} => {chegada}]'
                                linha = preco
                                funcoes.compra(linha, pagamento, historico, linha01)
                            else:
                                continue
                        if op == 2:  # opção para excluir linhas de ônibus na lista principal
                            print(
                                'Para excluir linhas de ônibus faça o que se pede:\nEssas são as linhas de ônibus disponiveis no catalogo:')
                            print(linhas)
                            excluir = int(input(
                                'Essas linhas são listas que possuem as informações de cada linha de ônibus, de 0 a x(quantidade de linhas de ônibus no total), selecione a lista que você deseja excluir: '))
                            linhas.pop(excluir)
                            print('linha de ônibus excluida!\nEssas são as linhas que continuaram no catalogo.')
                            print(linhas)
                        else:
                            print('opção invalida, tente novamente.')
                    if resp == 4:
                        print('Saindo do modo administrador')
                        break
            else:
                print('Senha incorreta!!')
            # Criar a receita da empresa

        elif opcao == 4:
            funcoes.cls()
            print('Volte sempre.')
            break

        else:
            print('Valor inválido. Por favor, digite novamente um valor válido.')
  
    except ValueError:
        continue
