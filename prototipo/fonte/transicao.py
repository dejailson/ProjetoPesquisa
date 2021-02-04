from Projeto import Projeto
from CadastrarProjeto import cadastrarProjeto
from Amostras import Amostras
from cadastrarAmostra import CadastrarAmostra
from Relatorio_do_Processamento import Relatorio

class Transicao:
    def __init__(self, n=None):
        if n==1:
            Projeto()
        elif n ==2:
            cadastrarProjeto()
        elif n ==3:
            Amostras()
        elif n ==4:
            CadastrarAmostra()
        elif n ==5:
            Relatorio()
        elif n==6:
            from main import Main

