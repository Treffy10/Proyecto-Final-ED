
class Caja:
    def __init__(self, id):
        self.id = id
        self.productoVendido = []

    def getID(self):
        return self.id

    def getProductoVendido(self):
        return self.productoVendido

    def setProductoVendido(self, producto):
        self.productoVendido = producto


