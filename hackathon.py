import pygame
import sys
import mystical_city_builder_1
import gameloop
import puzzle
import guess_movie
import celebrity

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CIRCLE_RADIUS = 50

# Load images
image_paths = ['circular1.png', 'circular2.png', 'circular3.png', 'circular4.png']
images = [pygame.image.load(img) for img in image_paths]

# Resize images to fit in circles
images = [pygame.transform.scale(img, (CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)) for img in images]

# Load background images
background_image = pygame.image.load('background.jpeg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
scene1_background = pygame.image.load('background_character.jpeg')
scene1_background = pygame.transform.scale(scene1_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
scene2_background = pygame.image.load('background_character.jpeg')
scene2_background = pygame.transform.scale(scene2_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
scene3_background = pygame.image.load('background_mandi.jpeg')
scene3_background = pygame.transform.scale(scene3_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
scene4_background = pygame.image.load('background_mandi1.jpeg')
scene4_background = pygame.transform.scale(scene4_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load individual scene backgrounds for unique buttons
chat_background = pygame.image.load('111.jpeg')
chat_background = pygame.transform.scale(chat_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

puzzle_background = pygame.image.load('111.jpeg')
puzzle_background = pygame.transform.scale(puzzle_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

city_builder_background = pygame.image.load('111.jpeg')
city_builder_background = pygame.transform.scale(city_builder_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

famous_personalities_background = pygame.image.load('111.jpeg')
famous_personalities_background = pygame.transform.scale(famous_personalities_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

movies_background = pygame.image.load('111.jpeg')
movies_background = pygame.transform.scale(movies_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

memes_background = pygame.image.load('111.jpeg')
memes_background = pygame.transform.scale(memes_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MOOD QUEST')

# Font setup
font = pygame.font.Font(None, 36)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, image=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = PURPLE
        self.image = image

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        if self.image:
            # Draw circular icon with image above the button
            img_rect = self.image.get_rect(center=(self.rect.centerx, self.rect.top - CIRCLE_RADIUS - 10))
            pygame.draw.circle(screen, BLACK, img_rect.center, CIRCLE_RADIUS)
            screen.blit(self.image, img_rect.topleft)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Create buttons
menu_buttons = [
    Button('SAD', 100, 300, 150, 50, images[0]),
    Button('NORMAL', 250, 300, 150, 50, images[1]),
    Button('HAPPY', 400, 300, 150, 50, images[2]),
    Button('LOVELY', 550, 300, 150, 50, images[3]),
    Button('Exit', 350, 500, 150, 50)
]

# Scene-specific buttons
scene_buttons = {
    'scene1': [
        Button('Back to Menu', 300, 400, 200, 50),
        Button('Exit', 300, 500, 200, 50),
        Button('Chat with People', 300, 300, 200, 50)  # Leads to Chat Scene
    ],
    'scene2': [
        Button('Back to Menu', 300, 400, 200, 50),
        Button('Exit', 300, 500, 200, 50),
        Button('Puzzle', 100, 300, 200, 50),  # Leads to Puzzle Scene
        Button('Mystical City Builder', 400, 300, 300, 50)  # Opens Mystical City Builder Script
    ],
    'scene3': [
        Button('Back to Menu', 300, 400, 200, 50),
        Button('Exit', 300, 500, 200, 50),
        Button('Chat with People', 100, 300, 200, 50),  # Leads to Chat Scene
        Button('Mystical City Builder', 400, 300, 300, 50)  # Opens Mystical City Builder Script
    ],
    'scene4': [
        Button('Back to Menu', 300, 500, 200, 50),
        Button('Exit', 300, 600, 200, 50),
        Button('Famous Personalities', 100, 300, 300, 50),  # Leads to Famous Personalities Scene
        Button('Movies', 450, 300, 200, 50),  # Leads to Movies Scene
        Button('Memes', 300, 400, 200, 50)  # Leads to Memes Scene
    ]
}

# Individual buttons for new scenes
new_scenes_buttons = {
    'chat_scene': [
        Button('Back to Menu', 300, 400, 200, 50)
    ],
    'puzzle_scene': [
        Button('Back to Menu', 300, 400, 200, 50)
    ],
    'city_builder_scene': [
        Button('Back to Menu', 300, 400, 200, 50)
    ],
    'famous_personalities_scene': [
        Button('Back to Menu', 300, 400, 200, 50)
    ],
    'movies_scene': [
        Button('Back to Menu', 300, 400, 200, 50)
    ],
    'memes_scene': [
        Button('Back to Menu', 300, 400, 200, 50)
    ]
}

# Backgrounds for new scenes
backgrounds = {
    'scene1': scene1_background,
    'scene2': scene2_background,
    'scene3': scene3_background,
    'scene4': scene4_background,
    'chat_scene': chat_background,
    'puzzle_scene': puzzle_background,
    'city_builder_scene': city_builder_background,
    'famous_personalities_scene': famous_personalities_background,
    'movies_scene': movies_background,
    'memes_scene': memes_background
}

# Main loop
running = True
current_scene = 'menu'

while running:
    mouse_pos = pygame.mouse.get_pos()

    if current_scene == 'menu':
        screen.blit(background_image, (0, 0))

        # Draw menu buttons
        for button in menu_buttons:
            if button.is_hovered(mouse_pos):
                button.color = ORANGE
            else:
                button.color = PURPLE
            button.draw(screen)

    else:
        screen.blit(backgrounds[current_scene], (0, 0))
        # Draw buttons for current scene
        if current_scene in scene_buttons:
            for button in scene_buttons[current_scene]:
                if button.is_hovered(mouse_pos):
                    button.color = ORANGE
                else:
                    button.color = PURPLE
                button.draw(screen)
        elif current_scene in new_scenes_buttons:
            for button in new_scenes_buttons[current_scene]:
                if button.is_hovered(mouse_pos):
                    button.color = ORANGE
                else:
                    button.color = PURPLE
                button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_scene == 'menu':
                for i, button in enumerate(menu_buttons):
                    if button.is_hovered(mouse_pos):
                        if button.text == 'Exit':
                            running = False
                        else:
                            current_scene = f'scene{i+1}'
            else:
                if current_scene in scene_buttons:
                    for button in scene_buttons[current_scene]:
                        if button.is_hovered(mouse_pos):
                            if button.text == 'Exit':
                                running = False
                            elif button.text == 'Back to Menu':
                                current_scene = 'menu'
                            elif button.text == 'Chat with People':
                                current_scene = 'chat_scene'
                            elif button.text == 'Puzzle':
                                puzzle.puzzle()
                            elif button.text == 'Mystical City Builder':
                                mystical_city_builder_1.mystical()
                            elif button.text == 'Famous Personalities':
                                celebrity.celeb()
                            elif button.text == 'Movies':
                                guess_movie.movie_guess_game()
                            elif button.text == 'Memes':
                                current_scene = 'memes_scene'
                elif current_scene in new_scenes_buttons:
                    for button in new_scenes_buttons[current_scene]:
                        if button.is_hovered(mouse_pos):
                            if button.text == 'Back to Menu':
                                current_scene = 'menu'

    pygame.display.flip()

pygame.quit()
sys.exit()
