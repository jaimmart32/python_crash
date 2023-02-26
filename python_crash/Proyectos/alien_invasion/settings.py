
class Settings:
    '''Una clase para guardar toda la configuración de alien invasion'''

    def __init__(self):
        '''Inicializa la configuaración dle juego'''

        # Configuraciń de la pantalla
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuarción de la nave.
        self.ship_speed = 1.5

        