class Registro:
    def __init__(self, nomeMusica, ano, album, id):
        self._nomeMusica = nomeMusica
        self._ano = ano
        self._album = album
        self._id = id
        self._esquerda = None
        self._direita = None
        self._balanco = 0
        self._altura = 1

    def __str__(self):
        formatPrint = 'Nome da música: {0}\nId da música: {1}\nAlbum da música: {2}\nAno da música: {3}'
        return formatPrint.format(self._nomeMusica, self._id, self._album, self._ano)

    def printToStr(self, campo):
        if campo == 'nome':
            return self.printNome()
        elif campo == 'ano':
            return self.printAno()
        else:
            return self.printId()

    def printNome(self):
        return str(self._nomeMusica)

    def printId(self):
        return str(self._id)

    def printAno(self):
        return str(self._ano)