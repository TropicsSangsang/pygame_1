import pygame

pygame.init()  #초기화(반드시 필요):pygame을 하면 반드시 해줘야 함

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("AppA Game")    # 게임 이름

#배경 이미지 불러오기  픽셀 480 640
background = pygame.image.load("C:\\PYTHONWORKSPACE\\pygame_basic\\background.png")

# 이벤트 루프: 이것이 있어야 위에서 만든 창이 계속해서 존재할수 있게 된다.
# 없으면 창이 생겼다가 바로 사라지는데 계속해서 존재할려면 이벤트 루프라는 것이
# 있어서 
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():   #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님


    # screen.fill((0, 0, 225))   background변수와 blit메서드 대신에 이것으로 사용가능   
    screen.blit(background, (0, 0))  #배경 그리기 : blit에 (넣을 대상 , 위치는 튜플형식으로)

    pygame.display.update()  # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()
