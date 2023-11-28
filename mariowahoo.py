import pygame

pygame.init()  # Initialize Pygame

width, height = 800, 600  # Set window dimensions
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FLAMES64")  # Set window title

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)

# Function to render text
def render_text(surface, text, font_size, position, color=WHITE):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    surface.blit(text_surface, text_rect)

# Function to draw checkered pattern
def draw_checkered_pattern(surface, rect, tile_size):
    colors = [GRAY, WHITE]
    for y in range(rect.top, rect.bottom, tile_size):
        for x in range(rect.left, rect.right, tile_size):
            square = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(
                surface, colors[(x // tile_size) % 2 != (y // tile_size) % 2], square)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Space key pressed
                # Proceed to start the game
                print("Start the game...")

    # Clear the screen
    screen.fill(BLACK)

    # Draw the checkered pattern in the center
    checkered_rect = pygame.Rect(width // 4, height // 3, width // 2, height // 3)
    draw_checkered_pattern(screen, checkered_rect, 40)

    # Render the GUI text
    render_text(screen, "FLAMES64", 90, (width // 2, 100))
    render_text(screen, "Select Your Plumber", 50, (width // 2, 200))
    render_text(screen, "Press Space to Start", 40, (width // 2, height - 50))

    # Draw M and L boxes within the checkered area
    m_box_rect = pygame.Rect(
        checkered_rect.left + 60, checkered_rect.centery - 50, 100, 100)
    l_box_rect = pygame.Rect(
        checkered_rect.right - 160, checkered_rect.centery - 50, 100, 100)
    pygame.draw.rect(screen, RED, m_box_rect)
    pygame.draw.rect(screen, GREEN, l_box_rect)
    render_text(screen, "M", 80, m_box_rect.center, BLACK)
    render_text(screen, "L", 80, l_box_rect.center, BLACK)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
