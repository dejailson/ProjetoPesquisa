import abc
from .Iteravel import Iteravel


def processar(tarefas, recurso):
    for tarefa in tarefas:
        recurso = tarefa(recurso)
    return recurso


class ProcessadorTarefa (metaclass=abc.ABCMeta):

    def __init__(self):
        self.__iteravel = Iteravel()

    @abc.abstractmethod
    def executar(self):
        pass

    def _adicionarTarefa(self, tarefa):
        self.__iteravel.adicionarItem(tarefa)

    def _adicionarRecurso(self, chave, valor):
        self.__iteravel.adicionarRecurso(chave, valor)

    def _tarefas(self):
        return self.__iteravel.obterItens()

    def _recurso(self, chave):
        return self.__iteravel.obterValor(chave)

    def _existeRecurso(self, chave):
        return self.__iteravel.existeChave(chave)
