import pygame
import random
class Enemy:
    def __init__(self, surface):
        img = pygame.image.load("")
        self.img = pygame.transform.scale(100,100)
        self.rect = self.img.get_rect(center=(350,500))
        self.surface = surface
        self.speed = 1
    def draw(self):
        self.surface.blit(self.img, self.rect)
    def move(self, player, game):
        self.rect.y += self.speed
        if self.rect.y >= 600:
            self.rect.y = 0
            self.rect.x = random.randint(0,800)
        if self.rect.colliderect(player.rect):
            game.lives -= 1
            self.rect.y = 0
            self.rect.x = random.randint(0,800)