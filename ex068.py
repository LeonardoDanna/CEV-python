from random import randint
print(20*'-')
print('Vamos jogar par ou impar!')
print(20*'-')

computador = randint(0, 10)
ganhou = False
vitorias = 0

while True:
    x = int(input('Digite um valor: '))
    total = x + computador
    y = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {x} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if y == 'P':
        if total % 2 == 0:
            print('Você venceu! \nVamos jogar novamente...')
            vitorias += 1
        else:
            print(' Você perdeu')
            break

    elif y == 'I':
        if total % 2 == 1:
            print('Você venceu! \nVamos jogar novamente...')
            vitorias += 1
        else:
            print(' Você perdeu')
            break

print(f'GAME OVER! Você venceu {vitorias} vezes.')