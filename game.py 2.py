import pygame
import sys

# Initial Pygame
pygame.init()

# Screen dimensions
screen_width = 1000
screen_height = 1000

# Colors
blue = (0, 0, 225)
brown = (244, 164, 96)

# Create the Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

# Running Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill Screen
    screen.fill(blue)

    # Draw Brown Rectangle
    rectangle_height = 300
    pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))

    # Update Display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
