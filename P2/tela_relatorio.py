from customtkinter import *
from CTkMessagebox import *
from tkinter import ttk
import sqlite3

class Tela_relatorio:
    def __init__(self):
        self.root_relatorio = CTk()
        self.widgets()
        self.pareamento()
        self.root_relatorio.mainloop()
    
    def conect_animal(self):
        self.conn = sqlite3.connect('Animal.bd')
        self.cursor_animal = self.conn.cursor()

    def conect_pessoa(self):
        self.conn = sqlite3.connect('Pessoa.bd')
        self.cursor_pessoa = self.conn.cursor()

    def desconect(self):
        self.conn.close() 


    def pareamento(self):
        self.conect_animal()
        self.conect_pessoa()
        self.consulta_animais = "SELECT DISTINCT especie, porte, idade, particularidade FROM animais"
        self.cursor_animal.execute(self.consulta_animais)
        self.consulta_pessoas = "SELECT DISTINCT nome, cpf, telefone, endereco, escolha_especie, porte FROM pessoa"
        self.cursor_pessoa.execute(self.consulta_pessoas)

        self.dados_pessoas = self.cursor_pessoa.fetchall()
        self.dados_animais = self.cursor_animal.fetchall()
        self.tamanho_lista = min(len(self.dados_pessoas), len(self.dados_animais))
        
        for indice in range(self.tamanho_lista):
            self.pessoa = self.dados_pessoas[indice]
            self.animal = self.dados_animais[indice]
            if self.pessoa[4] == self.animal[0] and self.pessoa[5] == self.animal[1]:
                pessoa_str = [str(elemento) for elemento in self.pessoa]
                animal_str = [str(elemento) for elemento in self.animal]

                pessoa_completa = ', '.join(pessoa_str)
                animal_completo = ', '.join(animal_str)

                self.tree.insert('', 'end', text=str(indice+1), values=(pessoa_completa, animal_completo))

        self.desconect()

    def widgets(self):
        self.root_relatorio.title('Tela de Relatorio')
        self.root_relatorio.geometry('700x700')
        self.root_relatorio.resizable(False, False)
        self.root_relatorio.config(background='#B0E0E6')

        self.tree = ttk.Treeview(self.root_relatorio, columns=('Pessoa', 'Animal'), show='headings')
        self.tree.heading('#0', text='Item', )
        self.tree.heading('Pessoa', text='Pessoa')
        self.tree.heading('Animal', text='Animal')
        self.tree.pack(fill='both', expand=False)





