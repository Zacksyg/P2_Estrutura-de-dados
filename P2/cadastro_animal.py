from customtkinter import *
from CTkMessagebox import *
from PIL import Image
import sqlite3

class Tela_cadastro_animal:
    def __init__(self):
        self.root_animal = CTk()
        self.widgets()
        self.monta_tabela_animal()
        self.root_animal.mainloop()

    def variaveis(self):
        self.especie = self.box_especie.get()
        self.porte = self.box_porte.get()
        self.idade = self.box_idade.get()
        self.particularidade = self.entry_particularidade.get()

    def conect(self):
        self.conn = sqlite3.connect('Animal.bd')
        self.cursor = self.conn.cursor()
    
    def desconect(self):
        self.conn.close()

    def monta_tabela_animal(self):
        self.conect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animais(
                especie CHAR(40) NOT NULL,
                porte CHAR(12) NOT NULL,
                idade INT(13) NOT NULL,
                particularidade CHAR(40) NOT NULL                
            );                
        ''')
        self.conn.commit()
        self.desconect()

    def novo_animal(self):
        if  self.box_especie.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.box_porte.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.box_idade.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.entry_particularidade.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        else:
            self.variaveis()
            self.conect()
            self.cursor.execute(""" INSERT INTO animais (especie, porte, idade, particularidade)
                VALUES (?,?,?,?)""", (self.especie, self.porte, self.idade, self.particularidade))
            self.conn.commit()
            self.desconect()
            CTkMessagebox(self.root_animal,title='Check', message='Registro Concluido com Sucesso!')

     
    
       
            
           
    

    def widgets(self):
        self.root_animal.title('Tela de Cadastro')
        self.root_animal.geometry('700x700')
        self.root_animal.resizable(False, False)
        self.root_animal.config(background='#B0E0E6')
        
        self.image_botao = CTkImage(dark_image=Image.open('P2\imagens\check.png'), size=(50,50))

        self.image = CTkImage(dark_image=Image.open('P2\imagens\imagem1.png'), size=(700,700))
        self.label_image = CTkLabel(self.root_animal, image=self.image,width=700, height=700)
        self.label_image.place(relx=0.00, rely=0.00)

        self.texto_inicial = CTkLabel(master=self.root_animal, text='Digite ou Selecione Abaixo As Informações Do Animal.', fg_color='transparent', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20)).place(relx= 0.20, rely=0.05)
        
        self.text_especie = CTkLabel(master=self.root_animal,text='Especie', fg_color='transparent', text_color='#2F4F4F', corner_radius=0, 
                                      font=('Arial',20)).place(relx= 0.45, rely=0.12)
        
        self.box_especie = CTkComboBox(master=self.root_animal, values=('Canino', 'Felino', 'Reptil', 'Peixe', 'Ave','Roedor','Apague e Digite A Especie'),
                                        bg_color='#B0E0E6',width=300, font=('Arial', 20))
        self.box_especie.place(relx= 0.30, rely= 0.17)
        
        

        self.text_idade = CTkLabel(master=self.root_animal,text='Idade', fg_color='transparent', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20))
        self.text_idade.place(relx= 0.46, rely=0.22)

        
        self.box_idade = CTkComboBox(master=self.root_animal, values=('<1 Ano', '1 - 2 Anos', '2 - 3 Anos', '3 - 4 Anos', '4+ Anos'),
                                     bg_color='#B0E0E6', width=300, font=('Arial', 20))
        self.box_idade.place(relx= 0.30, rely= 0.27)

        
        self.text_porte = CTkLabel(master=self.root_animal, text='Porte', fg_color='transparent', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20))
        self.text_porte.place(relx= 0.46, rely=0.32)


        self.box_porte = CTkComboBox(master=self.root_animal, values=('Pequeno', 'Médio', 'Grande'),bg_color='#B0E0E6',
                                    width=300, font=('Arial', 20))
        self.box_porte.place(relx= 0.30, rely= 0.37)

        self.text_particularidade = CTkLabel(master=self.root_animal, text = 'Particularidade', fg_color='transparent', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20))
        self.text_particularidade.place(relx= 0.41, rely=0.42)

        
        self.entry_particularidade = CTkEntry(master=self.root_animal, width=300, font=('Arial', 15),bg_color='transparent', corner_radius=25)
        self.entry_particularidade.place(relx = 0.30, rely = 0.47)

        

        self.botao_cadastrar = CTkButton(master=self.root_animal, text='Cadastrar', command=self.novo_animal, height=50, image=self.image_botao)
        self.botao_cadastrar.place(relx = 0.40, rely = 0.65)

       

Tela_cadastro_animal()
