from customtkinter import *
from CTkMessagebox import *
from PIL import Image



class Tela_cadastro_pessoa:
    def __init__(self):
        self.root_pessoa  = CTk()
        self.widgets()
        self.root_pessoa.mainloop()
    
    def variaveis(self):
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.telefone = self.entry_telefone.get()
        self.endereco = self.entry_endereco.get()

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
        elif not self.cpf.isnumeric():
            CTkMessagebox(self.root_pessoa, title='Erro', message='Digite Apenas Números no campo do cpf', icon='cancel')
        

    def widgets(self):
        self.root_pessoa.title('Tela De Cadastro De Pessoa')
        self.root_pessoa.geometry('700x700')
        self.root_pessoa.resizable(False, False)
        self.root_pessoa.config(background='#A9A9A9')

        self.image_botao = CTkImage(dark_image=Image.open('check.png'), size=(50,50))
        
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
        
        self.botao_cadastrar = CTkButton(master=self.root_pessoa, text='Cadastrar', height=50 , image=self.image_botao , command=self.nova_pessoa)
        self.botao_cadastrar.place(relx=0.40, rely= 0.55)
