class Producto():
    def __init__(self, name, precio_base, stock):
        self.nombre = name
        self.precio = precio_base
        self.stock = stock

    def apli_desc(self, porcent):
        self.precio *= (1 - porcent)
        print(f"El nuevo precio es {self.precio}")

    def actualizar_stock(self, cantidad):
        if (self.stock + cantidad) < 0:
            print("no puedes tener stock negativo")
        else:
            self.stock += cantidad
            print(f"La nueva cantidad es {self.stock}")

class Categoria():
    def __init__(self, nombcat):
        self.nombre_cate = nombcat
        self.lista = []

    def agregar_producto(self):
        self.lista.append(self, producto)
        self.lista.append(producto)

    def valor_total_categoria(self):
        pass



