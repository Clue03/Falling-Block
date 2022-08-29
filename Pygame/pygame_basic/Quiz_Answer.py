# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 640 * 480 (세, 가)
# 2. 캐릭터, 똥 70 * 70
###############################################################################

from turtle import screensize
import pygame
import random as r

pygame.init() #초기화 (반드시 필요한 작업)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 제목 설정
pygame.display.set_caption("따라 만든 게임 1")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 폰트, 좌표 etc...)

#배경 불러오기
background = pygame.image.load("C:/python master/bg.png")

#캐릭터 불러오기
character = pygame.image.load("C:/python master/char.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6
enemy_speed = r.randint(1,10)

# 적 캐릭터

enemy = pygame.image.load("C:/python master/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = r.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)  #초당 프레임 수 설정
    print("fps: " + str(clock.get_fps()))

#2. 이벤트 처리 (키보드, 마우스 etc...)   
    for event in pygame.event.get():  #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

# 3. 게임 캐릭터 위치 정의                
    character_x_pos += to_x * dt
    enemy_y_pos += 10
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = r.randint(0, screen_width - enemy_width)
    
# 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 확인
    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False
        
# 5. 화면에 그리기        
    screen.blit(background, (0,0))   
    screen.blit(character, (character_x_pos, character_y_pos))    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    pygame.display.update()

pygame.time.delay(500)

pygame.quit()