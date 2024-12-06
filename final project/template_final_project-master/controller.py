from enemy import Enemy
from player import Player
import pygame

class Controller:
    
    def __init__(self):
        '''
        Initilizes objects and resources required to run the program
        args: none
        return: none
        ''' 
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("arrows to move, space to attack")
        
        self.player = Player()
        self.enemy = Enemy()
        
    def mainloop(self):
        """
        the main functions of the program
        args: none
        return: none
        """
        
        while(True): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #2. detect collisions and update models
            self.player.move()
            self.player.attack()
            self.enemy.move(self.player.rect, self.player.player_mode)
            #3. Redraw next frame
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            self.background = pygame.image.load("assets/background.png")
            self.screen.blit(self.background, (0, 0))
            #4. Display next frame
            pygame.display.update()
            