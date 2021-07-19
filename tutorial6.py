import pygame
import random
import math
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

# lives
lives = 3
font = pygame.font.Font('freesansbold.ttf', 16)

def show_lives(x,y):
    x_lives = 10
    y_lives = 10
    lives_number = font.render("Lives :" + str(lives), True, (255,255,255))
    screen.blit(lives_number,(x_lives,y_lives))

# musuh
def enemy(x,y):
    image = pygame.image.load("enemy.png")
    screen.blit(image,(x_enemy,y_enemy))

x_enemy = random.randint(0,600)
y_enemy = random.randint(0,600)

x_point_enemy = 0
y_point_enemy = 0

# tabrakan 
def collison(x,y,x_enemy,y_enemy):
    distance = math.sqrt(math.pow(x-x_enemy,2) + (math.pow(y-y_enemy,2)))
    if distance <70:
        return True
    else:
        return False

running = True
while running:
    # mengubah warna screen
    screen.fill((255, 255,255))
    # menambhkan background
    screen.blit(background, (0,0))
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 1
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 1
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 1

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

    x += x_point
    y += y_point

    # tabrakan
    tabrakan = collison(x,y,x_enemy,y_enemy)
    if tabrakan:
        lives -= 1
    else:
        lives += 0
    
    # game over
    if lives <= 0:
        break

    #menampilksn lives
    show_lives(x,y)

    # menampilkan gambar ke dalam screen 
    plane(x,y)
    # menampilkan musuh
    enemy(x,y)
    pygame.display.update()

pygame.quit()