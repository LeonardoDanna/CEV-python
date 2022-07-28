contador = soma = x = 0
while True:
    x = int(input('Digite um valor [999 para parar]: '))
    if x == 999:
        break
    contador += 1
    soma += x
print(f'A soma dos {contador} valores foi {soma}')
