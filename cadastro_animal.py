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