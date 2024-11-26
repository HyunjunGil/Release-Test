import pygame
import logging

# 로그 파일 설정
logging.basicConfig(
    filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

# Pygame 초기화
logging.info("Initializing Pygame")
pygame.init()

# 화면 설정
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello App")

# 글꼴 설정
font = pygame.font.Font(None, 50)  # 기본 시스템 글꼴, 크기 50
text = font.render("Hello", True, (255, 255, 255))  # 흰색 텍스트
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

# 색상 설정
background_color = (0, 0, 0)  # 검은색 배경

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            logging.info("Exit event triggered")
            running = False

    # 화면 채우기
    screen.fill(background_color)

    # 텍스트 그리기
    screen.blit(text, text_rect)

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()
logging.info("Pygame terminated")
