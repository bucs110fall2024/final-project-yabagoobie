import pygame
#import your controller
from controller import Controller

def main():
    pygame.init()
    #Create an instance on your controller object
    controller_object = Controller()
    #Call your mainloop
    controller_object.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
