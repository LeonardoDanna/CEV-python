x = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas fica {x.upper()}')
print(f'Seu nome em minúsculas fica {x.lower()}')
print(f"Seu nome tem ao todo {len(x) - x.count(' ')} letras")
#print(f'Seu primeiro nome é {x.find(" ")} e ele tem {x} letras')
separa = x.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')