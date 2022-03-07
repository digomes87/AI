class Conta:
    """
        Na classe se descreve o objeto
        Descreve as caracteristicas, atributos

        __ na freten do atributo é deixar o acesso a ele privado
    """

    def __init__(self, numero, titular, saldo, limite):  # construtor
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titula = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}'.format(self.saldo, self.titula))

    def deposita(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.saldo -= valor
        else:
            print("Passou o limite de {}".format(self.__limite))

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)

    # sempre que quiser algo do objeto escriva um metodo pra isso

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titula

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
