class Ovulo:
    def __init__(self, diametroMaior, diametroMenor, estagio ):
        self.diametroMaior = diametroMaior
        self.diametroMenor = diametroMenor
        self.estagio = estagio
    def calcularVolume(self):
        return (3.14 * self.diametroMaior * (self.diametroMenor**2)) / 6
    def macharOcular(self):
        pass