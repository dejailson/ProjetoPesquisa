from reportlab.pdfgen import canvas
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from util.modelo.camarao import Camarao


class SalvarPDF:
    def __init__(self, amostra, camarao, listaOvos):
        self.recurso = gr()
        self.listaOvos = listaOvos
        self.nome = str(amostra.identificacao+'_'+amostra.nomeProjeto+'.pdf')
        self.caminho = self.recurso.montarCaminhoPDF(self.nome)
        self.camarao = Camarao(amostra.CCT, amostra.CA, amostra.T, self.listaOvos)
        self.mediaMassaOvos, self.volumeMassaOvos = self.camarao.volumeDaMassaDosOvos()
        self.mediaMassaOvos = str(self.mediaMassaOvos).split('.')
        self.mediaMassaOvos = self.mediaMassaOvos[0] + '.' + self.mediaMassaOvos[1][:2]


        self.volumeMassaOvos = str(self.volumeMassaOvos).split('.')
        self.volumeMassaOvos = self.volumeMassaOvos[0] + '.' + self.volumeMassaOvos[1][:2]

        self.MediaFecundidade = str(self.camarao.MediaFecundidade).split('.')
        self.MediaFecundidade = self.MediaFecundidade[0] + '.' + self.MediaFecundidade[1][:2]

    def salvar(self):
        cnv = canvas.Canvas(self.caminho)
        cnv.drawString(210,750,"Relatório da amostra "+ self.nome)
        
        cnv.drawString(80,700,"Média da Massa dos Ovos")
        cnv.drawString(100,685,self.mediaMassaOvos+"mm³")

        cnv.drawString(230,700,"Volume da Massa dos Ovos")
        cnv.drawString(250,685,self.volumeMassaOvos+"mm³")


        cnv.drawString(400,700,"Média de Fecundidade")
        cnv.drawString(400,685,self.MediaFecundidade+" ovo/tamanho")

        cnv.drawString(230,670,"Total de Ovos")
        cnv.drawString(270,655,str(len(self.listaOvos)))

        cnv.drawString(80,635,"Diametro Maior")
        cnv.drawString(230,635,"Diametro Menor")
        cnv.drawString(380,635,"Volume do Ovo")
        coordenadarInicial = 620
        cont = 0
        verificador = 0
        for egge in self.listaOvos:
            cnv.drawString(80,(coordenadarInicial-cont),str(egge.diametroMaior)[:4]+"mm³")
            cnv.drawString(230,(coordenadarInicial-cont),str(egge.diametroMenor)[:4]+"mm³")
            cnv.drawString(380,(coordenadarInicial-cont),str(egge.calcularVolume())[:4]+'mm³')
            cont += 15
            verificador += 1
            if verificador == 36:
                cont = 0
                verificador = 0
                coordenadarInicial = 750
                cnv.showPage()
        cnv.save()
        return self.nome
