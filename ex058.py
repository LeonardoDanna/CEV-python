from random import randint

computador = randint(1, 10)
acertou = False
palpites = 0

print('Sou seu Computador\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')

while not acertou:
    x = int(input('Qual seu palpite? '))
    palpites += 1
    if x == computador:
        acertou = True
    else:
        if x < computador:
            print('Mais... Tente mais uma vez')
        elif x > computador:
            print('Menos... Tente mais uma vez')

print(f'Você acertou com {palpites} tentativas. Parabéns!')
