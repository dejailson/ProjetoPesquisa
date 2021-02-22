import os
import config.Parametro as param

class GerenciadorRecurso:
    def __init__(self):
        pass
    
    def carregarIconeLapis(self):
        icon_lapis = os.path.join(param.SUBPASTA_ICONE,param.ICONE_LAPIS)
        return os.path.abspath(self.montarCaminhoRecurso(icon_lapis))

    def carregarIconeOlho(self):
        icon_olho = os.path.join(param.SUBPASTA_ICONE,param.ICONE_OLHO)
        return os.path.abspath(self.montarCaminhoRecurso(icon_olho))
    
    def carregarIconeLixeira(self):
        icon_lixeira = os.path.join(param.SUBPASTA_ICONE,param.ICONE_LIXEIRA)
        return os.path.abspath(self.montarCaminhoRecurso(icon_lixeira))

    def carregarImagemFundo(self):
        imagem_fundo = os.path.join(param.SUBPASTA_FUNDO,param.IMAGEM_FUNDO)
        return os.path.abspath(self.montarCaminhoRecurso(imagem_fundo))

    def montarCaminhoRecurso(self,recurso):
        return os.path.join(param.PASTA_RECURSO,param.PASTA_IMAGEM,recurso)