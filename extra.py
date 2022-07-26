x = int(input('Quantos anos você tem? '))
if x <= 49:
    print('Sua CNH é válida por 10 anos')
if 50 <= x <= 69:
    print('Sua CNH é válida por 5 anos')
if x >= 70:
    print('Sua CNH é válida por 3 anos')
print('Após esse período é necessário a renovação da CNH')