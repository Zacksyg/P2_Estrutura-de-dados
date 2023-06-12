from customtkinter import *
from CTkMessagebox import *

from cadastro_animal import Tela_cadastro_animal
from cadastro_pessoa import Tela_cadastro_pessoa
from tela_relatorio import Tela_relatorio
from tela_pesquisa import Tela_pesquisa
from PIL import Image





class Menu(Tela_cadastro_animal, Tela_cadastro_pessoa, Tela_relatorio):
    def __init__(self):
        self.root_menu = CTk()
        self.widgets()
        self.root_menu.mainloop()
    
    def chamar_tela_animal(self):
        self.root_menu.destroy()
        Tela_cadastro_animal()
        
    def chamar_tela_pessoa(self):
        self.root_menu.destroy()
        Tela_cadastro_pessoa()

    def chamar_tela_relatorio(self):
        self.root_menu.destroy()
        Tela_relatorio()

    def chamar_tela_pesquisa(self):
        self.root_menu.destroy()
        Tela_pesquisa()

    def widgets(self):
        self.root_menu.title('Tela de Cadastro')
        self.root_menu.geometry('700x700')
        self.root_menu.resizable(False, False)
        self.root_menu.config(background='#1C1C1C')
        


        self.texto_bem_vindo = CTkLabel(self.root_menu, text='Seja Bem vindo.\n Clique em um dos botões abaixo para realizar a ação desejada',
                              font=('Arial',20),text_color='white',fg_color='#1C1C1C').place(relx=0.10 , rely=0.05)
        
        self.botao_cadastro_animal = CTkButton(master=self.root_menu, text='Cadastrar Animal',corner_radius=1, command=self.chamar_tela_animal,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.20, rely=0.20)
        
        self.botao_cadastro_pessoa = CTkButton(master=self.root_menu, text='Cadastrar Pessoa',corner_radius=1,command=self.chamar_tela_pessoa,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.55, rely = 0.20)
        
        self.botao_emitir_relatorio = CTkButton(master=self.root_menu, text='Emitir Relatório',corner_radius=1, command=self.chamar_tela_relatorio,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.20, rely = 0.30)
        
        self.botao_pesquisa = CTkButton(master=self.root_menu, text='Pesquisar Animal',corner_radius=1, command=self.chamar_tela_pesquisa,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.55, rely = 0.30)



Menu()

