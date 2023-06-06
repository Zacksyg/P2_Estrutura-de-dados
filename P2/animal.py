from cadastro_animal import *
class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def exibir_detalhes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Espécie:", self.especie)

Animal()

