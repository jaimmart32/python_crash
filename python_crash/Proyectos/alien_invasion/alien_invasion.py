import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

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

        #Crea una instancia para guardar las estadisticas del juego.
        self.stats =  GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Hace el botón Play.
        self.play_button = Button(self, "Play")

    
    def run_game(self):
        """Inicializa el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y ratón
            self._check_events()
            if self.stats.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Inicia un juego nuevo cuando el jugador hace click en Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Restablece las estadisticas del juego.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Se deshace de los aliensy las balas que quedan.
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y la centra la nave.
            self._create_fleet()
            self.ship.center_ship()

            # Oculta el cursor del ratón.
            pygame.mouse.set_visible(False)
                
    
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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
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

        #Busca colision entre alien y nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("Eres un paquet!!")

        #Busca aliens llegando al fondo de la pantalla 
        self._check_aliens_bottom()

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

        # Dibuja el botón Play si el juego esta activo.
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _ship_hit(self):
        '''Responde impacto alien y nave'''
        if self.stats.ships_left > 0:
            # Disminuye ships left
            self.stats.ships_left -= 1

            #Se deshace de los aliens y balas restantes
            self.aliens.empty()
            self.bullets.empty()

            #Crea flota nueva y centra la nave
            self._create_fleet()
            self.ship.center_ship()

            #Pausa
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        '''Comprueba si algun alien ha llegadop al fondo de la pantalla'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Trata esto como si la nave hubiese sido alcanzada
                self._ship_hit()
                break


if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()

