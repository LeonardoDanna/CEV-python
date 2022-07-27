print(15 * '-=')
print('   10 TERMOS DE UMA PA')
print(15 * '-=')

x = int(input('Primeiro termo: '))
y = int(input('Razão: '))
decimo = x + (10-1) * y

for i in range(x, decimo + y, y):
    print(f'{i}', end=' -> ')

print('Acabou')
