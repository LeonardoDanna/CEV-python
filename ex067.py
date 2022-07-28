while True:
    x = int(input('Quer ver a tabuada de qual valor? '))
    if x < 0:
        break
    for i in range(1,11):
        print(f'{x} * {i} = {x * i}')
print('Programa de tabuada encerrado. Volte sempre')
