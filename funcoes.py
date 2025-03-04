import os
def cls():
    os.system('cls')  # Comando para limpar a tela no Windows


def valorint(n_passagem, linha):
   return n_passagem * linha
   


def valor1(n_passagem, c_passagem, linha): # desconto por criança 
    desconto = (linha * c_passagem) + (linha * n_passagem)/2
    
    
    #n = n_passagem - c_passagem
    #i = (n * linha) / n
    #op1 = n_passagem * linha 
    #op2 = op1 - ((c_passagem * linha) / c_passagem)
    print(f'O valor com desconto é {desconto}')
    #time.sleep(0.5)
    #time.sleep(0,5)

   