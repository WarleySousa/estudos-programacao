from random import randint
from time import sleep
computador = randint(0,5)   #Faz o computador sortear
print('-=-=-=-=-=-=-=-=-=-=-=-=-' * 2)
print('Cou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-' * 2)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Eu e você pensamos no mesmo número e você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')