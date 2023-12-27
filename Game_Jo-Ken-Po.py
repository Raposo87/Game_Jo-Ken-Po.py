
from random import randint # Importando biblioteca randon, para escolha aleatoria do computador
from time import sleep # Importando temporizador
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2) # escolha aleatoria do computador apenas de 0 a 2
print('''Suas opões:
[0] PEDRA
[1] PAPEL
[2]TESOURA''')
jogador = int(input('Escolha a sua jogada entre (0, 1 ou 2): '))
if 0 <= jogador <= 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print('-=' * 11)
    print('Você jogou {}'.format(itens[jogador]))
    print('O computador jogou {}'.format(itens[computador]))
    print('-=' * 11)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('***EMPATE!***')
    elif jogador == 1:
        print('***VOCÊ VENCEU!***')
    elif jogador == 2:
        print('***COMPUTADOR VENCEU!***')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('***COMPUTADOR VENCEU!***')
    elif jogador == 1:
        print('***EMPATE!***')
    elif jogador == 2:
        print('***VOCÊ VENCEU!***')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('***VOCÊ VENCEU!***')
    elif jogador == 1:
        print('***COMPUTADOR VENCEU!***')
    elif jogador == 2:
        print('***EMPATE!***')
    else:
        print('JOGADA INVALIDA!')