entrada = [4,5,6,7]

class Subconjuntos:
    def __init__(self, lista):
        self.salida = []
        self.entry = lista

    def calcular(self):
        self.temp = []
        if not self.entry:
            return False
        self.salida.append(list())
        self.salida.append(self.entry)
        self.i = 0
        lon = len(self.entry)
        for number in self.entry:
            for num2 in self.entry[self.entry.index(number)+1:]:
                self.temp.append(num2)
            self.salida.append(self.temp)
            self.temp = []
        return self.salida

x = Subconjuntos(entrada)
print(x.calcular())
