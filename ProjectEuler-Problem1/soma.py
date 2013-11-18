import sys

class Somar:
    soma = 0
    limite = 0
    numero = 0

    def calcularSoma(self,):
        self.numero = self.numero + 1
        if self.numero == self.limite:
            return self.soma
        if self.numero % 3 == 0 or self.numero % 5 == 0:
            self.soma = self.soma + self.numero
        return self.calcularSoma()

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    teste = Somar()
    teste.limite = 1000
    print teste.calcularSoma()