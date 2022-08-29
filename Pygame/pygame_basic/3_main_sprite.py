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

running = True
while running:
    for event in pygame.event.get():  #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))   
    screen.blit(character, (character_x_pos, character_y_pos))    

    pygame.display.update()


#게임 종료
pygame.quit()