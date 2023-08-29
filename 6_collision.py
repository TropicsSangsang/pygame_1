import pygame

pygame.init()  #초기화(반드시 필요):pygame을 하면 반드시 해줘야 함

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("AppA Game")    # 게임 이름

# FPS
clock = pygame.time.Clock()


#배경 이미지 불러오기
background = pygame.image.load("C:\\PYTHONWORKSPACE\\pygame_basic\\background.png")


#캐릭터( 스프라이트 )불러오기

character = pygame.image.load("C:\\PYTHONWORKSPACE\\pygame_basic\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]   # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = ( screen_width - character_width ) / 2  #화면가로의 절반크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height        # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터

enemy = pygame.image.load("C:\\PYTHONWORKSPACE\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  #이미지의 크기를 구해옴
enemy_width = enemy_size[0]   # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = ( screen_width - enemy_width ) / 2  #화면가로의 절반크기에 해당하는 곳에 위치(가로)
enemy_y_pos = ( screen_height - enemy_height ) / 2       # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)


# 이벤트 루프: 이것이 있어야 위에서 만든 창이 계속해서 존재할수 있게 된다.
# 없으면 창이 생겼다가 바로 사라지는데 계속해서 존재할려면 이벤트 루프라는 것이
# 있어서 
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 델타라는 변수에 저장

 # 캐릭터가 1초동안에 100만큼 이동을 해야함
 # 10 fps : 1초 동안에 10번 동작-->한번에 몇만큼 이동? 10만큼 이동!! 10*10=100
 # 20 fps : 1초 동안에 20번 동작-->한번에 5만큼 이동!! 5*20=100   

    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():   #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님


        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  #캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
            elif event.key == pygame.K_UP:
                to_y -= character_speed 
            elif event.key ==pygame.K_DOWN:
                to_y += character_speed 

        if event.type ==pygame.KEYUP:   # 방향키를 뗴면 멈춤
            if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x = 0
            elif event.key ==pygame.K_UP or event.key ==pygame.K_DOWN:    
                to_y = 0

    character_x_pos += to_x*dt  # 캐릭터 위치를 to_x에 위치시키고 키가 눌러졌을때 위치를 정해준다
    character_y_pos += to_y*dt  # 이 부분이 없으면 안움직임

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:       
        character_y_pos = screen_height - character_height     

    # 총돌 처리를 위한 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("총돌했어요")
        running = False



    screen.blit(background, (0, 0))  #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    pygame.display.update()  # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()
