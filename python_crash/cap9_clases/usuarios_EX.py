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


user_0 = Usuario('jaime', 'martinez', correo='james_5226@hotmail.com', edad=30)
user_1 = Usuario('pablo', 'mora', correo='moradin3@hotmail.com', edad=92)
user_2 = Usuario('miguel', 'arias', correo='ariaskillo@hotmail.com', edad=30)

user_0.describir_usuario()
user_0.saludar_usuario()

user_1.describir_usuario()
user_1.saludar_usuario()

user_2.describir_usuario()
user_2.saludar_usuario()

#9.5

usuario = Usuario('adin', 'ros', correo='adin_5226@hotmail.com', edad=18)
usuario.incrementar_intentos_inicio(1)
usuario.incrementar_intentos_inicio(2)
print(usuario.intentos_inicio)
usuario.incrementar_intentos_inicio(3)
print(usuario.intentos_inicio)
usuario.restablecer_intentos_inicio()
print(usuario.intentos_inicio)