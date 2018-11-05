import pygame

from scene import Scene

pygame.init()

size = (720, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("gotoFood")
pygame.display.flip()


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


done = False
clock = pygame.time.Clock()

scene = Scene(720, 480)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    for agent in scene.agents:
        agent.move(scene)

    # Draw all agents
    for agent in scene.agents:
        pygame.draw.circle(screen, BLUE, [int(agent.x), int(agent.y)], 5)

    # Draw all food
    for food in scene.food:
        pygame.draw.circle(screen, RED, [food.x, food.y], 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()