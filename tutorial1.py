import pygame

# instalasi
pygame.init()

# mengatur ukuran layar/screen

height = 600
width = 600

screen = pygame.display.set_mode([height, width])

# mengubah warna screen
screen.fill((255, 0,0))

# membuat lingkaran
pygame.draw.line(screen, (0,0,255),(100,100),(300,300),75)

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()

pygame.quit()
