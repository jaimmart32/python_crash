import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y sus recursos."""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    
    def run_game(self):
        """Inicializa el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y ratón
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            # Accedemos al color de la pantalla de fond, para redibujar la pantalla en cada paso por el bucle
            self._update_screen()
            
            
            
    
    def _check_events(self):
        """Responde a pulsaciones de teclas y ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event) 
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    
    def _check_keydown_events(self, event):
        """Responde a pulsaciones de tecla."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
            
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    
        
    
    
    def _fire_bullet(self):
        """Crea una bala nueva y la añade al grupo de balas"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                   

    
    
    
    def _update_bullets(self):
        """Actualioza la posición de las balas y de deshace de las viejas"""
        # Actualiza la posiución de las balas
        self.bullets.update()

        # Se deshace de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #Busca las balas que hayan dado a aliens
        # Si hay, se deshace el alien y la bala
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #Destruye balas existentes y crea una flota nueva.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self): 
        '''Actualiza la posicion de todos los aliens de la flota'''
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Crea la flota de aliens."""
        # Cra un alien y halla el numero de aliens en unas fila.
        # El espacio entre alien es gual a la anchura de un aliens.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determina el numero de filas de aliens que caben en la pantalla.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        #Crea la flota de aliens
        for row_number in range (number_rows):
            for alien_number in range  (number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        ''' Crea un alien y lo coloca en la fila'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x =alien.x
        alien.rect.y = alien.rect.height  + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def _update_screen(self):
        """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()

