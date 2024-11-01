class Empresa():
    def __init__(self, name : str):
        self._name = name
        self._clients = []
        
    def SetName(self, new_name : str):
        self._name = new_name
        
    def GetName(self):
        return self._name
    
    def insert(self, cliente : object):
        self._clients.append(cliente)
        
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
    empresa = None
    
    @staticmethod
    def menu():
        menu = r'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                          MENU DE OPÇÕES                                          ┃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                                                                                  ┃
   Escolha uma das opções abaixo:                                                                 ┃
                                                                                                  ┃
   [1]  Criar uma empresa                     ┃   [4]  Listar clientes               ┃  [0] Sair  ┃
   [2]  Adicionar um cliente na empresa       ┃   [5]  Mudar nome da empresa         ┃            ┃
   [3]  Associar um cliente a outro           ┃   [6]  Ver informações de um cliente ┃            ┃
                                                                                                  ┃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        print(menu)
        return int(input("Digite uma opcao: "))
    
    @classmethod
    def main(cls):
        op: int = cls.menu()
        while op != 0:
            if op == 1:
                cls.new_empresa()
            elif op == 2:

                print("Adicionando um cliente...")
            elif op == 3:

                print("Associando clientes...")
            elif op == 4:

                print("Listando clientes...")
            elif op == 5:

                print("Mudando nome da empresa...")
            elif op == 6:

                print("Verificando informações do cliente...")
            else:
                print("Opcao inexistente, digite novamente.")
            op = cls.menu() 
    
    @classmethod
    def new_empresa(cls):
        
        name = input(r'''
qual o nome da sua empresa?
Name:                      
''')
        empresa = Empresa(
            name= name
        )
        print(f"A empresa {empresa} foi criada!")

# Para executar o menu:
UI.main()
