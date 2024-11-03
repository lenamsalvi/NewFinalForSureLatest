import pygame
import random

# Globals
REFERSH_RATE_HZ = 60

def open_window_with_button():
    # Initialize the pygame library
    pygame.init()

    # Set the dimensions of the window (width, height)
    window_size = (400, 300)
    screen = pygame.display.set_mode(window_size)

    # Set the window title
    pygame.display.set_caption("Plant Collage Generator")

    # Define initial button properties
    button_color = (100, 100, 255)  # Blue color
    button_width, button_height = 100, 30
    button_x, button_y = 150, 250
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Set up font for the button text
    font = pygame.font.Font(None, 24)

    # Refresh rate
    clock = pygame.time.Clock()

    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for window close event
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is inside the button's rectangle
                if button_rect.collidepoint(event.pos):
                    # Move the button to a random location
                    button_rect.x = random.randint(0, window_size[0] - button_width)
                    button_rect.y = random.randint(0, window_size[1] - button_height)

        # Fill the screen with a color (RGB) - white in this case
        screen.fill((50, 50, 50))

        # Draw the button
        pygame.draw.rect(screen, button_color, button_rect)

        # Render the button text and blit it to the screen
        text_surface = font.render("Click Me", True, (255, 255, 255))  # White text color
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

        # Update the display
        pygame.display.flip()
        clock.tick(REFERSH_RATE_HZ)

    # Quit pygame
    pygame.quit()

# Call the function to open the window
open_window_with_button()
