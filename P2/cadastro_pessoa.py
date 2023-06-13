from customtkinter import *
from CTkMessagebox import *
from PIL import Image
import sqlite3


class Tela_cadastro_pessoa:
    def __init__(self):
        self.root_pessoa  = CTk()
        self.widgets()
        self.monta_tabela_pessoa()
        self.root_pessoa.mainloop()
    
    def variaveis(self):
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.telefone = self.entry_telefone.get()
        self.endereco = self.entry_endereco.get()
        self.escolha_especie = self.box_escolha_especie.get()
        self.porte = self.box_porte.get()


    def conect(self):
        self.conn = sqlite3.connect('Pessoa.bd')
        self.cursor = self.conn.cursor()
    
    def conect_animais(self):
        self.conn = sqlite3.connect('Animal.bd')
        self.cursor_animal = self.conn.cursor()
    
    def desconect(self):
        self.conn.close()

    def monta_tabela_pessoa(self):
        self.conect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoa(
                nome CHAR(40) NOT NULL,
                cpf INT(12) NOT NULL,
                telefone INT(13) NOT NULL,
                endereco CHAR(40) NOT NULL,
                escolha_especie CHAR(40) NOT NULL,
                porte CHAR(20) NOT NULL
            );                
        ''')
        self.conn.commit()
        self.desconect()

   

    def nova_pessoa(self):
        self.variaveis()
        if  self.entry_nome.get() == '':
            CTkMessagebox(self.root_pessoa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.entry_telefone.get() == '':
            CTkMessagebox(self.root_pessoa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.entry_cpf.get() == '':
            CTkMessagebox(self.root_pessoa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.entry_endereco.get() == '':
            CTkMessagebox(self.root_pessoa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif not self.telefone.isnumeric():
             CTkMessagebox(self.root_pessoa, title='Erro', message='Digite Apenas Números no Campo do Telefone!', icon='cancel')
        elif not len(self.telefone) == 11:
            CTkMessagebox(self.root_pessoa, title='Erro', message='Digite somente os números do seu celular(COM DDD e Sem Traço).', icon='cancel')
        elif not self.cpf.isnumeric():
            CTkMessagebox(self.root_pessoa, title='Erro', message='Digite Apenas Números no Campo do Cpf!', icon='cancel')
        elif not len(self.cpf) == 11:
            CTkMessagebox(self.root_pessoa, title='Erro', message='Digite os 11 números do seu Cpf (sem Símbolos)', icon='cancel')
        elif self.box_escolha_especie.get() == '':
            CTkMessagebox(self.root_pessoa, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.box_porte.get() == '':
            CTkMessagebox(self.root_pessoa, title='Erro', message='Preencha todos os campos', icon='cancel')
        else:
            self.variaveis()
            self.conect()
            self.cursor.execute(""" INSERT INTO pessoa (nome, cpf, telefone, endereco, escolha_especie, porte)
                VALUES (?,?,?,?,?,?)""", (self.nome, self.cpf, self.telefone, self.endereco, self.escolha_especie, self.porte))
            self.conn.commit()
            self.desconect()
            CTkMessagebox(self.root_pessoa,title='Check', message='Registro Concluido com Sucesso!')

    def widgets(self):
        self.root_pessoa.title('Tela De Cadastro De Pessoa')
        self.root_pessoa.geometry('700x700')
        self.root_pessoa.resizable(False, False)
        self.root_pessoa.config(background='#A9A9A9')

        self.image_botao = CTkImage(dark_image=Image.open('P2\imagens\check.png'), size=(50,50))
        
        self.text_inicio = CTkLabel(master=self.root_pessoa, text='Digite ou Selecione Abaixo As suas Informações.', font=('Arial',20),fg_color='#A9A9A9')
        self.text_inicio.place(relx = 0.20, rely=0.05)
        
        self.text_nome = CTkLabel(master=self.root_pessoa, text='Nome',font=('Arial',21),fg_color='#A9A9A9',corner_radius=0)
        self.text_nome.place(relx = 0.45, rely=0.12)

        self.entry_nome = CTkEntry(master=self.root_pessoa, width=250, corner_radius=1)
        self.entry_nome.place(relx=0.32, rely= 0.17)

        self.text_telefone = CTkLabel(master=self.root_pessoa, text='Telefone',font=('Arial',20),fg_color='#A9A9A9')
        self.text_telefone.place(relx = 0.43, rely=0.24)

        self.entry_telefone = CTkEntry(master=self.root_pessoa, width=150, corner_radius=1)
        self.entry_telefone.place(relx=0.38, rely=0.29)
    
        self.text_cpf = CTkLabel(master=self.root_pessoa, text='Cpf', font=('Arial',21),fg_color='#A9A9A9', corner_radius=0)
        self.text_cpf.place(relx = 0.46, rely=0.35)
        
        self.entry_cpf = CTkEntry(master=self.root_pessoa, width=150,  corner_radius=1)
        self.entry_cpf.place(relx = 0.38, rely = 0.39)

        self.text_endereco = CTkLabel(master=self.root_pessoa, text='Endereço', font=('Arial',21), fg_color='#A9A9A9')
        self.text_endereco.place(relx = 0.42, rely = 0.44)

        self.entry_endereco = CTkEntry(master=self.root_pessoa, width=250, corner_radius=25, bg_color='#A9A9A9')
        self.entry_endereco.place(relx = 0.32, rely= 0.49)
        
        self.text_escolha_especie = CTkLabel(master=self.root_pessoa, text ='Especie Desejada', font=('Arial', 20), bg_color='#A9A9A9')
        self.text_escolha_especie.place(relx = 0.40, rely = 0.55)

        self.box_escolha_especie =  CTkComboBox(master=self.root_pessoa,  values=('Canino', 'Felino', 'Reptil', 'Peixe', 'Ave','Apague e Digite A Especie'),
                                     bg_color='#B0E0E6', width=300, font=('Arial', 20))
        self.box_escolha_especie.place(relx = 0.30, rely = 0.60)
        
        self.text_porte = CTkLabel(master=self.root_pessoa, text='Porte', bg_color='#A9A9A9', corner_radius=0,
                                      font=('Arial',20))
        self.text_porte.place(relx= 0.46, rely=0.65)


        self.box_porte = CTkComboBox(master=self.root_pessoa, values=('Pequeno', 'Médio', 'Grande'),bg_color='#A9A9A9',
                                    width=300, font=('Arial', 20))
        self.box_porte.place(relx= 0.30, rely= 0.70)

        self.botao_cadastrar = CTkButton(master=self.root_pessoa, text='Cadastrar', height=50 , image=self.image_botao , command=self.nova_pessoa,bg_color='transparent', corner_radius=1)
        self.botao_cadastrar.place(relx=0.40, rely= 0.82)

    




