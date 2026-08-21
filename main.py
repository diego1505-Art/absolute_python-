import pygame
import random
import sys

# --- CONFIGURATION ---
WIDTH = 500
HEIGHT = 700
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Initialisation
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ULTRA SPACE SHOOTER - No Ads Edition")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# --- CLASSES ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # On crée un triangle pour le vaisseau (en attendant une image)
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, GREEN, [(20, 0), (0, 40), (40, 40)])
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        return Bullet(self.rect.centerx, self.rect.top)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(
            center=(random.randint(20, WIDTH-20), random.randint(-100, -40))
        )
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# --- LOGIQUE PRINCIPALE ---

def main():
    player = Player()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    
    all_sprites.add(player)
    
    score = 0
    running = True

    while running:
        # 1. Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # 2. Mise à jour
        all_sprites.update()
        
        # Apparition aléatoire des ennemis
        if random.random() < 0.05:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Collisions : Balles <-> Ennemis
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for hit in hits:
            score += 10

        # Collisions : Joueur <-> Ennemis
        if pygame.sprite.spritecollide(player, enemies, False):
            running = False # Game Over !

        # 3. Dessin
        screen.fill(BLACK)
        
        # Dessiner des étoiles en arrière-plan pour le style
        for i in range(10):
            pygame.draw.circle(screen, WHITE, (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 1)

        all_sprites.draw(screen)
        
        # Affichage du score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Ecran de fin
    print(f"GAME OVER ! Ton score final est de : {score}")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
