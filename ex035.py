print(20*'-')
print('Analisador de triângulos')
print(20*'-')

x1 = float(input('Primeiro segmento: '))
x2 = float(input('Segundo segmento: '))
x3 = float(input('Terceiro segmento: '))

if x1 < x2 + x3 and x2 < x1 + x3 and x3 < x1 + x2:
    print('É possível formar um triângulo com os segmentos acima.')
else:
    print('É impossível formar um triângulo com os segmentos acima.')

#Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado, é possível.