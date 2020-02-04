#!/usr/bin/env python3
#-*- econding: utf8 -*-

from tkinter import *
from tkinter import filedialog
import os.path 
import envio

class Application:
    def __init__(self, master=None):
        self.csv = None
        self.img = None
        self.text = None
        csv_name = None
        img_name = None

        self.fontePadrao = ("Times New Roman", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.testeContariner = Frame(master)
        self.testeContariner["padx"] = 20
        self.testeContariner.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados para serem enviados!")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Mensagem", font=self.fontePadrao)
        self.nomeLabel.pack(side=TOP)
  
        #self.nome = Entry(self.segundoContainer)
        self.nome = Text(self.segundoContainer, width=100, height=10) 
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.csv = Button(self.terceiroContainer)
        self.csv["text"] = "Anexar numeros"
        self.csv["width"] = 30
        self.csv["font"] = self.fontePadrao
        self.csv["command"] = self.pega_csv
        self.csv.pack(side=TOP)

        self.csv_resposta = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.csv_resposta.pack()
  
        #self.img = Entry(self.testeContariner)
        self.img = Button(self.testeContariner)
        self.img["text"] = "Anexar imagem"
        self.img["width"] = 30
        self.img["font"] = self.fontePadrao
        self.img["command"] = self.pega_img
        self.img.pack(side=TOP)

        self.img_resposta = Label(self.testeContariner, text="", font=self.fontePadrao)  
        self.img_resposta.pack(side=BOTTOM)
  
        self.autenticar = Button(self.quartoContainer, width=10, height=2 )
        self.autenticar["text"] = "Disparar"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["command"] = self.disparar
        self.autenticar.pack()
  
    def pega_csv(self):
        self.csv = filedialog.askopenfilename(initialdir = "/",title = "Selecione o arquivo",filetypes = (("Arquivos separado por por ponto e virgula",".csv"),(" Arquivos jpeg",".jpg")))
        csv_name = os.path.basename(self.csv)
        self.csv_resposta["text"] = csv_name

    def pega_img(self):
        self.img = filedialog.askopenfilename(initialdir = "/",title = "Selecione o arquivo",filetypes = (("Arquivos jpeg",".jpg"),("Arquivos separado por por ponto e virgula",".csv")))
        img_name = os.path.basename(self.img)
        self.img_resposta["text"] = img_name

    def disparar(self):
        self.text = self.nome.get('1.0', END)
        genio.disparo(self.csv, self.img, self.text)

if __name__ == '__main__':  
    root = Tk()
    root.title('Ourozap 1.0')
    Application(root)
    root.mainloop()