# 배경 이미지 설정
import pygame

# 파이게임 초기화
pygame.init()

# 크기 지정
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 제목 지정
pygame.display.set_caption("Puzzle Bobble")

# 게임시간 설정
clock = pygame.time.Clock()

# 종료 플래그로 사용되는 변수
running = True

# 메인 루프
while running:
    clock.tick(60) # FPS 60으로 설정

    for event in pygame.event.get(): # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT: # 윈도 종료 버튼을 누르면 종료
            running = False

        pygame.display.update() #화면의 필요한 부분만을 수정

# 파이게임 종료
pygame.quit()
