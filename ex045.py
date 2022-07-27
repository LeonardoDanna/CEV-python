from time import sleep
import random

lista = [0, 1, 2]
escolhido = random.choice(lista)

x = int(input('Suas opções:\n'
              '[ 0 ] PEDRA\n'
              '[ 1 ] PAPEL\n'
              '[ 2 ] TESOURA\n'
              'Qual é a sua jogada? '))
# Contagem
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO! !')

# Escolha do jogador
print(20*'-=')
print('Jogador escolheu: ', end='')
if x == 0:
    print('PEDRA')
elif x == 1:
    print('PAPEL')
elif x == 2:
    print('TESOURA')
else:
    print('uma opção inexistente.')

# Escolha do computador
print(f'O computador escolheu: ',end='')
if escolhido == 0:
    print('PEDRA')
elif escolhido == 1:
    print('PAPEL')
elif escolhido == 2:
    print('TESOURA')
print(20*'-=')

# Condição de empate
if x == escolhido:
    print('Empate')

# Condição de vitória
if x == 1 and escolhido == 0 or x == 0 and escolhido == 2 or x == 2 and escolhido == 1:
    print('JOGADOR ganhou!!')

# Condição de derrota
if x == 0 and escolhido == 1 or x == 1 and escolhido == 3 or x == 2 and escolhido == 0:
    print('COMPUTADOR ganhou.')


