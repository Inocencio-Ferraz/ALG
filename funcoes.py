import os

def cls():
    os.system('cls')  # Comando para limpar a tela no Windows


def pula_linha():
    print('=' * 60)


def valorint(n_passagem, linha):
    return n_passagem * linha


def desconto(n_passagem, c_passagem, linha):
    talt = (n_passagem * linha) + (c_passagem * linha) / 2
    return talt


def compra(linha, pagamento, historico, linha01):
    n_passagem = int(input('Número de passagens inteiras: '))
    crian = int(input('Há crianças ou estudantes\n[1] Sim ou [2] Não: '))
    if crian == 1:
        c_passagem = int(input('Número de passagens meia entradas: '))
        valor_total = desconto(n_passagem, c_passagem, linha)
        pagar = int(input(f'Valor a ser pago {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
        if pagar == 1:
            pagar = valor_total
            pagamento.append(pagar)
            print('Passagem comprada com sucesso.')
            passagem = {'Linha':'[Monteiro => João Pessoa]', 'quatidade de passagem': n_passagem, 'valor total': valor_total }
            historico.append(passagem)
        else:
            print('Compra cancelada.')
    else:
        valor_total = valorint(n_passagem, linha)
        pagar = int(input(f'Valor a ser pago Sem desconto é {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
        if pagar == 1:
            pagar = valor_total
            pagamento.append(pagar)
            print('Passagem comprada com sucesso.')
            passagem = {'linha': linha01, 'quatidade de passagem': n_passagem, 'valor total': valor_total }
            historico.append(passagem)
            
        else:
            print('Compra cancelada.')

    return valor_total
