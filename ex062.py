print(15*'-=')
print('         Gerador de PA       ')
print(15*'-=')

x = int(input('Primeiro termo: '))
y = int(input('Razão da PA: '))
termo = x
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += y
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} mostrados')
