print('\033[1;32m Exercício 92 Jogo de dados')
from random import randint
from time import sleep
from operator import itemgetter
dict = {}
lista = []
for x in range (0,4):
    dict[f'jogador{x+1}'] = randint(1,6)
for k, v in dict.items():
    print(f'O {k} tirou nos dados {v}')
    sleep(0.5)
ranking = {}
ranking = sorted(dict.items(), key=itemgetter(1), reverse=True)
print('=-'*30)
print('RANKING DOS DADOS')
cont = 1
for k, v in ranking:
    print(f'O {k} ficou em {cont}ª lugar e seu número no dado foi o {v}')
    cont +=1
