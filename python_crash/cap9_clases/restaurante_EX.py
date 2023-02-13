# 9.1

class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos nombre y tipo de cocina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0 # 9.4
    

    def describir_restaurante(self):
        """Describe el restaurante."""
        print(f"\nEl restaurante {self.nombre_restaurante.title()} tiene una cocina tipo: {self.tipo_cocina} y ha servido a {self.numero_servido} personas")
    

    def abrir_restaurante(self):
        """Anuncia que el restaurante esta abierto."""
        print(f"\nEl restaurante {self.nombre_restaurante.title()} ya esta abierto!")
    

    def establecer_numero_servido(self, clientes): #9.4
        """Configura el numero de clientes servidos."""
        if clientes > 0:
            self.numero_servido = clientes
    

    def incrementar_numero_servido(self, client):
        """Incrementa el numero de clientes servidos por el restaurante."""
        if client > 0:
            self.numero_servido += client



rest_1 = Restaurante('txitxarreria', 'brasas')

print(rest_1.nombre_restaurante)
print(rest_1.tipo_cocina)

rest_1.describir_restaurante()
rest_1.abrir_restaurante()

# 9.2

rest_2 = Restaurante('goiko', 'plancha')
rest_3 = Restaurante('juanchos', 'parrilla')
rest_4 = Restaurante('pummarola', 'horno de leña')

rest_2.describir_restaurante()
rest_3.describir_restaurante()
rest_4.describir_restaurante()

# 9.4

restaurante = Restaurante('kfc','???')

restaurante.describir_restaurante()
restaurante.numero_servido = 23_300_987
restaurante.describir_restaurante()

restaurante.establecer_numero_servido(89)
restaurante.describir_restaurante()

restaurante.incrementar_numero_servido(100)
restaurante.describir_restaurante()