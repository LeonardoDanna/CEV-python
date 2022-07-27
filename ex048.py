x = 0
y = 0
for i in range(0, 501, 1):
    # números impares e divisíveis por 3 entre 0 e 500.
    if i % 2 != 0 and i % 3 == 0:
        x += i
        y += 1
print(f'A soma de todos os {y} valores solicitados da {x}')
