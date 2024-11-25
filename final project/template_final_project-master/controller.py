from enemy import Enemy
from player import Player
import pygame

class Controller:
    
    def __init__(self):
        '''
        Initilizes objects and resources required to run your program
        args: none
        return: none
        ''' 
    
    def mainloop(self):
        """
        docstring
        """
        while(True): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()