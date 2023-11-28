import pygame

pygame.init()
X = 450
Y = 450

scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption("CheckersBot Pro AI")
imp = pygame.image.load("image_files/board.png")

scrn.blit(imp, (0, 0))

pygame.display.flip()
status = True
while status:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()
