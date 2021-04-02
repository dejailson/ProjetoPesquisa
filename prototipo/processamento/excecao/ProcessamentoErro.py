class ProcessamentoErro(Exception):
    def __init__(self, *args, **kwargs):
        super(ProcessamentoErro, self).__init__(args, kwargs)
