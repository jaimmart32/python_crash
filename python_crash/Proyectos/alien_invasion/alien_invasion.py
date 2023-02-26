import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y sus recursos."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")       

    
    def run_game(self):
        """Inicializa el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #accedemos al color de la pantalla de fond, para redibujar la pantalla en cada paso por el bucle
            self.screen.fill(self.bg_color)        
            
            pygame.display.flip()


if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()

