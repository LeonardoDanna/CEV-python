from random import randint
from time import sleep

print(20 * '-')
print('Vou pensar em um número entra 0 e 5. Tente advinhar...')
print(20 * '-')

y = randint(0, 5)
x = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(1)

if x == y:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {y} e não no {x}')
