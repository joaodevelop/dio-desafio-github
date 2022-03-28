print('\033[1;32m Exercício 93 Jogador de futebol')
dict = {}
dict['Nome'] = str(input('Nome do jogador: '))
lista = []
cont = total = 0
partidas = int(input('Quantas partidas ele jogou no campeonato?:  '))
for c in range (0, partidas):
    gols = int(input(f'Quantos gols ele marcou na partida {c+1}? '))
    lista.append(gols)
    cont +=1
dict['Gols'] = lista[:]
dict['Total'] = cont
print('*='*30)
print(f'O jogador {dict["Nome"]} jogou {dict["Total"]} partidas')
for k in range (0,partidas):
    print(f'Na partida {k} ele fez {lista[k]} gols')
    total += lista[k]
print(f'Ele marcou um total de {total} gols')


