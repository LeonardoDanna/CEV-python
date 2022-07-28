x = int(input('Digite um número: '))
total = 0

for i in range(1, x + 1):
    if x % i == 0:
        print('\033[33m', end=' ')
        total+=1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {x} foi divisível {total} vezes')

if total == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
