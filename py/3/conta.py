class Conta:
    """
        Na classe se descreve o objeto
        Descreve as caracteristicas, atributos

        __ na freten do atributo é deixar o acesso a ele privado
    """

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titula = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}'.format(self.saldo, self.titula))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

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
