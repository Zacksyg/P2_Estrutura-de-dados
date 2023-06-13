from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tkinter import ttk 
import sqlite3



class Tela_pesquisa:
    def __init__(self):
        self.root_pesquisa = CTk()
        self.widgets()
        self.populate_treeview()
        self.root_pesquisa.mainloop()

    def conect_animal(self):
        self.conn = sqlite3.connect('Animal.bd')
        self.cursor = self.conn.cursor()
    
    def desconect(self):
        self.conn.close()

    def variaveis(self):
        self.especie = self.entry_especie.get()
        self.porte = self.box_porte.get()
        self.idade = self.box_idade.get()

    def populate_treeview(self):
        self.conect_animal()
        self.cursor.execute('SELECT * FROM animais')
        dados = self.cursor.fetchall()
        for dado in dados:
            self.tree.insert('', 'end', values=dado)
        self.desconect()
        
    def contador(self):
        self.selecionado = self.tree.selection()
        self.quantidade = len(self.selecionado)
        if self.quantidade == 0:
            CTkMessagebox(self.root_pesquisa, title='Erro', message='Nenhum Animal Encontrado', icon='cancel')
        else:
            CTkMessagebox(self.root_pesquisa, title='Encontrados', message=(self.quantidade,'Animais Encontrados!'), icon='check')
            

    def pesquisar_animal(self):
        self.variaveis()
        if self.especie == '':
            CTkMessagebox(self.root_pesquisa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.porte == '':
            CTkMessagebox(self.root_pesquisa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.idade == '':
            CTkMessagebox(self.root_pesquisa, title='Erro', message='Preencha todos os campos', icon='cancel')
        else:
            for child in self.tree.get_children():
                if self.especie.lower() in self.tree.item(child)['values'][0].lower() and self.porte.lower() in self.tree.item(child)['values'][1].lower() and self.idade.lower() in self.tree.item(child)['values'][2].lower():
                    self.tree.selection_add(child)
                    self.tree.see(child)
            self.contador()
               
    def desmarcar_animais(self):
        self.selecao = self.tree.selection()
        for item in self.selecao:
            self.tree.selection_remove(item)

    def widgets(self):
        self.root_pesquisa.title('Tela de Dados')
        self.root_pesquisa.geometry('900x900')
        self.root_pesquisa.resizable(False, False)
        self.root_pesquisa.config(background='#FFFFFF')
        self.image_botao = CTkImage(dark_image=Image.open('P2\imagens\check.png'), size=(50,50))

        self.tree = ttk.Treeview(self.root_pesquisa, columns=('Especie', 'Porte', 'Idade', 'Particularidade'), show='headings')
        self.tree.heading('Especie', text='Especie', )
        self.tree.heading('Porte', text='Porte')
        self.tree.heading('Idade', text='Idade')
        self.tree.heading('Particularidade', text='Particularidade')
        self.tree.pack(fill='both', expand=False)

        self.text_explicacao = CTkLabel(master=self.root_pesquisa,text='Pesquise o Animal Abaixo', bg_color='#FFFFFF', text_color='#2F4F4F', corner_radius=0, 
                                      font=('Arial',20)).place(relx= 0.38, rely=0.28)

        self.text_especie = CTkLabel(master=self.root_pesquisa,text='Especie:', bg_color='#FFFFFF', text_color='#2F4F4F', corner_radius=0, 
                                      font=('Arial',20)).place(relx= 0.05, rely=0.35)
        
        self.entry_especie = CTkEntry(master=self.root_pesquisa,bg_color='#B0E0E6',width=300, font=('Arial', 20))
        self.entry_especie.place(relx= 0.14, rely= 0.35)

        self.text_porte = CTkLabel(master=self.root_pesquisa,text='Porte:', bg_color='#FFFFFF', text_color='#2F4F4F', corner_radius=0, 
                                      font=('Arial',20)).place(relx= 0.55, rely=0.35)
        
        self.text_idade = CTkLabel(master=self.root_pesquisa,text='Idade:', bg_color='#FFFFFF', text_color='#2F4F4F', corner_radius=0, 
                                      font=('Arial',20)).place(relx= 0.05, rely=0.40)
        
        self.box_idade = CTkComboBox(master=self.root_pesquisa, values=('<1 Ano', '1 - 2 Anos', '2 - 3 Anos', '3 - 4 Anos', '4+ Anos'),
                                     bg_color='#B0E0E6', width=300, font=('Arial', 20))
        self.box_idade.place(relx= 0.14, rely= 0.40)

        self.box_porte = CTkComboBox(master=self.root_pesquisa, values=('Pequeno', 'Médio', 'Grande'),bg_color='#B0E0E6',
                                    width=300, font=('Arial', 20))
        self.box_porte.place(relx= 0.62, rely= 0.35)

        self.botao_pesquisar = CTkButton(master=self.root_pesquisa, text='Pesquisar',command=self.pesquisar_animal, height=50, image=self.image_botao)
        self.botao_pesquisar.place(relx = 0.50, rely = 0.60)

        self.botao_resetar = CTkButton(master=self.root_pesquisa, text='Resetar',command=self.desmarcar_animais, height=55)
        self.botao_resetar.place(relx = 0.30, rely = 0.60)
        


