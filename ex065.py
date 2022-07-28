resp = 'S'
quant = soma = menor = maior = 0

while resp in 'Ss':
    x = int(input('Digite um número: '))
    quant += 1
    soma += x
    if quant == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

print(f'Você digitou {quant} números e a média foi {(soma / quant):.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
