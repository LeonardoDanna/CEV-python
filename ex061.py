print(15*'-=')
print('         Gerador de PA       ')
print(15*'-=')

x = int(input('Primeiro termo: '))
y = int(input('Razão da PA: '))
termo = x
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += y
    contador += 1

print('FIM')