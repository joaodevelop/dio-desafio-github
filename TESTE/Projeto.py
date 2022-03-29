## MÓDULO COM FUNÇÕES ÚTEIS AO PROJETO DO CURSO DO PROF. GUANABARA
def verde(msg):
    print(f'\033[1;32m{msg}')

def vermelho(msg):
    print(f'\033[1;31m{msg}')

def azul(msg):
    print(f'\033[1;34m{msg}')


def amarelo(msg):
    print(f'\033[1;33m{msg}')


def reverte(msg):
    print(f'\033[0;0m{msg}')

def linha():
    print('='*42)


def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Você não digitou um número inteiro!')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mVocê não digitou nada!')
            return 0
        else:
            return n1


def titulo(msg):
    reverte('='*42)
    verde(f'{msg}'.center(42))
    reverte('='*42)

def menu(lista):
    titulo("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f'\033[1;33m{c} - \033[1;34m{item}')
        c += 1
    print('\033[0;0m='*42)
    opc = leiaInt('\033[1;32mSua Opção: ')
    return opc


def lerarquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro na leitura do arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        for dado in arquivo:
            linha = dado.split(';')
            linha[1] = linha[1].replace('\n', '')
            print(f'\033[1;34m{linha[0]:<30} {linha[1]:>3} anos')

    finally:
        arquivo.close()

def cadastrar(arquivo, nome ='desconhecido', idade =0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro na leitura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na escrita do arquivo.')
        else:
            titulo('PESSOA CADASTRADA COM SUCESSO!')


def criararquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')

def arquivoexiste(arquivo):
    try:
        open(arquivo, 'r')
        return True
    except:
        print('Erro na abertura do arquivo')
        return False