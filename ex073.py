count = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama',
         'Sport Recife', 'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print(30*'--')
print(f'Lista de times do brasileirão: {count}')
print(30*'--')
print(f'Os 5 primeiros são: {count[:5]}')
print(30*'--')
print(f'Os 4 últimos são: {count[-4:]}')
print(30*'--')
print(f'Times em ordem alfabética: {sorted(count)}')
print(30*'--')
print(f'O chapecoense está na {count.index("Chapecoense") + 1}º posição')
