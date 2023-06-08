from customtkinter import *
from CTkMessagebox import *

class Tela_cadastro_animal:
    def __init__(self):
        self.root_animal = CTk()
        self.widgets()
        self.root_animal.mainloop()

  


    def novo_animal(self):
        if  self.box_especie.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.box_porte.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.box_idade.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
        elif self.entry_particularidade.get() == '':
            CTkMessagebox(self.root_animal, title='Erro', message='Preencha todos os campos', icon='cancel')
     
    
    

    def widgets(self):
        self.root_animal.title('Tela de Cadastro')
        self.root_animal.geometry('700x700')
        self.root_animal.resizable(False, False)
        self.root_animal.config(background='#B0E0E6')

        self.texto_inicial = CTkLabel(master=self.root_animal, text='Digite ou Selecione Abaixo As Informações Do Animal.', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20)).place(relx= 0.20, rely=0.05)
        
        self.text_especie = CTkLabel(master=self.root_animal,text='Especie', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0, 
                                      font=('Arial',20)).place(relx= 0.45, rely=0.12)
        
        self.box_especie = CTkComboBox(master=self.root_animal, values=('Canino', 'Felino', 'Reptil', 'Peixe', 'Ave','Outro'),
                                        bg_color='#B0E0E6',width=300, font=('Arial', 20))
        self.box_especie.place(relx= 0.30, rely= 0.17)
        
        

        self.text_idade = CTkLabel(master=self.root_animal,text='Idade', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20))
        self.text_idade.place(relx= 0.46, rely=0.22)

        
        self.box_idade = CTkComboBox(master=self.root_animal, values=('<1 Ano', '1 - 2 Anos', '2 - 3 Anos', '3 - 4 Anos', '4+ Anos'),
                                     bg_color='#B0E0E6', width=300, font=('Arial', 20))
        self.box_idade.place(relx= 0.30, rely= 0.27)

        
        self.text_porte = CTkLabel(master=self.root_animal, text='Porte', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20))
        self.text_porte.place(relx= 0.46, rely=0.32)


        self.box_porte = CTkComboBox(master=self.root_animal, values=('Pequeno', 'Médio', 'Grande'),bg_color='#B0E0E6',
                                    width=300, font=('Arial', 20))
        self.box_porte.place(relx= 0.30, rely= 0.37)

        self.text_particularidade = CTkLabel(master=self.root_animal, text = 'Particularidade', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20))
        self.text_particularidade.place(relx= 0.41, rely=0.42)

        
        self.entry_particularidade = CTkEntry(master=self.root_animal, width=300, font=('Arial', 15),bg_color='#B0E0E6', corner_radius=25)
        self.entry_particularidade.place(relx = 0.30, rely = 0.47)


        self.botao_cadastrar = CTkButton(master=self.root_animal, text='Cadastrar', command=self.novo_animal)
        self.botao_cadastrar.place(relx = 0.40, rely = 0.65)

        









class Tela_cadastro_pessoa:
    def __init__(self):
        self.root_pessoa  = CTk()
        self.widgets()
        self.root_pessoa.mainloop()

    def widgets(self):
        self.root_pessoa.title('Tela De Cadastro De Pessoa')
        self.root_pessoa.geometry('700x700')
        self.root_pessoa.resizable(False, False)
        self.root_pessoa.config(background='#A9A9A9')
        
        self.text_inicio = CTkLabel(master=self.root_pessoa, text='Digite ou Selecione Abaixo As suas Informações.', font=('Arial',20),fg_color='#A9A9A9').place(relx = 0.20, rely=0.05)
        
        self.text_nome = CTkLabel(master=self.root_pessoa, text='Nome',font=('Arial',21),fg_color='#A9A9A9',corner_radius=0).place(relx = 0.45, rely=0.12)
        self.entry_nome = CTkEntry(master=self.root_pessoa, width=250, corner_radius=1).place(relx=0.32, rely= 0.17)

        self.text_telefone = CTkLabel(master=self.root_pessoa, text='Telefone',font=('Arial',20),fg_color='#A9A9A9').place(relx = 0.43, rely=0.24)
        self.entry_telefone = CTkEntry(master=self.root_pessoa, width=150, corner_radius=1).place(relx=0.38, rely=0.29)
    
        self.text_cpf = CTkLabel(master=self.root_pessoa, text='Cpf', font=('Arial',21),fg_color='#A9A9A9', corner_radius=0).place(relx = 0.46, rely=0.35)
        self.entry_cpf = CTkEntry(master=self.root_pessoa, width=150,  corner_radius=1).place(relx = 0.38, rely = 0.39)

        self.text_endereco = CTkLabel(master=self.root_pessoa, text='Endereço', font=('Arial',21), fg_color='#A9A9A9').place(relx = 0.42, rely = 0.44)
        self.entry_endereco = CTkEntry(master=self.root_pessoa, width=250, corner_radius=25, bg_color='#A9A9A9').place(relx = 0.32, rely= 0.49)
        
        
    
        







class Menu(Tela_cadastro_animal, Tela_cadastro_pessoa):
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
        
        self.botao_emitir_relatorio = CTkButton(master=self.root_menu, text='Emitir Relatório',corner_radius=1,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.35, rely = 0.30)
        




Menu()

'''def novo_cliente_caixa1(self):
        if self.nome_entry.get() == '':
            messagebox.showerror(title=None, message='Preencha Todos os campos.')
        elif self.data_nasc_entry.get() == '':
            messagebox.showerror(title=None, message='Preencha Todos os campos.')
        else:
            self.nome = self.nome_entry.get()
            self.sexo = self.sexo_text.get()
            self.data_nasc = self.data_nasc_entry.get()
            self.operacao = self.operacao_texto.get()
            self.cliente_banco = self.cliente_texto.get()'''
