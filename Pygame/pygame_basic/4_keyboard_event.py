from turtle import screensize
import pygame

pygame.init() #초기화 (반드시 필요한 작업)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 제목 설정
pygame.display.set_caption("따라 만든 게임 1")

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

running = True
while running:
    for event in pygame.event.get():  #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x
    character_y_pos += to_y
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
            
    screen.blit(background, (0,0))   
    screen.blit(character, (character_x_pos, character_y_pos))    

    pygame.display.update()


#게임 종료
pygame.quit()