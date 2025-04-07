class tabla:
    def __init__ (self, numero):
        self.numero = numero

    def mostrarNormal (self):
        for i in range(1,11):
            print(f"{self.numero} x {i} = {self.numero*i}")

    def mostrarInvertido (self):
        for i in range(10,0,-1):
            print(f"{self.numero} x {i} = {self.numero*i}")

