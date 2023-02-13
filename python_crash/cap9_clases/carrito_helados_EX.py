
# 9.6

class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos nombre y tipo de cocina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
        
    
    def describir_restaurante(self):
        """Describe el restaurante."""
        print(f"\nEl restaurante {self.nombre_restaurante.title()} tiene una cocina tipo: {self.tipo_cocina} y ha servido a {self.numero_servido} personas")
    

    def abrir_restaurante(self):
        """Anuncia que el restaurante esta abierto."""
        print(f"\nEl restaurante {self.nombre_restaurante.title()} ya esta abierto!")
    

    def establecer_numero_servido(self, clientes):
        """Configura el numero de clientes servidos."""
        if clientes > 0:
            self.numero_servido = clientes
    

    def incrementar_numero_servido(self, client):
        """Incrementa el numero de clientes servidos por el restaurante."""
        if client > 0:
            self.numero_servido += client


class CarritoHelados(Restaurante):
    """Intento de modelar un carrito de helados."""
    def __init__(self, nombre_restaurante, tipo_cocina='heladeria'):
        """Inicializa los atributos de la heladeria."""
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores_helado = []
    

    def mostrar_sabores(self):
        """Muestra los sabores del carrito de helados."""
        print(f"\nEl carrito de helados tiene {len(self.sabores_helado)} helados:")
        for sabor in self.sabores_helado:
            print("- " + sabor.title())


livorno = CarritoHelados('livorno')
livorno.sabores_helado = ['vainilla', 'chocolate', 'pistacho']

livorno.describir_restaurante()
livorno.mostrar_sabores()