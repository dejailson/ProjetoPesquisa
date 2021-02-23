import os
import config.Parametro as param


class GerenciadorRecurso:
    DIRETORIO_RAIZ = os.path.realpath('..')

    def __init__(self):
        pass

    def carregarIconeLapis(self):
        icon_lapis = os.path.join(param.SUBPASTA_ICONE, param.ICONE_LAPIS)
        return self.montarCaminhoRecurso(icon_lapis)

    def carregarIconeOlho(self):
        icon_olho = os.path.join(param.SUBPASTA_ICONE, param.ICONE_OLHO)
        return self.montarCaminhoRecurso(icon_olho)

    def carregarIconeLixeira(self):
        icon_lixeira = os.path.join(param.SUBPASTA_ICONE, param.ICONE_LIXEIRA)
        return self.montarCaminhoRecurso(icon_lixeira)

    def carregarImagemFundo(self):
        imagem_fundo = os.path.join(param.SUBPASTA_FUNDO, param.IMAGEM_FUNDO)
        return self.montarCaminhoRecurso(imagem_fundo)

    def montarCaminhoRecurso(self, nomeRecurso):
        return os.path.join(self.DIRETORIO_RAIZ, param.PASTA_RECURSO,
                            param.PASTA_IMAGEM, nomeRecurso)
