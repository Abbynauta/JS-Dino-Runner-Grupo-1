from turtle import width
import pygame 
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG,DEFAULT_TYPE, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, FPS, SHIELD_TYPE, TITLE, RUNNING
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        mixer.init()
        #self.sound = pygame.mixer.Sound([0])
        #self.sound = pygame.mixer.Sound([1])
        
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = PlayerHeartManager()
        
        self.death_count = 0
        self.score = Score()
        
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        
        pygame.quit()
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
    def reset_game(self):
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        self.score.restart_score()
        self.power_up_manager.reset_power_ups()
        self.heart_manager.reset_hearts()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.score.score)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.heart_manager.draw(self.screen)
        self.draw_power_up_active()
        
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def msg_menu(self,message,width,height):
        font = pygame.font.Font(FONT_STYLE, 30)
        text_component = font.render(message, True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text_component, text_rect)
    
    def show_menu(self):
        self.screen.fill((255,255,255)) #Pintar ventana
        #mostrar mensaje de bienvenida
        height = SCREEN_HEIGHT // 2 
        width = SCREEN_WIDTH // 2
       # self.sound[0].play()
        if self.death_count == 0:
           self.msg_menu("Press any Key to Start",width, height)
        else:
           #MENSAJE DE VOLVER A JUGAR
           self.msg_menu("Play Again",width, height)
           #mostrar score
           self.msg_menu(f'Your Score is: {self.score.score}',width, height + 50)
           #numero de muertes
           self.msg_menu(f'Number of deaths: {self.death_count}',width, height + 100)
        #mostrar icono
        self.screen.blit(RUNNING[0],(width -25, height -140) )
        #actualizar ventana
        pygame.display.update()
        #escuchar eventos
        self.handle_key_events_on_menu()
        
    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
            
    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE
        is_invincible = has_shield or self.heart_manager.heart_count > 0
        if not has_shield:
            self.heart_manager.reduce_heart()
            
        if not is_invincible:
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1
        
        return is_invincible
        
    def draw_power_up_active(self):
        height = SCREEN_HEIGHT // 2 
        width = SCREEN_WIDTH // 2
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0:
                self.msg_menu(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.",
                              self.screen, width-50,height-260)
            else:
             self.player.has_power_up = False
             self.player.type = DEFAULT_TYPE  