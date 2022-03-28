print('\033[1;32m Exercício 114 - Link acessível?')
import urllib


from urllib import request, response, error

try:
    web = request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('Site inacessível')
else:
    print('Site está acessível')

