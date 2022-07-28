soma = quantidade = 0
x = int(input('Digite um número [999 para parar]: '))
while x != 999:
    soma += x
    quantidade += 1
    x = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}')
