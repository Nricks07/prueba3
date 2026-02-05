from SistemaInven import *

prod1 = Producto("Maruchan", 16, 100)
prod1.apli_desc(0.30)
prod1.actualizar_stock(-120)
prod1.actualizar_stock(120)
prod1.actualizar_stock(100)

prod2 = Celular("chaifon", 10, 10, )