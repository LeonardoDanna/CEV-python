x1 = float(input('Primeira nota: '))
x2 = float(input('Segunda nota: '))

media = (x1+x2) / 2

print(f'Tirando a nota {x1:.1f} e {x2:.1f}, a média do aluno é {media:.1f}')

if media >= 7:
    print('O aluno está aprovado!')
elif 5 <= media <= 6.9:
    print('O aluno está de recuperação.')
elif media <= 5:
    print('O aluno está reprovado.')