# 버블 이미지 설정 / map 생성
import os
import pygame

# 버블 클래스 생성
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)

# 맵 만들기
def setup():
    global map #전역공간에 있는 맵 사용
    map = [
        # ["R", "R", "Y", "Y", "B", "B", "G", "G"],
        list("RRYYBBGG"),
        list("RRYYBBG/"), # / : 버블이 위치할 수 없는 곳
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"), # . : 비어 있는 곳
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
    ]

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:
                continue
            position = get_bubble_position(row_idx, col_idx)
            image = get_bubble_image(col)
            bubble_group.add(Bubble(image, col, position))

def get_bubble_position(row_idx, col_idx):
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1:
        pos_x += CELL_SIZE // 2
    return pos_x, pos_y

def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "Y":
        return bubble_images[1]
    elif color == "B":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    elif color == "P":
        return bubble_images[4]
    else: # BLACK
        return bubble_images[-1]

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

# 버블 이미지 불러오기
bubble_images = [
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(), #가져오면서 투명도 처리
    pygame.image.load(os.path.join(current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha()
]

# 게임 관련 변수
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62

map = [] # 맵
bubble_group = pygame.sprite.Group()
setup()

# 종료 플래그로 사용되는 변수
running = True

# 메인 루프
while running:
    clock.tick(60) # FPS 60으로 설정

    for event in pygame.event.get(): # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT: # 윈도 종료 버튼을 누르면 종료
            running = False

        screen.blit(background, (0, 0)) # 0,0에 배경 삽입
        bubble_group.draw(screen)
        pygame.display.update() #배경 업데이트

# 파이게임 종료
pygame.quit()
