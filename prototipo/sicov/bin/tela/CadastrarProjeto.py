import tkinter as t
from tkinter import messagebox
from tkinter import ttk
from util.binario import Dados as dd
from util.modelo.projeto import Projeto
from util.modelo.pesquisador import Pesquisador
import config.Parametro as param 
from PIL import Image, ImageTk
import shelve
from time import sleep
from util.GerenciadorRecurso import GerenciadorRecurso as gr
import re
from config.Parametro import BANCO_DADOS


class cadastrarProjeto:
    def __init__(self, projeto=None):
        self.recurso = gr()
        self.projetoNone = projeto
        self.nomePadrao = ''
        self.dataPadrao = '10082021'
        self.descricaoPadrao = ''
        self.dados_membros = []
        if self.projetoNone != None:
            self.nomePadrao = self.projetoNone.nome
            self.dataPadrao = self.projetoNone.data.split('/')
            self.dataPadrao = self.dataPadrao[0] + self.dataPadrao[1] + self.dataPadrao[2]
            self.descricaoPadrao = self.projetoNone.descricao
            for c in projeto.pesquisadores:
                self.dados_membros.append(c)
        self.root = t.Tk()
        self.root.geometry("700x500")
        self.w1 = t.LabelFrame(self.root)
        self.w2 = t.LabelFrame(self.root)
        self.w1.pack(fill="both", expand="yes", padx=10, pady=10)
        self.w2.pack(fill="both", expand="yes", padx=10, pady=10)
        self.root.title('Cadastro de Projeto')
        
            
        
        self.validarSimNao = 0
        self.cont = 1

        self.msg1 = t.Label(self.root, text='Dados do Projeto',
                            font='arial 16 bold')
        self.msg1.place(x=12, y=20)

        self.msg2 = t.Label(self.root, text='Nome   ', font='arial 12 bold')
        self.msg2.place(x=12, y=50)
        self.nomeEntry = t.StringVar(self.root, value=self.nomePadrao)
        self.Nome = t.Entry(self.root, textvariable=self.nomeEntry, width=98, bord=2)
        self.Nome.place(x=90, y=55)
        self.msg3 = t.Label(self.root, text='Data     ', font='arial 12 bold')
        self.msg3.place(x=12, y=85)
        self.Data = self.MaskedWidget(self.root, 'fixed', width=45, mask='99/99/9999')
        self.Data.insert(0, self.dataPadrao)
        #self.Data = t.Entry(self.root, width=45, bord=2)
        self.Data.place(x=90, y=84)
        self.msg4 = t.Label(self.root, text='Descrição  ', font='arial 12 bold')
        self.msg4.place(x=12, y=120)
        self.Descricao = t.Text(self.root, width=83, height = 5, bord=2)
        self.Descricao.insert(t.END, self.descricaoPadrao)
        self.Descricao.place(x=15, y=150)
        self.msg5 = t.Label(self.root, text='EQUIPE', font='arial 16 bold')
        self.msg5.place(x=12, y=270)

        self.botao_adicionar = t.Button(self.root, text='+ Adicionar',
                                        font='arial 10 bold', 
                                        command=lambda : self.tela_Cad(x=1))
        self.botao_adicionar.place(x=600, y=265)

        self.tree = ttk.Treeview(self.root, selectmode="browse", 
                                column=("coluna1", "coluna2", "coluna3", "coluna4"), 
                                show="headings")
        self.tree.column("coluna1", width=50, minwidth=50)
        self.tree.heading('#1', text='Matrícula')
        self.tree.column("coluna2", width=150, minwidth=50)
        self.tree.heading('#2', text='Pesquisador')
        self.tree.column("coluna3", width=150, minwidth=50)
        self.tree.heading('#3', text='Membro')
        self.tree.column("coluna4", width=100, minwidth=50)
        self.tree.heading('#4', text='Coordenador')
        if self.projetoNone != None:
            self.visu()
        self.tree.place(x=15, y=300, height = 115, width=540)

        self.cancelarP = t.Button(self.root, text='Cancelar', 
                                font='arial 10 bold', 
                                command=lambda:self.mudarTela())
        self.cancelarP.place(x=20, y=450)
        self.salvarP = t.Button(self.root, text='Salvar', 
                                font='arial 10 bold', 
                                command=lambda:self.salvar())
        self.salvarP.place(x=620, y=450)

        self.caminho_lapis = self.recurso.carregarIconeLapis()
        self.img_lapis = Image.open(self.caminho_lapis)
        self.resu = self.red(self.img_lapis)
        self.imagem_lapis = ImageTk.PhotoImage(self.resu)
        self.imagem_lapis_L = t.Button(image=self.imagem_lapis, command= lambda: self.editarPesq()).place(x=570, y=315)

        self.caminho_lixeira = self.recurso.carregarIconeLixeira()
        self.img_lixeira = Image.open(self.caminho_lixeira)
        self.resu = self.red(self.img_lixeira)
        self.imagem_lixeira = ImageTk.PhotoImage(self.resu)
        self.imagem_lixeira_L = t.Button(image=self.imagem_lixeira, command=lambda: self.remover()).place(x=650, y=315)


        self.root.mainloop()

    def red(self, imge):
        self.basewidth = 25
        self.wpercent = (self.basewidth/float(imge.size[0]))
        self.hsize = int((float(imge.size[1])*float(self.wpercent)))
        imge = imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        return imge

    def tela_Cad(self, x=None):
        lista = ['', '']
        
        if self.projetoNone != None and x==None:
            posicao = self.tree.selection()[0]
            lista = [self.dados_membros[int(posicao[-1])-1].matricula, self.dados_membros[int(posicao[-1])-1].nome]
        self.tela = t.Tk()
        self.tela.geometry("400x300")
        self.tela.title('Cadastrar Participante')

        self.msgInicial = t.Label(self.tela, text='Cadastrar Participante', 
                                  font='arial 14 bold')
        self.msgInicial.place(x=100, y=10)

        self.mensagem1 = t.Label(self.tela, text='Matrícula', 
                                 font='arial 12 bold')
        self.mensagem1.place(x=12, y=50)

        self.matricula = t.Entry(self.tela, width=45, bord=2)
        self.matricula.insert(0, string=lista[0])
        self.matricula.place(x=120, y=50)

        self.mensagem2 = t.Label(self.tela, text='Pesquisador', 
                                 font='arial 12 bold')
        self.mensagem2.place(x=12, y=90)

        self.pesquisador = t.Entry(self.tela, width=45, bord=2)
        self.pesquisador.insert(0, string=lista[1])
        self.pesquisador.place(x=120, y=90)

        self.mensagem3 = t.Label(self.tela, text='Membro', font='arial 12 bold')
        self.mensagem3.place(x=12, y=130)

        self.membro = ttk.Combobox(self.tela, 
                                   values=['Bolsista', 'Orientador', 
                                           'Voluntário'],
                                    width=42)
        self.membro.place(x=120, y=130)
        self.membro.current(0)

        self.mensagem4 = t.Label(self.tela, text='Coordenador', 
                                 font='arial 12 bold')
        self.mensagem4.place(x=12, y=170)
        self.listSimNao = ['Sim', 'Não']
        if self.validarSimNao == 1:
            self.listSimNao = ['Não']
        self.coordenador = ttk.Combobox(self.tela, 
                                        values=self.listSimNao, width=42)
        self.coordenador.place(x=120, y=170)
        self.coordenador.current(0)

        self.butao1 = t.Button(self.tela, text="Salvar", font='arial 12 bold',
                               command=lambda: self.adicionar(x=x))
        self.butao1.place(x=100, y=250)
        self.butao2 = t.Button(self.tela, text="Cancelar", font='arial 12 bold', 
                               command=lambda: self.tela.destroy())
        self.butao2.place(x=200, y=250)

        self.tela.mainloop()

    def mudarTela(self, root=None):
        self.root.destroy()
        from tela.Projeto import Projeto as PJ
        PJ()

    def salvar(self):
        self.verCont = 0
        self.ver = [self.Nome.get().strip(), self.Data.get().strip(), self.Descricao.get(1.0, t.END).strip(), self.dados_membros]
        for i in self.ver:
            if i == '':
                self.verCont += 1

        self.projeto = Projeto(nome=self.Nome.get().strip(), 
                               data=self.Data.get().strip(), 
                               descricao=self.Descricao.get(1.0, t.END).strip(), 
                               pesquisadores=self.dados_membros)
         
        try: 
            self.dados = shelve.open(BANCO_DADOS)
            self.lista = self.dados['Projeto']
            if self.projetoNone == None:
                self.lista.append(self.projeto)
            else:
                for i in range(len(self.lista)):
                    if self.lista[i].nome == self.projetoNone.nome:
                        self.lista[i] = self.projeto
                        break
            self.dados['Projeto'] = self.lista
            self.dados.close()
        except:
            print('Erro!')
        self.mudarTela()

    def adicionar(self, x=None):
        self.Membro_Pesquisador = Pesquisador(nome=self.pesquisador.get().strip(), 
                                                matricula=self.matricula.get().strip(), 
                                                tipoMembro=self.membro.get().strip(), 
                                                coordenador=self.coordenador.get().strip())
        if x!=None:
            if self.Membro_Pesquisador.coordenador == 'Sim':
                self.validarSimNao = 1
            self.dados_membros.append(self.Membro_Pesquisador)
            self.lista = [self.Membro_Pesquisador.matricula, self.Membro_Pesquisador.nome, self.Membro_Pesquisador.tipoMembro, self.Membro_Pesquisador.coordenador]
            #self.lista.insert(0, self.cont)
            self.tree.insert("", 'end',values=self.lista,  tag='1')
            self.cont  += 1
        else:
            posicao = 0
            self.dados_membros[int(self.tree.selection()[0][-1])-1] = self.Membro_Pesquisador
            for c in range(len(self.tree.get_children())):
                self.tree.delete(self.tree.get_children()[0])
            self.visu()
        self.tela.destroy()

        

    def editarPesq(self):
        if self.tree.selection() == ():
            messagebox.showerror("Erro","Selecione um Membro!")
        else:
            posicao = self.tree.selection()[0]
            pesqui = self.dados_membros[int(posicao[-1])-1]
            self.tela_Cad()
    
    def remover(self):
        cont = 0
        if self.tree.selection() == ():
            messagebox.showerror("Erro","Selecione um Membro!")
        else:
            posicao = self.tree.selection()[0]
            self.dados_membros.remove(self.dados_membros[int(posicao[-1])-1])
            self.tree.delete(posicao)
        

        
        
    
    

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
        
        
    def visu(self):
        for i in self.dados_membros:
            lista = [i.matricula, i.nome, i.tipoMembro, i.coordenador]
            self.tree.insert("", 'end',values=lista,  tag='1')
            
