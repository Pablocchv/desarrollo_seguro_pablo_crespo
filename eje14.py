#Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.
url=input("Escribe la url a buscar")
contar_palabras=url

#poner restrionesc cuando se pida la url

from urllib import request
from urllib.error import URLError
try:
    with request.urlopen(url) as f:
            contenido = f.read()
except URLError:
            print('¡La url ' + url + ' no existe!')
    else:
        print((len(contenido.split())

#print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))

#print(contar_palabras('https://github.com/kaonashi-passwords/Kaonashi/blob/master/LICENSE.txt'))

#'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?'

