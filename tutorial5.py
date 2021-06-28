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
enemy_img = pygame.image.load("enemy.png")
class Enemy():
    def __init__(self):
        self.x = random.randint(599,600)
        self.y = random.randint(0, 600)
        self.pointx =  -0.5
    
    def move(self):
        self.x += self.pointx

    def draw(self):
        screen.blit(enemy_img,(self.x, self.y))

enemy_list = []
for i in range(7):
    new_enemy = Enemy()
    enemy_list.append(new_enemy)

running = True
while running:
    # menambhkan background
    screen.blit(background, (0,0))
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

    
    x += x_point
    y += y_point

    # move and draw
    for enemy in enemy_list:
        enemy.move()
        enemy.draw()
    # menampilkan gambar ke dalam screen 
    plane(x,y)
    # menampilkan musuh
    pygame.display.update()

pygame.quit()