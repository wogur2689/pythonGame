# 파이게임 불러오기
import os
import pygame

# 파이게임 초기화
pygame.init()

# 크기 지정
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임시간 설정
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) #파일 경로
background = pygame.image.load(os.path.join(current_path, "background.png")) #파일명과 조인하여 저장


# 종료 플래그로 사용되는 변수
running = True

# 메인 루프
while running:
    clock.tick(60) # FPS 60으로 설정

    for event in pygame.event.get(): # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT: # 윈도 종료 버튼을 누르면 종료
            running = False

        screen.blit(background, (0, 0)) # 0,0에 배경 삽입
        pygame.display.update() #배경 업데이트

# 파이게임 종료
pygame.quit()
