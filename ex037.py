x = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[ 1 ] BINÁRIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')

y = int(input('Sua opção: '))

if y == 1:
    print(f'{x} convertido para BINÁRIO é igual a {bin(x)[2:]}')
elif y == 2:
    print(f'{x} convertido para OCTAL é igual a {oct(x)[2:]}')
elif y == 3:
    print(f'{x} convertido para HEXADECIMAL é igual a {hex(x)[2:]}')
else:
    print('Opção inválida. Tente novamente')