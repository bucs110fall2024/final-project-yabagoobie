import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes the enemy object
        args: none
        return: none
        '''    
        self.image_file = pygame.image.load("assets/enemy.png")
        self.rect = self.image_file.get_rect()
        self.rect.x = 800
        self.rect.y = 250
        
    def move(self, player_rect, player_mode):
        '''
        Gives the enemies the ability to move around the screen
        args: 
        plauer_rect: rect object - used to detect if the enemy and player collided
        return: none
        '''
        self.rect.x -= 3

        if self.rect.colliderect(player_rect):
            if player_mode == True:
                print("you hit the alien, good job")
                self.rect.x = 800
                self.rect.y = 250
            else:
                print("the alien hit you, bummer")
                self.rect.x = 800
                self.rect.y = 250
        
    def draw(self, screen):
        '''
        draws the enemy sprite on the screen
        args: screen - the pygame display
        return: none
        '''
        screen.blit(self.image_file, (self.rect.x, self.rect.y))
        pygame.display.flip()
        