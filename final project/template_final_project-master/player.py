import pygame

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        '''
        Initializes the player
        args: none
        return: none
        ''' 
        self.image_file = pygame.image.load("assets/player.png")
        self.rect = self.image_file.get_rect()
        self.rect.x = 300
        self.rect.y = 200
        self.player_mode = False
        
    def move(self):
        '''
        Moves the player through inputs
        args: none
        return: none
        '''
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
            self.image_file = pygame.image.load("assets/player.png")
            self.player_mode = False
        if keys[pygame.K_RIGHT]: 
            self.rect.x += 2
            self.image_file = pygame.image.load("assets/player.png")
            self.player_mode = False
            
    def attack(self):
        '''
        controls if the player is attacking or not
        args: none
        return: none
        '''
        keys = pygame.key.get_pressed()  
        
        if keys[pygame.K_SPACE]: 
            self.image_file = pygame.image.load("assets/player_attack.png")
            self.player_mode = True

    def draw(self, screen):
        '''
        draws the player sprite on the screen
        args: screen - the pygame display
        return: none
        '''
        screen.blit(self.image_file, (self.rect.x, self.rect.y))
        pygame.display.flip()