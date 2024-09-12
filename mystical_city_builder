import pygame
import sys
import gameloop

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mystical City Builder")

# Set the logo as the window icon
logo_image = pygame.image.load('logo.png')
pygame.display.set_icon(logo_image)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (128, 0, 128)  # PURPLE
BUTTON_HOVER_COLOR = (255, 165, 0)  # ORANGE

# Load images
background_main = pygame.image.load('background_main.jpeg')
background_character = pygame.image.load('background_character.jpeg')
background_new_game = pygame.image.load('background_new_game.jpeg')
background_status = pygame.image.load('background_status.jpeg')
background_mandi = pygame.image.load('background_mandi1.jpeg')
background_play = pygame.image.load('background_play.jpeg')  # New background for play scene

def background_image(image):
    size = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(size, (0, 0))

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback, image=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = BUTTON_COLOR
        self.image = image

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            font = pygame.font.Font(None, 36)
            text_surf = font.render(self.text, True, WHITE)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def check_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.color = BUTTON_HOVER_COLOR
        else:
            self.color = BUTTON_COLOR

# Button callbacks
def character_button():
    global current_scene
    current_scene = "character_selection"

def new_game_button():
    global current_scene
    current_scene = "new_game"

def status_button():
    global current_scene
    current_scene = "status"

def mandi_button():
    global current_scene
    current_scene = "mandi"

def exit_button():
    print("exit")
    pygame.quit()
    sys.exit()

def back_to_menu_button():
    global current_scene
    current_scene = "main_menu"

# Game loop callback
def play_button():
    global current_scene
    current_scene = "play_scene"
    gameloop.game()

# Create buttons
buttons = [
    Button("CHARACTER", 350, 200, 200, 50, character_button),
    Button("PLAY", 350, 260, 200, 50, new_game_button),
    Button("STATUS", 350, 320, 200, 50, status_button),
    Button("MANDI", 350, 380, 200, 50, mandi_button),
    Button("EXIT", 350, 440, 200, 50, exit_button),
]

# Character selection buttons
character_selection_buttons = [
    Button("BACK TO MENU", 350, 400, 200, 50, back_to_menu_button),
    Button("EXIT", 350, 500, 200, 50, exit_button),
]

# New game buttons
new_game_buttons = [
    Button("PLAY", 350, 200, 200, 50, play_button),
    Button("BACK", 350, 350, 200, 50, back_to_menu_button),
    Button("EXIT", 350, 500, 200, 50, exit_button),
]

# Status buttons
status_buttons = [
    Button("KARMA POINTS", 350, 500, 200, 50, back_to_menu_button),
    Button("COINS", 350, 500, 200, 50, back_to_menu_button),
    Button("REPOSITORIES", 350, 500, 200, 50, back_to_menu_button),
    Button("BACK", 350, 400, 200, 50, back_to_menu_button),
    Button("EXIT", 350, 500, 200, 50, exit_button),
]

# Mandi buttons
mandi_buttons = [
    Button("BACK", 350, 400, 200, 50, back_to_menu_button),
    Button("EXIT", 350, 500, 200, 50, exit_button),
]

# Play scene buttons
play_scene_buttons = [
    Button("BACK", 350, 400, 200, 50, back_to_menu_button),
    Button("EXIT", 350, 500, 200, 50, exit_button),
]

current_scene = "main_menu"
characters = [
    pygame.image.load('character..webp'),
    pygame.image.load('monster.png'),
]
def mystical():
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if current_scene == "main_menu":
                    for button in buttons:
                        if button.is_clicked(pos):
                            button.callback()
                elif current_scene == "character_selection":
                    for button in character_selection_buttons:
                        if button.is_clicked(pos):
                            button.callback()
                elif current_scene == "new_game":
                    for button in new_game_buttons:
                        if button.is_clicked(pos):
                            button.callback()
                elif current_scene == "status":
                    for button in status_buttons:
                        if button.is_clicked(pos):
                            button.callback()
                elif current_scene == "mandi":
                    for button in mandi_buttons:
                        if button.is_clicked(pos):
                            button.callback()
                elif current_scene == "play_scene":
                    for button in play_scene_buttons:
                        if button.is_clicked(pos):
                            button.callback()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if current_scene == "main_menu":
                    for button in buttons:
                        button.check_hover(pos)
                elif current_scene == "character_selection":
                    for button in character_selection_buttons:
                        button.check_hover(pos)
                elif current_scene == "new_game":
                    for button in new_game_buttons:
                        button.check_hover(pos)
                elif current_scene == "status":
                    for button in status_buttons:
                        button.check_hover(pos)
                elif current_scene == "mandi":
                    for button in mandi_buttons:
                        button.check_hover(pos)
                elif current_scene == "play_scene":
                    for button in play_scene_buttons:
                        button.check_hover(pos)

        if current_scene == "main_menu":
            background_image(background_main)
            for button in buttons:
                button.draw(screen)
        elif current_scene == "character_selection":
            background_image(background_character)
            for i, character in enumerate(characters):
                screen.blit(character, (350, 200 + i * 100))
            for button in character_selection_buttons:
                button.draw(screen)
        elif current_scene == "new_game":
            background_image(background_new_game)
            for button in new_game_buttons:
                button.draw(screen)
        elif current_scene == "status":
            background_image(background_status)
            for button in status_buttons:
                button.draw(screen)
        elif current_scene == "mandi":
            background_image(background_mandi)
            for button in mandi_buttons:
                button.draw(screen)
        elif current_scene == "play_scene":
            background_image(background_play)
        # Add code for play scene here
            for button in play_scene_buttons:
                button.draw(screen)

        pygame.display.flip()

    pygame.quit()
