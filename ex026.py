frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('A')+1))

