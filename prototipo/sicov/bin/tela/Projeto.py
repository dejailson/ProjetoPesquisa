import tkinter as t
from tkinter import messagebox
import config.Parametro as param
from tkinter import ttk
from tela.CadastrarProjeto import cadastrarProjeto as CP
from util.binario import Dados as dd
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from util.Search import Search
from tela.visu_Projeto import cadastrarProjeto
from PIL import ImageTk
from PIL import Image
import shelve
import re
from config.Parametro import BANCO_DADOS, SUBPASTA_IMGS_AMOSTRAS

class Projeto():
    def __init__(self):
        self.recurso = gr()

        self.pro = t.Tk()
        try:
            self.pro.iconbitmap(self.recurso.carregarIconeJanela())
        except:
            pass
        self.pro.geometry("700x500")
        self.pro.resizable(0, 0) 
        self.w1 = t.LabelFrame(self.pro)
        self.w2 = t.LabelFrame(self.pro)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=5)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=5)
        self.pro.title('Projeto')

        self.msg1 = t.Label(self.pro, text='Filtros', font=param.FONTE_OUTRA[0])
        self.msg1.place(x=30, y=0)
        self.msg2 = t.Label(self.pro, text='Nome   ', font=param.FONTE_OUTRA[3])
        self.msg2.place(x=12, y=50)
        self.Nome = t.Entry(self.pro, width=50, bord=2)
        self.Nome.place(x=160, y=55, height=30)
        self.msg3 = t.Label(self.pro, text='Data', font=param.FONTE_OUTRA[3])
        self.msg3.place(x=465, y=55)
        self.Data = self.MaskedWidget(self.pro, 'fixed', mask='99/99/9999')
        self.Data.insert(0, '14082021')
        self.Data.place(x=520, y=60)
        #self.Data.place(x=520, y=55, height=30)
        self.msg4 = t.Label(self.pro, text='Coordenador     ', font=param.FONTE_OUTRA[2])
        self.msg4.place(x=12, y=150)
        self.coordenador = t.Entry(self.pro, width=50, bord=2)
        self.coordenador.place(x=160, y=150, height=30)

        self.botao_pesquisar = t.Button(self.pro, text=' Pesquisar ', font=param.FONTE_PADRAO, command=lambda: self.search())
        self.botao_pesquisar.place(x=540, y=150)#sem ação
        self.botao_adicionar = t.Button(self.pro, text='Cadastrar Projeto', font=param.FONTE_OUTRA[1],  
                                        command=lambda : self.mudarTela())
        self.botao_adicionar.place(x=580, y=265)
        
        self.tree = ttk.Treeview(self.pro, selectmode="browse", 
                                column=("coluna1", "coluna2", "coluna3", "coluna4"),
                                show="headings")
        self.tree.column("coluna1", width=100, minwidth=50)
        self.tree.heading('#1', text=' ')
        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Projeto')
        self.tree.column("coluna3", width=50, minwidth=50)
        self.tree.heading('#3', text='Data')
        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')

        self.visu()

        self.tree.place(x=15, y=300, height = 115, width=540)

        self.visualizarAmo = t.Button(self.pro, text='Visualizar Todos os Projetos', 
                                font='arial 10 bold', 
                                command=lambda:self.visu())
        self.visualizarAmo.place(x=20, y=450)

        self.button2 = t.Button(self.pro, text='Voltar', 
                                command=lambda:self.mudarTela(var=1))
        self.button2.place(x=570, y=450, width=100)
        

        self.caminho_lapis = self.recurso.carregarIconeLapis()
        self.img_lapis = Image.open(self.caminho_lapis)
        self.resu = self.red(self.img_lapis)
        self.imagem_lapis = ImageTk.PhotoImage(self.resu)
        self.imagem_lapis_L = t.Button(image=self.imagem_lapis, command=lambda: self.editar()).place(x=570, y=315)

        self.caminho_olhos = self.recurso.carregarIconeOlho()
        self.img_olhos = Image.open(self.caminho_olhos)
        self.resu = self.red(self.img_olhos)
        self.imagem_olhos = ImageTk.PhotoImage(self.resu)
        self.imagem_olhos_L = t.Button(image=self.imagem_olhos, command=lambda: self.viewProjeto()).place(x=610, y=315)

        self.caminho_lixeira = self.recurso.carregarIconeLixeira()
        self.img_lixeira = Image.open(self.caminho_lixeira)
        self.resu = self.red(self.img_lixeira)
        self.imagem_lixeira = ImageTk.PhotoImage(self.resu)
        self.imagem_lixeira_L = t.Button(image=self.imagem_lixeira, command=lambda: self.remover()).place(x=650, y=315)

        self.pro.mainloop()

    def editar(self):
        if self.tree.selection() == ():
            messagebox.showwarning("Erro!","Selecione um Projeto!")
        else:
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            posicao = self.tree.selection()[0]
            posicao = self.tree.get_children().index(posicao)
            projeto = self.lista[posicao]
            self.dados.close()
            from tela.CadastrarProjeto import cadastrarProjeto
            self.pro.destroy()
            cadastrarProjeto(projeto=projeto)

    def red(self, imge):
        self.basewidth = 25
        self.wpercent = (self.basewidth/float(imge.size[0]))
        self.hsize = int((float(imge.size[1])*float(self.wpercent)))
        imge = imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        return imge


    def mudarTela(self, var=None):
        self.pro.destroy()
        if var == None:
            CP()
        else:
            from tela.TelaPrincipal import TelaPrincipal
            TelaPrincipal()


    def viewProjeto(self):
        if self.tree.selection() == ():
            messagebox.showwarning("Erro!","Selecione um Projeto!")
        else:
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            posicao = self.tree.selection()[0]
            posicao = self.tree.get_children().index(posicao)
            projeto = self.lista[posicao]
            self.dados.close()
            cadastrarProjeto(lista=projeto)

    def remover(self):
        if self.tree.selection() == ():
            messagebox.showwarning("Erro!","Selecione um Projeto!")
        else:
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            posicao = self.tree.selection()[0]
            posicao = self.tree.get_children().index(posicao)
            projeto = self.lista[posicao]
            for amostra in projeto.amostras:
                caminho = self.recurso.montarCaminhoImagem(amostra.identificacao +'_'+ projeto.nome  +'.png')
                try:
                    self.recurso.excluirImagem(caminho)
                except:
                    pass
            self.lista.remove(self.lista[posicao])
            posicao = self.tree.selection()[0]
            self.tree.delete(posicao)
            self.dados['Projeto'] = self.lista
            self.dados.close()

    def search(self):
        self.lista = [self.Nome.get().strip(), self.Data.get().strip(), self.coordenador.get().strip()]
        self.visu(lista=Search(projeto=self.lista))


    def visu(self, lista=None):
        posicao = self.tree.get_children()
        for c in range(len(posicao)):
            self.tree.delete(posicao[c])
        if lista == None:
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            self.cont = 1
            for c in self.lista:
                self.list = [self.cont]
                self.list.append(c.nome)
                self.list.append(c.data)
                self.list.append(c.coordenador.nome)
                self.tree.insert("", 'end',values=self.list,  tag='1')
                self.cont += 1
            self.dados.close()
        else:
            cont = 0
            if len(lista) > 0:
                for c in lista:
                    cont += 1
                    lista1 = [cont, c.nome, c.data, c.coordenador.nome]
                    self.tree.insert("", 'end',values=lista1,  tag='1')




    class MaskedWidget(ttk.Entry):
        def __init__(self, master, format_type, **kw):
            definitions = {
                '9': '[0-9]',
                'a': '[a-zA-Z]',
                'x': '[a-zA-z0-9]'
                }
            self.fields = {
                'type': format_type,
                'mask': None,
                'monetary': False,
                'dec_places': 2,
                'dec_sep': '.',
                'tho_places': 3,
                'tho_sep': ',',
                'symbol': '',
                'fmt_neg': '-%(symbol)s%(amount)s',
                'fmt_pos': '%(symbol)s%(amount)s',
                'placeholder': '_',
                'textvariable': None,
            }

            if str(format_type).lower() == 'fixed':
                assert 'mask' in kw, 'the fixed mask, is not present'

            self.fields['mask'] = kw.pop('mask', '').lower()
            for k in list(kw.keys()):
                if k in self.fields:
                    if k!='textvariable':
                        self.fields[k]=kw.pop(k)
                    else:
                        self.fields[k]=kw[k]
            if not 'textvariable' in kw:
                self.fields['textvariable']=t.StringVar(master)
                kw['textvariable'] = self.fields['textvariable']
            ttk.Entry.__init__(self, master, **kw)

            self.defs = definitions
            self.tests = []
            self.partialPosition = None
            self.firstNonMaskPosition = None
            self.len = len(self.fields['mask'])
            for i,c in enumerate(self.fields['mask'].lower()):
                if c == '?':
                    self.len -= 1
                    self.partialPosition = i
                atom = self.defs.get(c, None)
                self.tests.append(re.compile(f'{atom}') if atom else atom)
                if not atom and self.firstNonMaskPosition==None:
                    self.firstNonMaskPosition = len(self.tests)-1

            self.writeBuffer()

            if str(self.cget("state")).upper()!="DISABLED":
                self.bind('<KeyPress>', self._onKeyPress, True)
                self.bind('<KeyRelease>', lambda e: 'break', True)
                self.bind('<FocusIn>', self._onFocusIn, True)

        def writeBuffer(self):
            self.fields['textvariable'].set(
                ''.join(
                    filter(
                        lambda x: x!=None,
                            map(
                                lambda c, self=self:
                                    (self.fields['placeholder']
                                    if self.defs.get(c, None)
                            else c)
                        if c!='?' else None, self.fields['mask'])
                    )
                )
            )
            return self.get()
        def clean(self):
            self.fields['textvariable'].set('')
            self.writeBuffer()

        def clean_numeric(self, string):
            if not isinstance(string, basestring): string = str(string)
            string = string.replace(self.fields['symbol']+' ', '')\
                        .replace(self.fields['tho_sep'], '')\
                        .replace(self.fields['dec_sep'], '.')
            if not '.' in string:
                string = list(string)
                string.insert(-2, '.')
                string = ''.join(string)
            return string.partition('.')

        def fmt_numeric( self, amount):
            temp = '00' if not '.' in str(amount) \
                        else str(amount).split('.')[1]
            l = []
            amount = amount.split('.')[0]
            try:
                minus = float(''.join(self.clean_numeric(amount)))<0
            except ValueError:
                minus = 0
            if len(amount)> self.fields['tho_places']:
                nn = amount[-self.fields['tho_places']:]
                l.append(nn)
                amount = amount[:len(amount)-self.fields['tho_places']]
                while len(amount) > self.fields['tho_places']:
                    nn = amount[len(amount)-self.fields['tho_places']:]
                    l.insert(0, nn)
                    amount = amount[0:len(amount)-self.fields['tho_places']]

            if len(''.join(self.clean_numeric(amount)))>0: l.insert(0, amount)
            amount = self.fields['tho_sep'].join(l)+self.fields['dec_sep']+temp
            if minus:
                amount = self.fields['fmt_neg']%{
                    'symbol':self.fields['symbol'],
                    'amount': amount
                }
            else:
                amount = self.fields['fmt_pos']%{
                    'symbol': (self.fields['symbol']+' ') if self.fields['symbol'] else '',
                    'amount': amount
                }
            return amount

        def seekNext(self, pos):
            if 0 <= pos+1<self.len:
                if self.tests[pos+1]:
                    return pos+1
                return self.seekNext(pos+1)
            return pos

        def seekPrev(self, pos):
            if 0 <= pos-1 < self.len:
                if self.tests[pos-1]:
                    return pos-1
                return self.seekPrev(pos-1)
            return pos

        def shiftL(self, begin, end):
            if begin < 0: return
            for i in range(self.len):
                j = self.seekNext(begin)
                if self.tests[i]:
                    if j < self.len and self.tests[i].match(self.buffer[i]):
                        self.buffer[i] = self.buffer[j]
                        self.buffer[j] = self.fields['placeholder']
                    else:
                        break

        def shiftR(self, pos, c):
            if pos in range(len(self.len)):
                j = self.seekNext(pos)
                t = self.buffer[pos]
                if not t == c and j < self.len and t == self.fields['placeholder']:
                    self.buffer[pos] = c

        def writeBuffer(self):
            self.fields['textvariable'].set(
                ''.join(
                    filter(
                        lambda x: x!=None,
                            map(
                                lambda c, self=self:
                                    (self.fields['placeholder']
                                    if self.defs.get(c, None)
                            else c)
                        if c!='?' else None, self.fields['mask'])
                    )
                )
            )
            return self.get()

        def _onFocusIn(self, event):
            if self.len>0 and self.tests[0]:
                self.icursor(0)
            else:
                self.icursor(self.seekNext(0))

        def _onKeyPress(self, event):
            if event.keysym == 'Tab':
                return
            elif event.keysym == 'Escape':
                if self.fields['type'] == 'fixed':
                    self.writeBuffer()
                else:
                    self.delete(0, len(event.widget.get()))
            widget = event.widget
            val = widget.get()
            idx = widget.index(t.INSERT)

            if event.keysym == 'Left':
                if 0 <= idx < self.len:
                    if idx < self.firstNonMaskPosition:
                        return 'break'
                    elif not self.tests[idx]:
                        widget.icursor(self.seekPrev(idx))
            elif event.keysym == 'Right':
                if 0 <= idx < self.len:
                    if idx >= self.len:
                        return 'break'
                    elif not self.tests[idx]:
                        widget.icursor(self.seekNext(idx))
            elif event.keysym == 'BackSpace' and self.fields['type'] != 'numeric':
                def repl_or_stop(cls, wget, pos):            
                    if 0 <= pos <= cls.len:
                        if not cls.tests[pos]:
                            pos = cls.seekPrev(pos)
                        cls._write_char(pos, cls.fields['placeholder'], -1)
                    return 'break'
                repl_or_stop(self, widget, idx - 1)
                return 'break'
            else:
                if self.fields['type'] == 'fixed':
                    if self._write_char(idx, event.char) == 'break':
                        return 'break'
                elif self.fields['type'] == 'numeric' and event.char.isdigit():
                    if val:
                        widget.delete(0, len(val))
                        head, sep, tail = self.clean_numeric(val)
                    else:
                        head, sep, tail = '0', '.', '00'

                    if not head:
                        head = '0'
                    if len(tail) < 2:
                        tail = '0' + tail

                    if tail and len(tail + event.char) <= 2 and (int(tail+event.char))<99:
                        tail = tail[1:] + event.char
                    else:
                        if not int(head):
                            head = tail[0] if tail else '0'
                        else:
                            head += tail[0]
                        tail = tail[1:] + event.char
                        widget.insert(0, ''.join([head, sep, tail]))
                    return 'break'
                elif self.fields['type'] == 'numeric' and event.keysym == 'BackSpace':
                    if val:
                        widget.delete(0, len(val))
                        head, sep, tail = self.clean_numeric(val[:-1])
                    else:
                        head, sep, tail = '0', '.', '00'
                    widget.insert(0, ''.join([head, sep, tail]))
                    return 'break'
                else:
                    self.bell()
                    return 'break'

        def insert(self, index, value):
            if self.fields['type']=='numeric':
                ttk.Entry.insert(self, index, self.fmt_numeric(value))
            else:
                for c in str(value):
                    while (not self.tests[index] or not self.tests[index].match(c)):
                        index += 1
                    self._write_char(index,c)
                    index += 1

        def _write_char(self, idx, char, direction=+1):
            if 0<=idx<self.len and self.tests[idx]:
                if char != self.fields['placeholder'] and not self.tests[idx].match(char):
                    self.bell()
                    return 'break'
                self.delete(idx)
                ttk.Entry.insert(self, idx, char)
                if direction == +1:
                    if idx + 1 < self.len and not self.tests[idx+1]:
                        idx = self.seekNext(idx)
                    else:
                        idx += 1
                elif direction == -1 and \
                    idx - 1 >= 0 and \
                    not self.tests[idx]:
                    idx = self.seekPrev(idx)
                self.icursor(idx)
                return 'break'
            else:
                self.bell()
                return 'break'


    def get_calendar(locale, fwday):
        # instantiate proper calendar class
        if locale is None:
            return calendar.TextCalendar(fwday)
        else:
            return calendar.LocaleTextCalendar(fwday, locale)
        
        
                

