
class Conta:
        
    def __init__(self, numero, titular, saldo, limite):
# __init__ = este método define o construtor da classe, ou seja, é onde definimos como uma nova pessoa será criada em nosso programa.
# __init__ = é uma função especial que podemos aplicar para inicializar uma classe,
        print("Construindo objeto... {}".format(self))
        self.__numero = numero    #Underscore __ serve para privar o resultado e só permite ser alterado com as outras funções DEF.
        self.__titular = titular  #permite seu acesso apenas por meio dos métodos da classe, usando o prefixo __
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
        
    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")
    
    def deposita(self, valor):
        self.__saldo += valor
        
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
     
    @property   
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    @staticmethod #este método pode ser invocado sem a necessidade de que você tenha uma 
 #instância desta classe. O codigo vai chamar o codigo_banco sem precisar de conta.
    def codigo_banco(self):
        return self.__codigo_banco
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}