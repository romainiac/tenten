import pygame, sys

class GameManager:
    def __init__(self):
        self.running = True
        pygame.init()
    
    def end_game(self):
        self.running = False

    def stop(self):
        pygame.quit()
        sys.exit()