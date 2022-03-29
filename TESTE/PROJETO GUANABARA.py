import Projeto
from Projeto import menu
from Projeto import *
## MENU DE CADASTRAMENTO EM PYTHON! EXERCÍCIO 115 - PROJETO FINAL DO CURSO!

pessoas = []
if not arquivoexiste('cadastro.txt'):
    criararquivo('cadastro.txt')
while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do Sistema'])
    if escolha == 1:
        lerarquivo('cadastro.txt')
    elif escolha == 2:
        titulo("\033[1;34mOPÇÃO 2 - Cadastrar pessoas")
        nome = str(input('Qual o nome da pessoa?: '))
        idade = leiaInt('Qual a idade da pessoa?: ')
        cadastrar('cadastro.txt', nome, idade)
    elif escolha == 3:
        linha()
        print('\033[1;34mSaindo do sistema...Até logo!')
        linha()
        break
    else:
        print('\033[1;31mERRO! Você deve digitar uma das opções 1, 2 ou 3!')

