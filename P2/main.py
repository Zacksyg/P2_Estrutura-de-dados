from animal import Animal
from cadastro_animal import CadastroAnimais
from pessoa import *

if __name__== '__main__':


    cadastro = CadastroAnimais()

    animal1 = Animal('Zé' , 12, 'felino' , 'grande', 'nenhuma')
    cadastro.adicionar_animal(animal1)

    cadastro.exibir_animais()
    
    luiz = Pessoa('Luiz', '21', 'Gato')
