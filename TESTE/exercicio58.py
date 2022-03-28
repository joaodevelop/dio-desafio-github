print('\033[1;32mExercício 58 Jogo da advinhação')
print('Pensei em um número de 1 a 10')
print('Você consegue acertar qual foi?')
from random import randint
num = randint(1,10)
choice = 0
cont = 1
while choice != num:
    choice = int(input('Qual número você escolhe?: '))
    if choice == num:
        print(f'Parabens, você acertou! {num} foi o número escolhido!')
    else:
        print('Não, ainda não é este número que eu pensei')
        cont += 1
print(f'Você precisou de {cont} tentativas para advinhar o número!')