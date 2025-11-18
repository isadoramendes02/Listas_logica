import math
import emoji
from funcoes import *
while True:
    operacoes=int(input("Escolha a operação: 1 - adição 2- subtração 3-multiplicação 4-divisão, 0 - para sair do programa:"))
    if operacoes == 1:
        print(soma())
    elif operacoes == 2:
        print(subtração())
    elif operacoes == 3:
        print(multiplicação())
    elif operacoes == 4:
        print(divisão())
    elif operacoes == 0:
        break
    print(emoji.emojize("Obrigado(a) por utilizar nosso programa!:red_heart:", variant="emoji_type"))
