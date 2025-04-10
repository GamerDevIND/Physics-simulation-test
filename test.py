import pygame
from math import *

pygame.init()

pygame.display.set_caption("E")
screen = pygame.display.set_mode((1000,600))

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 24)

point0 = pygame.Vector2(100,50)

trails = []

velocity = pygame.Vector2(0,0)
init_velocity = velocity.copy()

acceleration_scaler = 5
acceleration_scaler_var = acceleration_scaler
damping  = 0.9

main_loop = True
while main_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

    dt = clock.tick(60) / 1000

    dt *= 10

    mouse = pygame.Vector2(pygame.mouse.get_pos())

    screen.fill((25,25,25))

    direction = point0 - mouse

    screen.blit(font.render(f"Distance: {direction.length():.2f}\nSpeed: {velocity.length():.2f}\nMouse: {mouse.x} / {mouse.y}\nFPS: {int(clock.get_fps())}", True, "white"), (50, 50))

    if direction.length() > 5:
        acceleration = direction.normalize()  * acceleration_scaler_var
        acceleration_scaler_var += 0.01
    else: 
        acceleration = pygame.Vector2(0,0)
        acceleration_scaler_var = acceleration_scaler

    velocity += acceleration

    velocity *= damping

    trails.append(point0.copy())

    point0 -= velocity * dt

    if pygame.mouse.get_pressed()[0]:
        point0 = mouse.copy()
        velocity = pygame.Vector2(0,0)
        acceleration = pygame.Vector2(0,0)

    if len(trails) > 20:
        trails.pop(0)
    
    for i, p in enumerate(trails):
        alpha = int(255 * (i / len(trails)))
        pygame.draw.circle(screen, (alpha, alpha, alpha), p, 2)

    pygame.draw.circle(screen, "white", point0, 3, 1)
    # pygame.draw.line(screen, "green", point0, mouse, 3)

    pygame.display.flip()

pygame.quit()
