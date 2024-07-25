import pygame

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My first Pygame window")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_h:
                print("H key pressed")
            elif event.key == pygame.K_j:
                print("J key pressed")
            elif event.key == pygame.K_k:
                print("K key pressed")
            elif event.key == pygame.K_l:
                print("L key pressed")
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
    pygame.display.update()

pygame.quit()
