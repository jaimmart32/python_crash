class Settings:
    '''Una clase para guardar toda la configuración de alien invasion'''

    def __init__(self):
        '''Inicializa las configuaracines estáticas del juego.'''

        # Configuraciń de la pantalla
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuarción de la nave.
        self.ship_limit = 3

        #Configuración de las balas
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #Configuraciuon del alien
        self.fleet_drop_speed = 10
        

        # Rapidez con la que se acelera el juego.
        self.speedup_scale = 1.3

        # Lo rápido que aumenta el valor de en puntos de los aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Inicializa las configuraciones que cambian durante el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction de 1 representa derecha; -1 representa izquierda.
        self.fleet_direction = 1

        # Puntuación.
        self.alien_points = 5
    
    def increase_speed(self):
        """Incrementa las configuraciones de velocidad(dificultad del juego) y 
        los valores en puntos de los aliens abatidos."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
    





        