import os


def cls():
    os.system('cls')  # Comando para limpar a tela no Windows


def valorint(n_passagem, linha):
    return n_passagem * linha


def desconto(n_passagem, c_passagem, linha):
    talt = (n_passagem * linha) + (c_passagem * linha) / 2
    return talt


def compra(linha, pagamento):
    n_passagem = int(input('Número de passagens inteiras: '))
    crian = int(input('Há crianças ou estudantes\n[1] Sim ou [2] Não: '))
    if crian == 1:
        c_passagem = int(input('Número de passagens meia entradas: '))
        valor_total = desconto(n_passagem, c_passagem, linha)
        pagar = int(input(f'Valor a ser pago Sem desconto é {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
        if pagar == 1:
            pagar = valor_total
            pagamento.append(pagar)
        else:
            print('Compra cancelada.')
        print('Passagem comprada com sucesso.')
    else:
        valor_total = valorint(n_passagem, linha)
        pagar = int(
            input(f'Valor a ser pago Sem desconto é {valor_total}: \nConfirmar pagamento [1] Sim [2] Não: '))
        if pagar == 1:
            pagar = valor_total
            pagamento.append(pagar)
        else:
            print('Compra cancelada.')
        print('Passagem comprada com sucesso.')
    passagem = {'Linha': '[Monteiro => João Pessoa]', 'quatidade de passagem': n_passagem,
                'valor total': valor_total}
    return passagem
