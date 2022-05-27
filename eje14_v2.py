def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))

from urllib import request
from urllib.error import URLError

url=input("Escribe una URL")
try:
        f = request.urlopen(url)
except URLError:
        print("¡La url " + url + "no existe!")
    else:
        contenido = f.read()
        print( len(contenido.split()))

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))