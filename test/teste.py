class Mochila:
    def __init__(self):
        self.__bolso = {}
        
    def guardar(self, item, quantidade):
        if item in self.__bolso:
            self.__bolso[item] += quantidade
        else:
            self.__bolso[item] = quantidade
        
        
    def tirar(self, item, quantidade):
        if self.__bolso[item] > quantidade:
            self.__bolso[item] -= quantidade
        else:
            raise ValueError("vc nao tem tudo isso")
            

        
        
    def ver(self):
        for item, quantidade in self.__bolso.items():
            print(f"{item} : {quantidade}")
        
class Pessoa:
    def __init__(self, name):
        self.name = name
        self.mochila = Mochila()
        
p1 = Pessoa(
    name="flavio"
)

p1.mochila.guardar(
    item="lapis",
    quantidade= 3
)
p1.mochila.guardar(
    item="caderno",
    quantidade=1
)

p1.mochila.guardar(
    item="lapis",
    quantidade= 1
)

p1.mochila.ver()
p1.mochila.tirar(
    item="lapis",
    quantidade=2
)
print("---- caderno depois ----")
p1.mochila.ver()