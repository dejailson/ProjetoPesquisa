class Camarao:
    def __init__(self, CCT, CA, T, Ovos):
        self.ComprimentoTotal = CCT + CA + T
        self.Ovos = Ovos
        self.MediaFecundidade = len(self.Ovos) / self.ComprimentoTotal
    
    def volumeDaMassaDosOvos(self):
        self.mediaVolumeOvos = 0
        for ovo in self.Ovos:
            self.mediaVolumeOvos += ovo.calcularVolume()
        self.mediaVolumeOvos /= len(self.Ovos)
        self.volumeMassaOvos = self.MediaFecundidade * self.mediaVolumeOvos
        return self.mediaVolumeOvos, self.volumeMassaOvos

