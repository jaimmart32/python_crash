# 9.7 y 9.8


class Usuario:
    def __init__(self, nombre, apellido, **user_info):
        """"Inicializa los atributos nombre, apellido y información 
        que suele guardarse en un perfil de usuario."""
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_inicio = 0 #9.5
        self.user_info = user_info
    

    def describir_usuario(self):
        """Describe al usuario mostrando el diccionarío con la información."""
        print(f"{self.nombre.title()} {self.apellido.title()}.")
        print(self.user_info)
    

    def saludar_usuario(self):
        """Imprime un saludo personalizado para el usuario."""
        print(f"\nHola {self.nombre.title()} {self.apellido.title()}, bienvenido!\n")
    

    def incrementar_intentos_inicio(self, intentos): #9.5
        """Incrementa el numero de intentos de inicio de sesión."""
        if intentos > 0:
            self.intentos_inicio += intentos
    

    def restablecer_intentos_inicio(self): #9.5
        """Restablece el numero de intentos de inicio de sesión."""
        self.intentos_inicio = 0


class Privilegios:
    """Intento de modelar privilegios en un usuario."""

    def __init__(self,privilegios=[]):
        """Inicializa el atributo privilegios."""
        self.privilegios = privilegios
    
    
    def mostrar_privilegios(self):
        "Muestra los privilegios de un usuario."
        print("\nPrivilegios:")
        if self.privilegios:
            for privilegio in self.privilegios:
                print("- " + privilegio)
        else:
            print("- Este usuario no tiene privilegios.")

class Admin(Usuario):
    """Un usuario con privilegios administrativos."""

    def __init__(self, nombre, apellido, **user_info):
        super().__init__(nombre, apellido, **user_info)
        self.privilegios = Privilegios()


jimmy = Admin('jimmy', 'floyd', correo='james_5226@hotmail.com', edad=30, altura=176)
jimmy.describir_usuario()

jimmy.privilegios.mostrar_privilegios()
print("\nAñadiendo privilegios...")
jimmy_privilegios = [
    'restablecer contraseñas',
    'moderar debates',
    'suspender cuentas',
    'hacer shadow-banning',
    ]

jimmy.privilegios.privilegios = jimmy_privilegios
jimmy.privilegios.mostrar_privilegios()