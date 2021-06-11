import pygame

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


# memambahkan gambar
def plane(x,y):
    image = pygame.image.load("plane.png")
    screen.blit(image,(x,y))

x = 100
y = 300

x_point = 0
y_point = 0

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 0.1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 0.5
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 0.1
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point = 0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point = 0
            
    # mengubah warna screen
    screen.fill((255, 255,255))

    x += x_point
    y += y_point

    # menampilkan gambar ke dalam screen 
    plane(x,y)
    pygame.display.update()

pygame.quit()