class GameStats:
    '''Sigue las estadisticas de alien invasion'''
    def __init__(self, ai_game):
        '''Inicializa las estadísticas'''
        self.settings = ai_game.settings
        self.reset_stats()
        #Inicia alien invasion en estado activo
        self.game_active = True
    
    def reset_stats(self):
        '''Inicializa las estadisiticas que pueden cambiar durante el juego'''
        self.ships_left = self.settings.ship_limit