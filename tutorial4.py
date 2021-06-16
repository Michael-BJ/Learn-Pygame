import pygame
import random

# instalasi
pygame.init()

# mengatur ukuran layar/screen

height = 600
width = 600

screen = pygame.display.set_mode([height, width])

# Mengubah title screen
pygame.display.set_caption("Tutorial 3")

# memuat dan menggati logo/icon screen
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# menambahkan background
background = pygame.image.load("background.jpg")

def plane(x,y):
    image = pygame.image.load("plane.png")
    screen.blit(image,(x,y))

x = 100
y = 300

x_point = 0
y_point = 0

# musuh
def enemy(x,y):
    image = pygame.image.load("enemy.png")
    screen.blit(image,(x_enemy,y_enemy))

x_enemy = random.randint(0,600)
y_enemy = random.randint(0,600)

x_point_enemy = 0
y_point_enemy = 0

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 0.5
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 0.5
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 0.5
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point = 0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point = 0

        # Batasan
        if x <= 0:	
            x = 0
        elif x>= 525:
            x= 525
        if y <= 0:
            y =0 
        elif y>= 550:
            y = 550   

    # mengubah warna screen
    screen.fill((255, 255,255))
    # menambhkan background
    screen.blit(background, (0,0))
    
    x += x_point
    y += y_point

    # menampilkan gambar ke dalam screen 
    plane(x,y)
    # menampilkan musuh
    enemy(x,y)
    pygame.display.update()

pygame.quit()