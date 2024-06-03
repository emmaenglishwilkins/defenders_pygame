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
        sb = myfont.render("Score: " + str(self.score) + " Lives: " + str(self.lives), 1, (255, 255, 255))
        screen.blit(sb, (200, 10))

    def gameover(self, screen):
        gb = myfont.render("Game Over", 1, (255, 0, 0))
        screen.blit(gb, (200, 300))

    def update_score(self):
        self.score += 1

def check_bullet_enemy_collision(bullets, enemy, game, screen):
    for bullet in bullets:
        if bullet.rect.colliderect(enemy.rect):
            bullets.remove(bullet)
            enemy.reset_postion()
            game.update_score()
            break

def main():
    screen = pygame.display.set_mode((800, 600))
    game = Game(screen)
    xdir = 0
    bullets = []

    clock = pygame.time.Clock()

    while True:
        screen.fill((50, 50, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xdir = 1
                elif event.key == pygame.K_LEFT:
                    xdir = -1
                elif event.key == pygame.K_SPACE:
                    bullets.append(game.player.shoot())
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    xdir = 0

        if game.lives > 0:
            game.update(xdir)

            for bullet in bullets:
                bullet.update()
                bullet.draw(screen)

            check_bullet_enemy_collision(bullets, game.enemy, game, screen)
        else:
            game.gameover(screen)

        game.scoreboard(screen)
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS

main()
