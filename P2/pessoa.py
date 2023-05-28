class Pessoa:
    def __init__(self, nome, idade, preferencia):
        self.nome = nome
        self.idade = idade
        self.preferencia = preferencia
    
    def exibir_info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Preferencia: {self.preferencia}')
    
    
    