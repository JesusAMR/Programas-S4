entrada =   "()[]{}()"

class ValidarParentesis:
    def __init__(self, inp):
        self.validos =   { "(":")", "{":"}", "[":"]" }
        self.i = 0
        self.lon = len(inp)
        self.entry = inp

    def valido(self):
        valido =  True
        while(self.i < self.lon):
            if self.entry[self.i] not in self.validos:
                return False
            caracterBuscar = self.validos[self.entry[self.i]]
            if caracterBuscar == self.entry[self.i+1]:
                valido = valido and True
                self.i = self.i + 1
            else:
                valido = valido and False
            self.i = self.i + 1
        return valido

x = ValidarParentesis(entrada)
if(x.valido()):
    print "Cadena Valida!"
else:
    print "Cadena Invalida!"

