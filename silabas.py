class Silabeador():

    def __init__(self):
        self.__consonantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
        self.__paresConson = ('bl','cl','fl','gl','kl','pl','tl','br','cr','dr','fr','gr','kr','pr','tr','ch','ll','rr')
        self.__vocAbiertas = ('a', 'e', 'o', 'á', 'é', 'ó', 'ú')
        self.__vocCerradas = ('i', 'u', 'ü')
        self.__vocales = self.__vocAbiertas + self.__vocCerradas
        self.__semiVocales = ('y')


    def silabeo(self, cad):
        grupo = ''
        grupoVocal = []
        silabas = []
        contador = 0
        prefijo = ''

        #Excepcion si la palabra comienza por in
        if cad[:2] == 'in':
            prefijo = 'in'
            cad = cad[2:]

        #Separamos la cadena en grupos de vocales
        for i in cad:
            if i in self.__vocales or i in self.__semiVocales:
                if i in self.__vocales:
                    grupo += i
                elif i in self.__semiVocales:
                    if cad.index(i) == len(cad)-1:
                        grupo += i
                    else:
                        grupo += ','
            elif i in self.__consonantes:
                grupo += ','

        listVocales = grupo.split(',')

        #Lista con los grupos vocales
        for j in listVocales:
            if j != '':
                grupoVocal.append(j)
            
        for item in grupoVocal:
            if len(item) == 2:
                if (item[0] in self.__vocCerradas and item[1] in self.__vocCerradas) or (item[0] in self.__vocAbiertas and item[1] in self.__vocCerradas) or (item[0] in self.__vocCerradas and item[1] in self.__vocAbiertas) or item[1] in self.__semiVocales:
                    pass
                else:
                    position = grupoVocal.index(item)
                    grupoVocal.pop(grupoVocal.index(item))
                    grupoVocal.insert(position,item[0])
                    grupoVocal.insert(position+1,item[1])
            elif len(item) == 3:
                if (item[0] in self.__vocCerradas and item[1] in self.__vocAbiertas and item[2] in self.__vocCerradas):
                    pass

        for k in grupoVocal:
            indice = cad.find(k)
            if indice == 0:
                silabas.append(k)
                contador += 1
            else:
                silaba = cad[indice-1]+k
                silabas.append(silaba)
                if cad[0:indice] in self.__paresConson:
                    silaba = cad[0:indice]+k
                    silabas.pop(contador)
                    silabas.append(silaba)
                elif len(cad[0:indice]) > 1:
                    silaba = silabas[contador-1] + cad[0]
                    silabas.pop(contador-1)
                    silabas.insert(contador-1, silaba)
                contador += 1
            cad = cad[indice+len(k):]
            
        if cad != '':
            lastSilaba = silabas[-1]
            newSilaba = lastSilaba + cad
            silabas.pop(-1)
            silabas.append(newSilaba)

        if prefijo == 'in':
            silabas.insert(0, prefijo)

        return silabas
