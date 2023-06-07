from customtkinter import *


class Tela_cadastro_animal:
    def __init__(self):
        self.root_animal = CTk()
        self.widgets()
        self.root_animal.mainloop()
        

    def widgets(self):
        self.root_animal.title('Tela de Cadastro')
        self.root_animal.geometry('700x700')
        self.root_animal.resizable(False, False)
        self.root_animal.config(background='#B0E0E6')

        self.texto_inicial = CTkLabel(master=self.root_animal, text='Digite ou Selecione Abaixo As Informações Do Animal.', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20)).place(relx= 0.20, rely=0.05)
        
        self.text_especie = CTkLabel(master=self.root_animal,text='Especie', fg_color='#B0E0E6', text_color='#2F4F4F', corner_radius=0,
                                      font=('Arial',20)).place(relx= 0.45, rely=0.12)
        
        self.box_especie = CTkComboBox(master=self.root_animal, values=('Canino', 'Felino', 'Reptil', 'Peixe', 'Ave'), width=300, font=('Arial', 20)).place(relx= 0.30, rely= 0.17)






class Menu(Tela_cadastro_animal):
    def __init__(self):
        self.root_menu = CTk()
        self.widgets()
        self.root_menu.mainloop()
        

    def widgets(self):
        self.root_menu.title('Tela de Cadastro')
        self.root_menu.geometry('700x700')
        self.root_menu.resizable(False, False)
        self.root_menu._set_appearance_mode("dark")
        


        self.texto_bem_vindo = CTkLabel(self.root_menu, text='Seja Bem vindo.\n Clique em um dos botões abaixo para realizar a ação desejada',
                              font=('Arial',20),text_color='white',fg_color='black').place(relx=0.10 , rely=0.05)
        
        self.botao_cadastro_animal = CTkButton(master=self.root_menu, text='Cadastrar Animal',corner_radius=1,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.20, rely=0.20)
        
        self.botao_cadastro_pessoa = CTkButton(master=self.root_menu, text='Cadastrar Pessoa',corner_radius=1,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.55, rely = 0.20)
        
        self.botao_emitir_relatorio = CTkButton(master=self.root_menu, text='Emitir Relatório',corner_radius=1,
                                               font=('Arial',20), text_color='black' , width=200, height=50).place(relx=0.35, rely = 0.30)
        


