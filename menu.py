import pygame
import sys

pygame.init()

#Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu - Sonic 26x")

#Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
PINK = (255, 105, 180)
GRAY = (100, 100, 100)

#Charger l'image de fond avec opacité
background_img = pygame.image.load("./IMG/sang.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
background_img.set_alpha(204)  # 80% d'opacité (255 * 0.8 = 204)

#Charger les images des personnages
sonic_img = pygame.image.load("./IMG/sonic.png")
sonic_img = pygame.transform.scale(sonic_img, (100, 120))

amy_img = pygame.image.load("./IMG/amy.png")
amy_img = pygame.transform.scale(amy_img, (100, 120))

# Boutons
sonic_button = pygame.Rect(200, 250, 150, 150)
amy_button = pygame.Rect(450, 250, 150, 150)
start_button = pygame.Rect(300, 450, 200, 60)

#Variables de sélection
selected_character = "sonic"  # Par défaut, Sonic est sélectionné

# 🎮 Boucle du menu
running = True
while running:
    screen.fill(WHITE)  # Fond blanc
    screen.blit(background_img, (0, 0))  # Affiche l'image avec 80% d'opacité

    #Affichage des personnages et boutons
    pygame.draw.rect(screen, BLUE if selected_character == "sonic" else GRAY, sonic_button, border_radius=20)
    pygame.draw.rect(screen, PINK if selected_character == "amy" else GRAY, amy_button, border_radius=20)
    pygame.draw.rect(screen, (0, 255, 0), start_button, border_radius=10)

    screen.blit(sonic_img, (225, 260))  # Affiche Sonic
    screen.blit(amy_img, (475, 260))  # Affiche Amy

    #Texte
    font = pygame.font.Font(None, 40)
    title_text = font.render("Choisi ton persoo!", True, (0, 0, 0))
    screen.blit(title_text, (220, 100))

    start_text = font.render("START", True, (255, 255, 255))
    screen.blit(start_text, (350, 465))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Sélection de Sonic
            if sonic_button.collidepoint(mouse_x, mouse_y):
                selected_character = "sonic"

            # Sélection de Amy
            elif amy_button.collidepoint(mouse_x, mouse_y):
                selected_character = "amy"

            # Bouton START
            elif start_button.collidepoint(mouse_x, mouse_y):
                running = False  # Quitte le menu et lance le jeu

    pygame.display.flip()  # Mise à jour de l'affichage

#Lancer `main.py` avec le personnage sélectionné
import subprocess
subprocess.run(["python", "main.py", selected_character])
