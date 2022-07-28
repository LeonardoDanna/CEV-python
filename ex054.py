from datetime import date

atual = date.today().year
maiorDeIdade = atual - 18
totalMaiores = 0
totalMenores = 0

for i in range(0 + 1, 8):
    x = int(input(f'Em que ano a {i}º pessoa nasceu? '))
    if x <= maiorDeIdade:
        totalMaiores += 1
    else:
        totalMenores += 1

print(f'No total temos {totalMaiores} maior(es) de idade \ne {totalMenores} menor(es) de idade.')
