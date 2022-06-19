# 파이게임 불러오기
import pygame

# 파이게임 초기화
pygame.init()

# 크기 지정
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 지정
WHITE = (255, 255, 255)

# 제목 지정
pygame.display.set_caption("파이게임")

# 종료 플래그로 사용되는 변수
done = False

# 메인 루프
while not done:
    for event in pygame.event.get(): # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT: # 윈도 종료 버튼을 누르면 종료
            done = True

        screen.fill(WHITE) #스크린 색상 흰색
        pygame.display.update() #화면의 필요한 부분만을 수정

# 파이게임 종료
pygame.quit()
