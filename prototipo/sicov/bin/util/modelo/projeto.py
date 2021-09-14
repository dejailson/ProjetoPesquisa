class Projeto:
    bd = None
    def __init__(self, nome, data, descricao, pesquisadores, coordenador):
        self.nome = nome #Identificação
        self.data = data
        self.descricao = descricao
        self.pesquisadores = pesquisadores
        self.coordenador = coordenador
        self.amostras = []

    def setAmostra(self, amostra):
        self.amostras.append(amostra)

            
