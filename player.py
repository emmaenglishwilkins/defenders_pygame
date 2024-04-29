import pygame
class Player:
    def __init__(self, surface):
        img = pygame.image.load("emma_defender.png") # add name of player png file here
        self.img = pygame.transform.scale(img, (100, 100))
        self.rect = self.img.get_rect(center=(350, 500))
        self.surface = surface
        self.xdir = 0
        self.speed = 1
    def draw(self):
        self.surface.blit(self.img, self.rect)
    def move(self, xdir):
        self.rect.x += xdir * self.speed
        if self.rect.left < 0  or self.rect.right > 800:
            self.xdir =- self.xdir