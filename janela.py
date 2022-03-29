#from tkinter import *
import tkinter

class Janela:
    def __init__(self, raiz):
        self.fr1 = tkinter.Frame(raiz)
        #cada componente criado deve ser empacotado no método pack()
        self.fr1.pack()

        #cria um label
        self.lb1 = tkinter.Label(self.fr1, text = 'Olá Mundo!', background = 'gray',
                                 font = ('verdana', 20, 'bold', 'italic'), width = '10', height = 3)
        self.lb1.pack(side='left')

        self.fr2 = tkinter.Frame(raiz)
        self.fr2.pack()
        #cria um botão
        self.bt1 = tkinter.Button(self.fr2, text = 'Clique Aqui', background = 'gray',
                                 font = ('verdana', 20, 'bold', 'italic'), command = self.muda_label)
        self.bt1.bind('<Return>', self.muda_label2)
        self.bt1.pack(side='left')

        self.lb2 = tkinter.Label(self.fr1, text='', width=55)
        self.lb2.pack()

        self.lb2 = tkinter.Label(self.fr2, text='', width=55)
        self.lb2.pack()

    def muda_label(self):
        self.lb1['text'] = 'Deu certo!'

    def muda_label2(self, event):
        self.lb1['text'] = 'Deu certo2'


#Cria uma instância de janela
raiz = tkinter.Tk()
Janela(raiz)

#Define a largura da janela "raiz" (600 = largura, 400 = altura, 400 = posicionamento x, 100 = posicionamento y)
raiz.geometry('600x400+400+100')
raiz.mainloop()