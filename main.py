import pygame
from player import Player
from enemy import Enemy

pygame.init()
myfont = pygame.font.SysFont("freeserif", 48)

class Game:
    def __init__(self, screen):
        self.player = Player(screen)
        self.enemy = Enemy(screen)
        self.score = 0
        self.lives = 5

    def update(self, xdir):
        self.player.draw()
        self.player.move(xdir)
        self.enemy.draw()
        self.enemy.move(self.player, self)

    def scoreboard(self, screen):
        sb = myfont.render("Score: " + str(self.score) + " Lives: " + str(self.lives), 1, (255, 255,255))
        screen.blit(sb, (200, 10))

    def gameover(self, screen):
        gb = myfont.render("Game OVer", 1, (255, 0, 0))
        screen.blit(gb, (200, 300))
def main():
    screen = pygame.display.set_mode((800, 600))
    game = Game(screen)
    xdir = 0

    while True:
        screen.fill((50, 50, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x = 1
                elif event.key == pygame.K_LEFT:
                    x = -1
            elif event.type == pygame.KEYUP:
                xdir = 0

        if game.lives > 0:
            game.update(xdir)
        else:
            game.gameover(screen)

        game.scoreboard(screen)
        pygame.display.update()
main()