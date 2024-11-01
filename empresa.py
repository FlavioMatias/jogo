class Empresa():
    def __init__(self, name : str):
        self._name = name
        self._clients = []
        
    def SetName(self, new_name : str):
        self._name = new_name
        
    def GetName(self):
        return self._name
    
    def insert(self, cliente : object):
        self._clients.append((cliente, cliente._cpf))
        
    def listar(self):
        for client in self._clients:
            print(client[0]._name)
            
        
    
    
class Cliente():
    def __init__(self, name : str, cpf : str, limite : float):
        self._name = name
        self._cpf = cpf
        self._limite = limite
        self._socio = None
        
    def SetSocio(self, socio : object):
        if self._socio is None and socio._socio is None:
            self._socio = socio
            socio._socio = self
            
    def GetLimite(self):
        if self._socio:
            return self._limite + self._socio._limite
        else:
            return self._limite
            
    def ToString(self):
        return [self._name, self._cpf, self._limite, self._socio]
        
class UI:

    def menu():
        menu = r'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                          MENU DE OPÇÕES                                          ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                                                                  ┃
┃   Escolha uma das opções abaixo:                                                                 ┃
┃                                                                                                  ┃
┃   [1]  Criar uma empresa                     ┃   [4]  Listar clientes               ┃  [0] Sair  ┃
┃   [2]  Adicionar um cliente na empresa       ┃   [5]  Mudar nome da empresa         ┃            ┃
┃   [3]  Associar um cliente a outro           ┃   [6]  Ver informações de um cliente ┃            ┃
┃                                                                                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        print(menu)
                
        return int(input("Digite uma opcao: "))
    
    def main(cls):
        
        op = cls.menu()
        while op != 0:
            if op == 1:
            else:
                print("Opcao inexitente, digite novamente, gay")
UI.menu()
