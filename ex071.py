print(10 * '-=')
print('    BANCO ROQ    ')
print(10 * '-=')

x = int(input('Que valor você quer sacar? R$'))
atual = x
nota1 = nota10 = nota20 = nota50 = 0

while atual >= 50:
    if x >= 50 and atual >= 0:
        atual -= 50
        nota50 += 1
    else:
        break

while 20 <= atual <= 50:
    if x >= 20 and atual >= 0:
        atual -= 20
        nota20 += 1
    else:
        break

while 10 <= atual <= 20:
    if x >= 10 and atual >= 0:
        atual -= 10
        nota10 += 1
    else:
        break

while 1 <= atual <= 10:
    if x >= 1 and atual >= 0:
        atual -= 1
        nota1 += 1
    else:
        break

print(10 * '-=')
print(f'Seu saque contará com:\n', end='')
if nota50 != 0:
    print(f'{nota50} nota(s) de R$50')
if nota20 != 0:
    print(f'{nota20} nota(s) de R$20')
if nota10 != 0:
    print(f'{nota10} nota(s) de R$10')
if nota1 != 0:
    print(f'{nota1} nota(s) de R$1: ')
print(10 * '-=')

''' RESOLUÇÃO DO GUANABARA
x = int(input('Que valor você quer sacar? R$'))
total = x
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''