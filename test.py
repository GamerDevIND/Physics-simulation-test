import pygame

pygame.init()

pygame.display.set_caption("E")
screen = pygame.display.set_mode((1000,600))

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 24)

point0 = pygame.Vector2(100,50)

velocity = pygame.Vector2(0,0)
init_velocity = velocity.copy()

acceleration_scaler = 5

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
        acceleration = direction.normalize().normalize()  * acceleration_scaler
    else: 
        acceleration = pygame.Vector2(0,0)

    velocity += acceleration

    velocity *= 0.9

    point0 -= velocity * dt

    pygame.draw.circle(screen, "white", point0, 3, 1)
    pygame.draw.line(screen, "green", point0, mouse, 3)

    pygame.display.flip()

pygame.quit()
