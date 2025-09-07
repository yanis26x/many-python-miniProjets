import pygame
import sys
import random
from code_base_dun_niv import load_images

pygame.init()

WIDTH, HEIGHT = 1000, 400
WORLD_WIDTH = 6000
WHITE = (255, 255, 255)
COULEUR_SOL = (23, 32, 42)
GROUND_Y = HEIGHT - 50
MAX_SPEED = 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic 26x")

character = "sonic"
if len(sys.argv) > 1:
    character = sys.argv[1]

background_img, player_img, ring_img, enemy_img, goal_img, enemy2_img, boss_img = load_images(character, WORLD_WIDTH, HEIGHT)

jump_sound = pygame.mixer.Sound("./OST/jump.wav")
ring_sound = pygame.mixer.Sound("./OST/ring.wav")
hit_sound = pygame.mixer.Sound("./OST/hit.wav")
enemieMort_sound = pygame.mixer.Sound("./OST/enemieMORT.wav")

player = pygame.Rect(100, GROUND_Y - 50, 40, 50)
velocity_x = 0
velocity_y = 0
acceleration = 0.5
friction = 0.9
gravity = 1
is_jumping = False
rings_collected = 0

platforms = [pygame.Rect(0, GROUND_Y, WORLD_WIDTH, 50)]
rings = [pygame.Rect(random.randint(200, WORLD_WIDTH - 200), GROUND_Y - 30, 20, 20) for _ in range(30)]
checkpoints = [i for i in range(1000, WORLD_WIDTH, 1000)]
RED = (255, 0, 0)

goal_rect = pygame.Rect(WORLD_WIDTH - 100, GROUND_Y - 80, 80, 80)
camera_x = 0

enemies = [pygame.Rect(random.randint(60, 1000), GROUND_Y - 40, 40, 40) for _ in range(2)]
enemy_speeds = [random.choice([-2, 2]) for _ in range(len(enemies))]

enemies2 = [pygame.Rect(random.randint(3000, 3700), GROUND_Y - 40, 40, 40) for _ in range(1)]
enemy2_speeds = [random.choice([-2, 2]) for _ in range(len(enemies2))]

# Boss
boss = pygame.Rect(WORLD_WIDTH - 300, GROUND_Y - 50, 50, 50)
boss_jumping = False
boss_jump_timer = 0
boss_air_time = 60  # 3 secondes en l'air (180 frames à 60 fps)
boss_ground_time = 420  # 7 secondes au sol (420 frames à 60 fps)
boss_state_timer = boss_ground_time  # Timer initial sur le sol
clock = pygame.time.Clock()
running = True

while running:
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        velocity_x = min(velocity_x + acceleration, MAX_SPEED)
    elif keys[pygame.K_LEFT]:
        velocity_x = max(velocity_x - acceleration, -MAX_SPEED)
    else:
        velocity_x *= friction
    
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = -15
        is_jumping = True
        jump_sound.play()
    
    velocity_y += gravity
    
    player.x += int(velocity_x)
    player.y += int(velocity_y)
    
    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.y = platform.y - player.height
            velocity_y = 0
            is_jumping = False
    
    camera_x = max(0, min(player.x - WIDTH // 2, WORLD_WIDTH - WIDTH))
    
    # Correction de la collecte des anneaux
    new_rings = []
    for ring in rings:
        if player.colliderect(ring):
            ring_sound.play()
            rings_collected += 1
        else:
            new_rings.append(ring)
    rings = new_rings
    
    new_enemies = []
    for i, enemy in enumerate(enemies):
        enemy.x += enemy_speeds[i]
        if enemy.x < 60 or enemy.x > 1000:
            enemy_speeds[i] *= -1
        if player.colliderect(enemy):
            if velocity_y > 0:
                enemieMort_sound.play()
                velocity_y = -10
                continue
            else:
                hit_sound.play()
                if rings_collected > 0:
                    rings_collected = 0
                else:
                    running = False
        else:
            new_enemies.append(enemy)
    enemies = new_enemies

    new_enemies2 = []
    for i, enemy2 in enumerate(enemies2):
        enemy2.x += enemy2_speeds[i]
        if enemy2.x < 3000 or enemy2.x > 3700:
            enemy2_speeds[i] *= -1
        if player.colliderect(enemy2):
            if velocity_y > 0:
                enemieMort_sound.play()
                velocity_y = -10
                continue
            else:
                hit_sound.play()
                if rings_collected > 0:
                    rings_collected = 0
                else:
                    running = False
        else:
            new_enemies2.append(enemy2)
    enemies2 = new_enemies2

   # Boss comportement
    boss_state_timer -= 1
    if not boss_jumping:
        if boss_state_timer <= 0:
            boss_jumping = True
            boss_state_timer = boss_air_time
            boss.y -= 100
    else:
        if boss_state_timer <= 0:
            boss.y = GROUND_Y - 50
            boss_jumping = False
            boss_state_timer = boss_ground_time
    
    if player.colliderect(boss):
        running = False  # One-shot du joueur
    
    screen.blit(background_img, (-camera_x, 0))
    screen.blit(player_img, (player.x - camera_x, player.y))
    for platform in platforms:
        pygame.draw.rect(screen, COULEUR_SOL, (platform.x - camera_x, platform.y, platform.width, platform.height))
    for ring in rings:
        screen.blit(ring_img, (ring.x - camera_x, ring.y))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.x - camera_x, enemy.y))
    for enemy2 in enemies2:
        screen.blit(enemy2_img, (enemy2.x - camera_x, enemy2.y))
    for checkpoint in checkpoints:
        pygame.draw.line(screen, RED, (checkpoint - camera_x, GROUND_Y), (checkpoint - camera_x, HEIGHT), 2)
    screen.blit(goal_img, (goal_rect.x - camera_x, goal_rect.y))
    screen.blit(boss_img, (boss.x - camera_x, boss.y))
    rings_text = pygame.font.Font(None, 36).render(f"RINGS: {rings_collected}", True, (255, 215, 0))
    screen.blit(rings_text, (10, 10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
