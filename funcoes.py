import os

def cls():
    os.system('cls')  # Comando para limpar a tela no Windows


def valorint(n_passagem, linha):
   return n_passagem * linha
   

def desconto(n_passagem, c_passagem, linha):
    talt = (n_passagem * linha) + (c_passagem * linha) / 2 
    return talt
  
