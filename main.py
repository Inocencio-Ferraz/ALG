import time
import funcoes

running = True 
linhas = [['Monteiro', 'João Pessoa', 100.0, '06:00', '12:00'],
        ['Monteiro', 'Campina Grande', 55.0, '07:00', '11:15'],
        ['Monteiro', 'Sumé', 13.0, '07:30', '08:10'],
        ['Monteiro', 'Serra Branca', 25.0, '08:00', '09:00']]  # lista para as linhas de onibus

pagamento = []  # Receita da empresa

try:
    historico = funcoes.carregar()
except:
    historico = []

while running:
    funcoes.cls()
    try:
        print('Viação Santa Cruz FC')
        print('[1] Linhas')
        print('[2] Modo Administrador')
        print('[3] Sair do sistema')
        

        opcao = int(input('\nDigite a opção que você deseja: '))

        if opcao == 1:
            funcoes.cls()  # Limpa a tela após a operação
        
            for linha in linhas:
              funcoes.espaco()
              time.sleep(funcoes.TEMPO_DE_ESPERA / 2)
              print(f"{linha[0]} => {linha[1]}, {linha[2]:.2f} R$, {linha[3]} => {linha[4]}")
            funcoes.espaco()
            time.sleep(funcoes.TEMPO_DE_ESPERA)    

            linha = -1
            while linha < 0 or linha > len(linhas):
                linha = int(input('\nDigite para voltar ao menu [0] \nDigite o número da linha desejada: '))
                if linha == 0:
                    funcoes.cls()
                    print('Voltando...')
                    time.sleep(funcoes.TEMPO_DE_ESPERA)


                elif 1 <= linha <= len(linhas):  # Verifica se a linha escolhida é válida
                    funcoes.cls()
                    linha_selecionada = linhas[linha - 1] #Seleciona o número correto da linha, excluindo a linha 0
                    linha01 = f'{linha_selecionada[0]} => {linha_selecionada[1]}' #Saí e chega
                    preco = linha_selecionada[2] # O 2 é o preço da passagem
                    funcoes.compra(preco, pagamento, historico, linha01)
                else:
                    print('Valor invalido!')
        

        elif opcao == 2:  # modo adm
            funcoes.cls()
            sen = '1234'  # senha de acesso
            senha = input('Digite a senha de acesso: ')
            print('Analisando...')
            time.sleep(funcoes.TEMPO_DE_ESPERA)
            if senha == sen:
                print('Senha Correta!')

                admin = True
                while admin:
                    print('O que o funcionario deseja:\n [ 1 ] historico de passagem\n [ 2 ] Caixa da empresa\n [ 3 ] Editar linhas de Onibus\n [ 4 ] Sair do modo admin')
                    resp = int(input('Qual a opção desejada: '))
                    
                    if resp == 1:
                        funcoes.cls()
                        print(' ------ HISTORICO DE PASSAGENS ------') 
                        for e in historico:
                            funcoes.espaco()
                            for k, v in e.items():
                                print(f'{k} = {v}')
                            funcoes.espaco()
                    elif resp == 2:
                        funcoes.cls()
                        soma = sum(pagamento)
                        print(f'Caixa da empresa: {soma}R$')
                    elif resp == 3:  # opção para adicionar e excluir linhas de onibus na lista.
                        funcoes.cls()
                        print('O que o funcionario deseja editar?\n[ 1 ] para adicionar novas linhas.\n[ 2 ] para excluir linhas antigas.\n[ 3 ] voltar')
                        op = int(input('Qual a opção desejada: '))
                        if op == 1:  # opção para adicionar linhas de ônibus na lista principal
                            funcoes.cls()
                            print('Para adicionar novas linhas faça o que se pede: ')
                            nova_linha = []
                            saida = str(input('Coloque a seguir a cidade de saída do ônibus: '))
                            nova_linha.append(saida)
                            chegada = str(input('Coloque a seguir a cidade de chegada do ônibus: '))
                            nova_linha.append(chegada)
                            preco = float(input('Coloque a seguir o preço da passagem: '))
                            nova_linha.append(preco)
                            hora1 = str(input('Coloque a seguir o horário de saida do ônibus em formato 00:00: '))

                            while funcoes.hora_com_erro(hora1):
                                print('Valor invalido! Digite no formato solicitado: 00:00')
                                hora1 = str(input('Coloque a seguir o horário de saida do ônibus em formato 00:00: '))
                            nova_linha.append(hora1)
                            hora2 = str(input('Coloque a seguir o horario de chegada do ônibus em formato 00:00: '))

                            while funcoes.hora_com_erro(hora2):
                                print('Valor invalido! Digite no formato solicitado: 00:00')
                                hora2 = str(input('Coloque a seguir o horário de saida do ônibus em formato 00:00: '))  

                            nova_linha.append(hora2)
                            linhas.append(nova_linha)
                            print('Essas são as linhas de ônibus atuais: ')
                            op = int(input(f'{linhas}\nConfirmar comprar dessa nova linha [1] SIM [2] NÃO: '))
                            if op == 1:
                                linha01 = f'[{saida} => {chegada}]'
                                linha = preco
                                funcoes.compra(linha, pagamento, historico, linha01)
                                funcoes.cls()
                            else:
                                continue
                        elif op == 2:  # opção para excluir linhas de ônibus na lista principal [não está funcionando a opção]
                            funcoes.cls()
                            print('Para excluir linhas de ônibus faça o que se pede:\nEssas são as linhas de ônibus disponiveis no catalogo:')
                            print(linhas)
                            excluir = int(input('Selecione a lista que você deseja excluir: '))
                            while excluir < 1 or excluir > len(linhas) : #tratamento de erro pra excluir uma linha válida.
                                print(f'Valor inválido. \nDigite um valor entre 1 e {len(linhas)} ')
                                excluir = int(input('Selecione a lista que você deseja excluir: '))
                            linhas.pop(excluir - 1) 
                            print('linha de ônibus excluida!\nEssas são as linhas que continuaram no catalogo.')
                            print(linhas)
                        elif op == 3:
                            funcoes.cls()
                            print('Voltando...')
                            time.sleep(funcoes.TEMPO_DE_ESPERA)
                            continue
                        else:
                            print('opção invalida, tente novamente.')
                    if resp == 4:
                        funcoes.cls()
                        print('Saindo do modo administrador...')
                        time.sleep(funcoes.TEMPO_DE_ESPERA)
                        admin = False
            else:
                print('Senha incorreta!!')
                time.sleep(funcoes.TEMPO_DE_ESPERA)
            
        elif opcao == 3:
            funcoes.salvar(historico)
            funcoes.cls()
            print('Volte sempre.')
            running = False
            

        else:
            print('Valor inválido. Por favor, digite novamente um valor válido.')
  
    except ValueError:
        print('-------- Digite um valor correto ---------')
        time.sleep(funcoes.TEMPO_DE_ESPERA) 
        continue
    except:
        print('+++')
        time.sleep(funcoes.TEMPO_DE_ESPERA)
        continue
