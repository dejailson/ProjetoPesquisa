class Pesquisador:
    def __init__(self, nome, matricula, tipoMembro, coordenador):
        self.nome = nome
        self.matricula = matricula
        self.tipoMembro = tipoMembro
        self.coordenador = coordenador
        self.listaAtributos = [nome, tipoMembro, coordenador, matricula]