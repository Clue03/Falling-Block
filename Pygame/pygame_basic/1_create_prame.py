from turtle import screensize
import pygame

pygame.init() #초기화 (반드시 필요한 작업)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("따라 만든 게임 1")

running = True
while running:
    for event in pygame.event.get():  #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()