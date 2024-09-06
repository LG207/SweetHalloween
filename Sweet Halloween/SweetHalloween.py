import pygame
import sys
import random
import math

# Inicializa o pygame
pygame.init()

# Define as dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sweet Halloween Project")

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
BAR_COLOR = (0, 255, 0)  # Cor da barra de vida

# Define a taxa de atualização do jogo
FPS = 60
clock = pygame.time.Clock()

# Carrega as imagens dos ícones e redimensiona para um tamanho menor
icon_size = (40, 40)  # Tamanho pequeno e consistente para os ícones
shield_icon_active = pygame.transform.scale(pygame.image.load('shield_active.png'), icon_size)  # Ícone de escudo ativo
shield_icon_inactive = pygame.transform.scale(pygame.image.load('shield_inactive.png'), icon_size)  # Ícone de escudo inativo
item_image = pygame.image.load("candy.png").convert_alpha() # Ícone doce
ghost_frame1 = pygame.image.load("ghost1.png").convert_alpha() # Sprite fantasma
ghost_frame2 = pygame.image.load("ghost2.png").convert_alpha() # Sprite fantasma
blob_frame1 = pygame.image.load("blob1.png").convert_alpha() # Sprite blob
blob_frame2 = pygame.image.load("blob2.png").convert_alpha() # Sprite blob
redEye_frame1 = pygame.image.load("red1.png").convert_alpha() # Sprite red
redEye_frame2 = pygame.image.load("red2.png").convert_alpha() # Sprite red
background_image = pygame.image.load("fundoH.png").convert_alpha() # Sprite background
cacBoy_image = pygame.image.load("cacBoy.png").convert_alpha() #Sprite Jogador
# redimensionar a imagem
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a fonte para o texto
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 30)

# Função para desenhar o texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Função para o menu principal ===================================================================================================================================
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Sweet Halloween", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        mx, my = pygame.mouse.get_pos()

        # Define os botões
        button_play = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
        button_credits = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50)
        button_quit = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 90, 200, 50)

        # Desenha os botões
        pygame.draw.rect(screen, BLUE, button_play)
        pygame.draw.rect(screen, BLUE, button_credits)
        pygame.draw.rect(screen, BLUE, button_quit)

        # Desenha o texto dos botões
        draw_text("Jogar", small_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        draw_text("Créditos", small_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)
        draw_text("Sair", small_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 115)

        # Verifica se algum botão foi clicado
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_play.collidepoint((mx, my)):
            if click:
                game()  # Inicia o jogo
        if button_credits.collidepoint((mx, my)):
            if click:
                credits()  # Exibe os créditos
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

# Função para a tela de créditos
def credits():
    while True:
        screen.fill(BLACK)
        draw_text("Créditos", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text("Desenvolvido por Luiz", small_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        mx, my = pygame.mouse.get_pos()

        button_back = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 90, 200, 50)

        pygame.draw.rect(screen, BLUE, button_back)

        draw_text("Voltar", small_font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 115)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_back.collidepoint((mx, my)):
            if click:
                main_menu()  # Volta para o menu principal

        pygame.display.flip()
        clock.tick(FPS)

# Função do jogo principal ===================================================================================================================================
def game():
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(cacBoy_image, (int(cacBoy_image.get_width() * 1.5), int(cacBoy_image.get_height() * 1.5)))  # carrega sprite do personagem
            self.rect = self.image.get_rect()  # Obtém o retângulo do personagem
            self.rect.centerx = SCREEN_WIDTH // 2  # Centraliza o personagem horizontalmente
            self.rect.bottom = SCREEN_HEIGHT - 10  # Posiciona o personagem próximo à base da tela
            self.speed = 5  # Velocidade do personagem
            self.shield = True  # Escudo ativo no início
            self.items_collected = 0  # Contador de itens coletados
            self.level = 1 # Inicia no nivel 1
            self.shoot_speed = 5 # Velocidade dos tiros
            self.last_shot_time = 0  # Marca o último momento em que o jogador atirou
            self.shoot_delay = 700  # Tempo de atraso entre tiros (em milissegundos)
            self.invulnerable = False  # Controle de invulnerabilidade
            self.invulnerable_time = 0  # Tempo que o jogador fica invulnerável
            self.invulnerable_duration = 1000  # Duração da invulnerabilidade (1 segundo)


        # Temporização do tiro
        def shoot(self, target_x, target_y):
            current_time = pygame.time.get_ticks() # Verifica se o tempo entre os tiros passou
            if current_time - self.last_shot_time >= self.shoot_delay: # Cria a bala se o atraso for suficiente
                bullet = Bullet(self.rect.centerx, self.rect.centery, target_x, target_y)
                all_sprites.add(bullet)  # Adiciona a bala à lista de todos os sprites
                player_bullets.add(bullet)  # Adiciona a bala à lista de balas do jogador
                self.last_shot_time = current_time  # Atualiza o último momento em que o jogador atirou

        # Contador de itens
        def collect_item(self, item):
            self.items_collected += 1  # Incrementa o contador de itens coletados
            item.kill()  # Remove o item da tela

        # Caso o personagem seja hitado
        def hit(self):
            if not self.invulnerable:  # Só recebe dano se não estiver invulnerável
                if self.shield:  # Se o escudo estiver ativo
                    self.shield = False  # Desativa o escudo
                    print("Escudo destruído!")
                    self.invulnerable = True  # Ativa a invulnerabilidade
                    self.invulnerable_time = pygame.time.get_ticks()  # Registra o tempo que ficou invulnerável
                else:
                    print("O jogador foi atingido!")
                    game_over = True
    
                    while game_over:
                        screen.fill(BLACK)
                        
                        # Exibir "Você Perdeu"
                        game_over_text = font.render("Você Perdeu", True, RED)
                        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 150))
                        
                        # Exibir opções
                        menu_text = small_font.render("Voltar ao Menu", True, WHITE)
                        quit_text = small_font.render("Sair", True, WHITE)
                        
                        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, 360))
                        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, 420))
                        
                        screen.blit(menu_text, menu_rect)
                        screen.blit(quit_text, quit_rect)
                        
                        pygame.display.flip()
                        
                        # Detectar clique do mouse
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = pygame.mouse.get_pos()
                                if menu_rect.collidepoint(mouse_pos):
                                    game_over = False
                                    main_menu()
                                elif quit_rect.collidepoint(mouse_pos):
                                    pygame.quit()
                                    sys.exit()

        # Movimento do Personagem/ Sistema de escudo/ Invencibilidade/ Níveis/ Vitória - Frames
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:  # Move para a esquerda
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:  # Move para a direita
                self.rect.x += self.speed

            # Mantém o personagem dentro dos limites da tela
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            # Checa se o jogador ainda está invulnerável e calcula a duração
            if self.invulnerable:
                current_time = pygame.time.get_ticks()
                if current_time - self.invulnerable_time > self.invulnerable_duration:
                    self.invulnerable = False  # Remove a invulnerabilidade após 1 segundo

            # Verifica se o jogador avançou de fase/ Tela da vitória
            if self.items_collected >= 10:
                self.items_collected = 0  # Reseta o contador de itens
                self.level += 1  # Avança de nível
                print(f"Avançou para o nível {self.level}")
                if self.level > 3:
                    # Loop para a tela de vitória
                    while True:
                        screen.fill((0, 0, 0))  # Preenche a tela com preto

                        # Renderiza a mensagem de vitória
                        font = pygame.font.SysFont(None, 74)
                        victory_text = font.render("Você salvou o Halloween!", True, (255, 255, 255))
                        screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, SCREEN_HEIGHT // 4))

                        # Renderiza os botões
                        button_font = pygame.font.SysFont(None, 50)
                        menu_button_text = button_font.render("Menu Principal", True, (255, 255, 255))
                        exit_button_text = button_font.render("Sair", True, (255, 255, 255))

                        # Define os retângulos dos botões
                        menu_button_rect = menu_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                        exit_button_rect = exit_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

                        # Desenha os botões na tela
                        pygame.draw.rect(screen, (0, 128, 0), menu_button_rect.inflate(20, 10))
                        pygame.draw.rect(screen, (128, 0, 0), exit_button_rect.inflate(20, 10))
                        screen.blit(menu_button_text, menu_button_rect)
                        screen.blit(exit_button_text, exit_button_rect)

                        # Verifica eventos do mouse
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if menu_button_rect.collidepoint(event.pos):
                                    main_menu()  # Volta ao menu principal
                                elif exit_button_rect.collidepoint(event.pos):
                                    pygame.quit()
                                    sys.exit()  # Sai do jogo

                        pygame.display.flip()            

    # Classe da bala
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, target_x, target_y):
            super().__init__()
            self.image = pygame.Surface((5, 10))  # Cria um retângulo de 5x10 como bala
            self.image.fill(WHITE)  # Define a cor da bala
            self.rect = self.image.get_rect()  # Obtém o retângulo da bala
            self.rect.centerx = x
            self.rect.centery = y
            
            # Calcula a direção da bala
            angle = math.atan2(target_y - y, target_x - x)
            self.speed_x = math.cos(angle) * 10
            self.speed_y = math.sin(angle) * 10

        def update(self):
            self.rect.x += self.speed_x  # Move a bala
            self.rect.y += self.speed_y  # Move a bala
            # Remove a bala se ela sair da tela
            if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
                self.kill()

    # Classe do inimigo
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, color, speed, direction):
            super().__init__()
            self.image = pygame.Surface((50, 50))  # Cria um quadrado de 50x50 como inimigo
            self.image.fill(color)  # Define a cor do inimigo
            self.rect = self.image.get_rect()  # Obtém o retângulo do inimigo
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # Posiciona aleatoriamente no eixo x
            self.rect.y = random.randint(100, 200)  # Posiciona na parte superior da tela
            self.speed = speed  # Velocidade do inimigo
            self.direction = direction  # Direção de movimento horizontal (-1 esquerda, 1 direita)

            # Carrega os dois frames de animação
            self.frames = [pygame.transform.scale(redEye_frame1, (int(redEye_frame1.get_width() * 3.0), int(redEye_frame1.get_height() * 3.0))),
                            pygame.transform.scale(redEye_frame2, (int(redEye_frame2.get_width() * 3.0), int(redEye_frame2.get_height() * 3.0)))]
    
            self.current_frame = 0  # Frame atual da animação
            self.frame_count = 0  # Contador para trocar os frames

            self.image = self.frames[self.current_frame]  # Define o frame inicial
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.x += self.speed * self.direction  # Move o inimigo horizontalmente

            # Inverte a direção se bater na borda da tela
            if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.direction *= -1

                # O inimigo atira ocasionalmente
            if random.random() < 0.01:  # 1% de chance de atirar a cada frame
                self.shoot()

            # Alterna entre os frames de animação
            self.animate()

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.bottom, random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT)
            all_sprites.add(bullet)  # Adiciona a bala à lista de todos os sprites
            enemy_bullets.add(bullet)  # Adiciona a bala à lista de balas dos inimigos

        def kill(self):
            # Chance de drop de item ao ser destruído (70% de chance)
            if random.random() < 0.7:
                item = Item(self.rect.centerx, self.rect.centery)
                all_sprites.add(item)  # Adiciona o item aos sprites
                items.add(item)  # Adiciona o item ao grupo de itens
            super().kill()

        def animate(self):
            # A cada 10 frames de jogo, alterna o frame da sprite
            self.frame_count += 1
            if self.frame_count >= 10:  # Ajuste o valor para mudar a velocidade da animação
                self.current_frame = (self.current_frame + 1) % len(self.frames)  # Alterna entre 0 e 1
                self.image = self.frames[self.current_frame]  # Atualiza a imagem do inimigo
                self.frame_count = 0  # Reseta o contador

    class DiagonalEnemy(Enemy):
        def __init__(self):
            super().__init__(YELLOW, random.choice([3, 4]), random.choice([-1, 1]))  # velocidade moderada, movimento diagonal
            self.rect.x = random.choice([0, SCREEN_WIDTH - self.rect.width])  # Começa nas bordas laterais
            self.rect.y = random.randint(50, 150)
            self.vertical_direction = random.choice([-1, 1])  # Direção vertical aleatória

            # Carrega os dois frames de animação
            self.frames = [pygame.transform.scale(ghost_frame1, (int(ghost_frame1.get_width() * 3.0), int(ghost_frame1.get_height() * 3.0))),
                            pygame.transform.scale(ghost_frame2, (int(ghost_frame2.get_width() * 3.0), int(ghost_frame2.get_height() * 3.0)))]
    
            
            self.current_frame = 0  # Frame atual da animação
            self.frame_count = 0  # Contador para trocar os frames

            self.image = self.frames[self.current_frame]  # Define o frame inicial
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.x += self.speed * self.direction  # Move horizontalmente
            self.rect.y += self.speed * self.vertical_direction  # Move verticalmente

            # Inverte a direção horizontal se bater na borda da tela
            if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.direction *= -1
            # Inverte a direção vertical se bater na borda superior ou inferior
            if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
                self.vertical_direction *= -1

            # Alterna entre os frames de animação
            self.animate()

        def animate(self):
            # A cada 10 frames de jogo, alterna o frame da sprite
            self.frame_count += 1
            if self.frame_count >= 10:  # Ajuste o valor para mudar a velocidade da animação
                self.current_frame = (self.current_frame + 1) % len(self.frames)  # Alterna entre 0 e 1
                self.image = self.frames[self.current_frame]  # Atualiza a imagem do inimigo
                self.frame_count = 0  # Reseta o contador

            if pygame.sprite.collide_rect(self, player):
                player.hit()  # Causa dano ao jogador

        def damage_player(self, player):
            if player.shield:  # Se o jogador tem escudo
                player.shield = False  # Desativa o escudo
            else:
                player.hit()  # Atinge o jogador caso o escudo esteja desativado

    class ShooterEnemy(Enemy):
        def __init__(self):
            super().__init__(GREEN, 2, random.choice([-1, 1]))  # Verde, velocidade lenta, movimento horizontal aleatório
            self.shoot_delay = 0  # Contador para o delay entre os tiros

            # Carrega os dois frames de animação
            self.frames = [pygame.transform.scale(blob_frame1, (int(blob_frame1.get_width() * 5.0), int(blob_frame1.get_height() * 5.0))),
                            pygame.transform.scale(blob_frame2, (int(blob_frame2.get_width() * 5.0), int(blob_frame2.get_height() * 5.0)))]
    
            self.current_frame = 0  # Frame atual da animação
            self.frame_count = 0  # Contador para trocar os frames

            self.image = self.frames[self.current_frame]  # Define o frame inicial
            self.rect = self.image.get_rect()

        def update(self):
            super().update()
            self.shoot_delay += 1
            if self.shoot_delay >= 120:  # Atira a cada 120 frames (~2 segundos)
                self.shoot_multiple()
                self.shoot_delay = 0

            # Alterna entre os frames de animação
            self.animate()

        def animate(self):
            # A cada 10 frames de jogo, alterna o frame da sprite
            self.frame_count += 1
            if self.frame_count >= 10:  # Ajuste o valor para mudar a velocidade da animação
                self.current_frame = (self.current_frame + 1) % len(self.frames)  # Alterna entre 0 e 1
                self.image = self.frames[self.current_frame]  # Atualiza a imagem do inimigo
                self.frame_count = 0  # Reseta o contador


        def shoot_multiple(self):
            for i in range(3):  # Atira 3 balas em sequência
                bullet = Bullet(self.rect.centerx, self.rect.bottom + i * 20, random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT)
                all_sprites.add(bullet)
                enemy_bullets.add(bullet)

    # Classe do item que pode ser coletado
    class Item(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = item_image  # Usa a sprite carregada como a imagem do item
            self.rect = self.image.get_rect()
            self.rect.center = (x,y) # Define a posição inicial do item
            self.gravity = 0.3  # Aceleração da gravidade
            self.speed_y = 0  # Velocidade vertical inicial

        def update(self):
            self.speed_y += self.gravity  # Aumenta a velocidade vertical pela gravidade
            self.rect.y += self.speed_y  # Atualiza a posição do item no eixo y
            if self.rect.bottom >= SCREEN_HEIGHT: # Verifica se o item chegou no chão
                self.rect.bottom = SCREEN_HEIGHT  # Mantém o item no chão
                self.speed_y = 0  # Para a movimentação

    # Função para criar novos inimigos
    def create_enemy():
        enemy_type = random.choice([Enemy, DiagonalEnemy, ShooterEnemy])
        if enemy_type == Enemy:
            enemy = Enemy(RED, random.choice([3, 4, 5]), random.choice([-1, 1]))
        elif enemy_type == DiagonalEnemy:
            enemy = DiagonalEnemy()
        else:
            enemy = ShooterEnemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Função para desenhar a interface
    def draw_interface(player):
        # Desenha a faixa de fundo para os ícones
        pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, 60))  # Faixa na parte superior com 60px de altura

        # Desenha o ícone do escudo
        if player.shield:
            screen.blit(shield_icon_active, (10, 20))  # Ícone de escudo ativo
        else:
            screen.blit(shield_icon_inactive, (10, 20))  # Ícone de escudo inativo

        # Mostra o contador de itens coletados
        item_count_text = small_font.render(f"Doces coletados: {player.items_collected}", True, WHITE)
        screen.blit(item_count_text, (10, 70))  # Exibe o número de itens coletados

        # Mostra o nível atual
        level_count_text = small_font.render(f"Nível: {player.level} de 3", True, WHITE)
        screen.blit(level_count_text, (650, 70))

    # Configurações iniciais
    # Cria grupos de sprites
    all_sprites = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # Cria o jogador e adiciona ao grupo de todos os sprites
    player = Player()
    all_sprites.add(player)

    # Timer para o spawn dos inimigos
    spawn_timer = pygame.time.get_ticks()
    spawn_interval = 1000  # 1 segundo

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Fecha o jogo se o usuário clicar no "X"
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique com o botão esquerdo do mouse
                    player.shoot(*event.pos)
      
        # Desenhar o fundo primeiro
        screen.blit(background_image, (0, 0))

        # Atualiza os sprites
        all_sprites.update()

        # Verifica colisões entre as balas dos inimigos e o jogador
        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            player.hit()

        # Verifica colisões entre as balas do jogador e os inimigos
        hits = pygame.sprite.groupcollide(enemies, player_bullets, True, True)

        # Verifica colisões entre o jogador e itens
        collected_items = pygame.sprite.spritecollide(player, items, True)
        for item in collected_items:
            player.collect_item(item)  # Coleta o item

        # Gerencia o spawn de novos inimigos
        current_time = pygame.time.get_ticks()
        if current_time - spawn_timer >= spawn_interval:
            create_enemy()
            spawn_timer = current_time  # Reinicia o temporizador de spawn

        # Desenha tudo na tela
        #screen.fill(BLACK)  # Limpa a tela com a cor preta
        all_sprites.draw(screen)  # Desenha todos os sprites na tela

        # Desenha a interface
        draw_interface(player)
        all_sprites.draw(screen)  # Desenha todos os sprites na tela
        pygame.display.flip()  # Atualiza a tela

        # Mantém a taxa de atualização constante
        clock.tick(FPS)

    # Encerra o pygame
    pygame.quit()
    sys.exit()

# Chama o menu principal
main_menu()