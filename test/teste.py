import json

class user:
    def __init__(self, nome : str, idade : int, id : int):
        self.nome = nome
        self.idade = idade
        self.id = id
    @property
    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "id": self.id
        }
    

eu = user(
    nome= "flavio",
    idade= 19,
    id= 1
    )


with open('usuario.json', 'a', encoding='utf-8') as f:

    json.dump(eu.to_dict, f, indent=6)
