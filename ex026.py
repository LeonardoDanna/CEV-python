x = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {x.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {x.find("A") + 1}')
print(f'A última letra A apareceu na posição {x.rfind("A") + 1}')  # rfind procura da direita para a esquerda
