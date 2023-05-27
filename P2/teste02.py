class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def exibir_detalhes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Espécie:", self.especie)


class CadastroAnimais:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def exibir_animais(self):
        if not self.animais:
            print("Nenhum animal cadastrado.")
        else:
            for animal in self.animais:
                animal.exibir_detalhes()



cadastro = CadastroAnimais()

animal1 = Animal("Rex", 5, "Cachorro")
cadastro.adicionar_animal(animal1)

animal2 = Animal("Mia", 3, "Gato")
cadastro.adicionar_animal(animal2)

animal3 = Animal("Daisy", 2, "Coelho")
cadastro.adicionar_animal(animal3)

cadastro.exibir_animais()
