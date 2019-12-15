from silabas import Silabeador

def frasePi(palabras):
    frasePi = ''
    piLenguaje = ''

    for item in palabras:
        silabas = Silabeador().silabeo(item)
        palabraPi = []
        for silaba in silabas:
            silabaPi = 'pi' + silaba
            palabraPi.append(silabaPi)
        piLenguaje += frasePi.join(palabraPi) + ' '

    return piLenguaje

def fraseSinPi(palabrasPi):

    frase = ''
    fraseOrig = ''
    print(palabrasPi)
    for item in palabrasPi:
        palabra = item[2:]
        silabas = Silabeador().silabeo(palabra)
        indice = 1
        while indice < len(silabas):
            if len(silabas[indice]) == 2:
                silabas[indice] = ''
                indice += 2
            else:
                silabas[indice] = silabas[indice][2:]
                indice +=1

        fraseOrig += frase.join(silabas) + ' '

    return fraseOrig

if __name__ == '__main__':
    fraseInput = input('Introduzca una frase para traducir a pilenguaje: ')
    palabras = fraseInput.split(' ')
    piLenguaje = frasePi(palabras)
    palabrasPi = piLenguaje.split(' ')
    fraseOriginal = fraseSinPi(palabrasPi)
    print('\nLa frase original es: {}'.format(fraseInput))
    print('La frase en formato piLenguaje es: {}'.format(piLenguaje))
    print('Al convertir obtenemos de nuevo la frase original: {}'.format(fraseOriginal))
