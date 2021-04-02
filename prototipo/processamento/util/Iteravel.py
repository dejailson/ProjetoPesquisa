class Iteravel:
    def __init__(self):
        self.__itens = list()
        self.__colecao = dict()

    def adicionarRecurso(self, chave, valor):
        self.__colecao.update({chave: valor})

    def adicionarItem(self, item):
        if (not self.existeItem(item)):
            self.__itens.append(item)

    def obterValor(self, chave):
        if(self.existeChave(chave)):
            return self.__colecao.get(chave)
        else:
            raise KeyError('Iteravel.obterRecurso',
                           f'Não existe chave com o nome {chave}')

    def existeChave(self, chave):
        return self.__colecao.__contains__(chave)

    def existeItem(self, item):
        return self.__itens.__contains__(item)

    def obterItens(self):
        return self.__itens

    def obterItem(self, posicao):
        return self.__itens[posicao]
