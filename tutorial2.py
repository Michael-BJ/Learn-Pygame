import pygame

# instalasi
pygame.init()

# mengatur ukuran layar/screen

height = 600
width = 600

screen = pygame.display.set_mode([height, width])

# Mengubah title screen
pygame.display.set_caption("Tutorial 2")

# memuat dan menggati logo/icon screen
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# mengubah warna screen
screen.fill((255, 255,255))

# memambahkan gambar
image = pygame.image.load("plane.png")
screen.blit(image,(100,300))

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()

pygame.quit()