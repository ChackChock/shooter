import pygame

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load("images\\background.png")
background = pygame.transform.scale(background, (800, 600))
player = pygame.image.load("images\\player.png")
enemy = pygame.image.load("images\\enemy.png")
bullet = pygame.image.load("images\\bullet.png")

game = True
while game:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # Обновление объектов игры

    # Отрисовка
    window.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
