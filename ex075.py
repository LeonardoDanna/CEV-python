lista = []
pares = []
noveAparece = posTres = 0

for i in range(0, 4):
    x = int(input('Digite um número: '))
    lista.append(x)
    if x % 2 == 0:
        pares.append(x)
    if x == 9:
        noveAparece += 1
    if x == 3:
        posTres += 1

print(f'Você digitou os valores {lista}')
if noveAparece == 0:
    pass
else:
    print(f'O valor 9 apareceu {noveAparece} vezes')

if posTres == 0:
    pass
else:
    print(f'O valor 3 apareceu na {lista.index(3)+1}º posição')

listaVaziaCheck = bool(pares)
if listaVaziaCheck == False:
    pass
else:
    print(f'Os valores pares digitados foram {pares}')
