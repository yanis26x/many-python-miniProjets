import pygame

def load_images(character, WORLD_WIDTH, HEIGHT):
    """Charge et retourne les images du jeu en fonction du personnage choisi."""
    background_img = pygame.image.load("./IMG/background.jpg")
    background_img = pygame.transform.scale(background_img, (WORLD_WIDTH, HEIGHT))

    if character == "amy":
        player_img = pygame.image.load("./IMG/amy.png")
    else:
        player_img = pygame.image.load("./IMG/sonic.png")
    
    player_img = pygame.transform.scale(player_img, (40, 50))
    
    ring_img = pygame.image.load("./IMG/ring.png")
    ring_img = pygame.transform.scale(ring_img, (20, 20))
    
    enemy_img = pygame.image.load("./IMG/enemy.png")
    enemy_img = pygame.transform.scale(enemy_img, (40, 40))

    goal_img = pygame.image.load("./IMG/goal.webp")  # Charger l'image de fin de niveau


    enemy2_img =pygame.image.load("./IMG/silver.png")
    enemy2_img = pygame.transform.scale(enemy2_img, (40, 50))

    boss_img =pygame.image.load("./IMG/boss1.png")
    boss_img = pygame.transform.scale(boss_img, (100, 100))

 

    
    return background_img, player_img, ring_img, enemy_img,goal_img,enemy2_img, boss_img
