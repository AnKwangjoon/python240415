import pygame
import sys

# 화면 크기 설정
WIDTH = 800
HEIGHT = 600

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 블록 정보
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 30
BLOCK_COLOR = (0, 255, 0)

# 공 정보
BALL_RADIUS = 10
BALL_COLOR = (255, 0, 0)
BALL_SPEED = [5, 5]

# 패들 정보
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
PADDLE_COLOR = (0, 0, 255)

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")
clock = pygame.time.Clock()

# 블록 그리기 함수
def draw_block(x, y):
    pygame.draw.rect(screen, BLOCK_COLOR, (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

# 공 그리기 함수
def draw_ball(x, y):
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

# 패들 그리기 함수
def draw_paddle(x, y):
    pygame.draw.rect(screen, PADDLE_COLOR, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

# 게임 루프
def game_loop():
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx, ball_dy = BALL_SPEED

    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    paddle_y = HEIGHT - 50

    block_rows = 5
    block_cols = 10
    blocks = []
    for row in range(block_rows):
        for col in range(block_cols):
            blocks.append(pygame.Rect(col * (BLOCK_WIDTH + 2), row * (BLOCK_HEIGHT + 2), BLOCK_WIDTH, BLOCK_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= 10
        if keys[pygame.K_RIGHT]:
            paddle_x += 10

        screen.fill(WHITE)

        ball_x += ball_dx
        ball_y += ball_dy

        # 벽과 공의 충돌 처리
        if ball_x <= 0 or ball_x >= WIDTH:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy

        # 패들과 공의 충돌 처리
        if ball_y >= paddle_y - BALL_RADIUS and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
            ball_dy = -ball_dy

        # 블록과 공의 충돌 처리
        for block in blocks[:]:
            if block.colliderect(pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
                blocks.remove(block)
                ball_dy = -ball_dy

        draw_ball(ball_x, ball_y)
        draw_paddle(paddle_x, paddle_y)
        for block in blocks:
            draw_block(block.x, block.y)

        pygame.display.flip()
        clock.tick(60)

game_loop()
