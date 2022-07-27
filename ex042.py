x1 = float(input('Primeiro segmento: '))
x2 = float(input('Segundo segmento: '))
x3 = float(input('Terceiro segmento: '))

if x1 < x2 + x3 and x2 < x1 + x3 and x3 < x1 + x2:
    print('Com os segmentos acima é possível formar um triângulo ', end='')
    if x1 != x2 != x3 != x1:
        print('ESCALENO')
    elif x1 == x2 == x3:
        print('EQUILÁTERO')
    else:
        print('ISÓSCELES')
else:
    print('É IMPOSSÍVEL formar um triângulo com os segmentos acima.')
