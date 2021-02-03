# import module
import os
import random
import pygame
import sys  # sys.exit을 이용한 게임 종료 코드
from pygame.locals import *  # import 는 Pygame

print("""
──────────────▐█████───────
──────▄▄████████████▄──────
────▄██▀▀────▐███▐████▄────
──▄██▀───────███▌▐██─▀██▄──
─▐██────────▐███─▐██───██▌─
─██▌────────███▌─▐██───▐██─
▐██────────▐███──▐██────██▌
██▌────────███▌──▐██────▐██
██▌───────▐███───▐██────▐██
██▌───────███▌──▄─▀█────▐██
██▌──────▐████████▄─────▐██
██▌──────█████████▀─────▐██
▐██─────▐██▌────▀─▄█────██▌
─██▌────███─────▄███───▐██─
─▐██▄──▐██▌───────────▄██▌─
──▀███─███─────────▄▄███▀──
──────▐██▌─▀█████████▀▀────
──────███──────────────────

FakeVengers Game """)
print()

name = input("What is your name? : ")
print("Welcome to FakeVengers game, {}!".format(name))

total_running = True
while total_running:
    to_play = input("This is a main room. Do you wanna continue? (yes or no) : ")
    if to_play == "yes":
        while True:
            choose_rooms = input("choose a room btw 1 to 4 (1-4) : ")
            ######################################################
            if choose_rooms == '1':
                ans = input("Good, do you wanna play car racing? (yes or no) : ")
                if ans == "yes":
                    print("Let's play car racing!")
                    ######################################################
                    # Car racing game
                    pygame.init()

                    # 화면 크기 설정해당 프로그램을 통해 이루고자 하는 바를 적어주세요.
                    screen_width = 480  # 가로 크기
                    screen_height = 640  # 세로 크기
                    screen = pygame.display.set_mode((screen_width, screen_height))

                    # 화면 타이틀 설정
                    pygame.display.set_caption("Car Racing")

                    # FPS
                    clock = pygame.time.Clock()
                    ######################################################

                    # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
                    current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
                    image_path = os.path.join(current_path, "images")  # images 폴더 위치 반환

                    # 배경 만들기
                    background = pygame.image.load(os.path.join(image_path, "background.c.png"))

                    # 캐릭터 만들기
                    character = pygame.image.load(os.path.join(image_path, "RacingCar02.png"))
                    character_size = character.get_rect().size
                    character_width = character_size[0]
                    character_height = character_size[1]
                    character_x_pos = (screen_width / 2) - (character_width / 2)
                    character_y_pos = screen_height - character_height

                    #  이동 위치
                    to_x = 0
                    to_y = 0
                    character_speed = 10

                    # 장애물 만들기
                    enemy = pygame.image.load(os.path.join(image_path, "car2.png"))
                    enemy_size = enemy.get_rect().size
                    enemy_width = enemy_size[0]
                    enemy_height = enemy_size[1]
                    enemy_x_pos = random.randint(0, screen_width - enemy_width)
                    enemy_y_pos = 0
                    enemy_speed = 8

                    enemy2 = pygame.image.load(os.path.join(image_path, "car2.png"))
                    enemy2_size = enemy2.get_rect().size
                    enemy2_width = enemy2_size[0]
                    enemy2_height = enemy2_size[1]
                    enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
                    enemy2_y_pos = 0
                    enemy2_speed = 6


                    running = True
                    time_start = pygame.time.get_ticks()  # 추가

                    while running:
                        dt = clock.tick(60)

                        # 2. 이벤트 처리(키보드, 마우스 등)
                        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                                running = False  # 게임이 진행중이 아님

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    to_x -= character_speed
                                elif event.key == pygame.K_RIGHT:
                                    to_x += character_speed
                                elif event.key == pygame.K_UP:  # 캐릭터를 위로
                                    to_y -= character_speed
                                elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                                    to_y += character_speed

                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    to_x = 0
                                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    to_y = 0

                        # 3. 게임 캐릭터 위치 정의
                        character_x_pos += to_x
                        character_y_pos += to_y

                        if character_x_pos < 0:
                            character_x_pos = 0
                        elif character_x_pos > screen_width - character_width:
                            character_x_pos = screen_width - character_width

                        # 세로 경계값 처리
                        if character_y_pos < 0:
                            character_y_pos = 0
                        elif character_y_pos > screen_height - character_height:
                            character_y_pos = screen_height - character_height

                        enemy_y_pos += enemy_speed

                        if enemy_y_pos > screen_height:
                            enemy_y_pos = 0
                            enemy_x_pos = random.randint(0, screen_width - enemy_width)

                        enemy2_y_pos += enemy2_speed

                        if enemy2_y_pos > screen_height:
                            enemy2_y_pos = 0
                            enemy2_x_pos = random.randint(0, screen_width - enemy2_width)

                        # 4. 충돌 처리
                        character_rect = character.get_rect()
                        character_rect.left = character_x_pos
                        character_rect.top = character_y_pos

                        enemy_rect = enemy.get_rect()
                        enemy_rect.left = enemy_x_pos
                        enemy_rect.top = enemy_y_pos

                        if character_rect.colliderect(enemy_rect):
                            print("collide")
                            running = False

                        enemy2_rect = enemy2.get_rect()
                        enemy2_rect.left = enemy2_x_pos
                        enemy2_rect.top = enemy2_y_pos

                        if character_rect.colliderect(enemy2_rect):
                            print("collide")
                            running = False

                        # 5. 화면에 그리기
                        screen.blit(background, (0, 0))
                        screen.blit(character, (character_x_pos, character_y_pos))
                        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
                        screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))

                        # 시간 제한 10초
                        time_remaining = 10000 - (pygame.time.get_ticks() - time_start)

                        if time_remaining <= 0:
                            print("You win!")
                            running = False

                        pygame.display.update()

                    # 잠시 대기

                    pygame.time.delay(680)  # 1.5초 정도 대기(ms)
                    pygame.quit()

                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            if choose_rooms == '2':
                ans = input("Good, do you wanna play shooting game? (yes or no) : ")
                if ans == "yes":
                    print("Let's play shooting game!")
                    ######################################################
                    # Shooting game
                    # 기본 초기화(반드시 해야 하는 것들)
                    pygame.init()

                    # 화면 크기 설정
                    screen_width = 640  # 가로 크기
                    screen_height = 480  # 세로 크기
                    screen = pygame.display.set_mode((screen_width, screen_height))

                    # 화면 타이틀 설정
                    pygame.display.set_caption("Pang")  # 게임 이름

                    # FPS
                    clock = pygame.time.Clock()
                    ######################################################

                    # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
                    current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
                    image_path = os.path.join(current_path, "images")  # images 폴더 위치 반환

                    # 배경 만들기
                    background = pygame.image.load(os.path.join(image_path, "background.png"))

                    # 스테이지 만들기
                    stage = pygame.image.load(os.path.join(image_path, "stage.png"))
                    stage_size = stage.get_rect().size
                    stage_height = stage_size[1]  # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

                    # 캐릭터 만들기
                    character = pygame.image.load(os.path.join(image_path, "character.png"))
                    character_size = character.get_rect().size
                    character_width = character_size[0]
                    character_height = character_size[1]
                    character_x_pos = (screen_width / 2) - (character_width / 2)
                    character_y_pos = screen_height - character_height - stage_height

                    # 캐릭터 이동 방향
                    character_to_x = 0

                    # 캐릭터 이동 속도
                    character_speed = 6

                    # 무기 만들기
                    weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
                    weapon_size = weapon.get_rect().size
                    weapon_width = weapon_size[0]

                    # 무기는 한 번에 여러 발 발사 가능
                    weapons = []

                    # 무기 이동 속도
                    weapon_speed = 10

                    # 공 만들기 (4개 크기에 대해 따로 처리
                    ball_images = [
                        pygame.image.load(os.path.join(image_path, "balloon1.png")),
                        pygame.image.load(os.path.join(image_path, "balloon2.png")),
                        pygame.image.load(os.path.join(image_path, "balloon3.png")),
                        pygame.image.load(os.path.join(image_path, "balloon4.png"))]

                    # 공 크기에 따른 최초 스피드
                    ball_speed_y = [-18, -15, -12, -9]  # index 0,1,2,3 에 해당하는 값

                    # 공들
                    balls = []

                    balls.append({
                        "pos_x": 50,  # 공의 x 좌표
                        "pos_y": 50,  # 공의 y 좌표
                        "img_idx": 0,  # 공의 이미지 인덱스
                        "to_x": 3,  # x 축 이동방향,
                        "to_y": -6,  # y 축 이동방향
                        "init_spd_y": ball_speed_y[0]})  # y 최초 속도

                    # 사라질 무기, 공 정보 저장 변수
                    weapon_to_remove = -1
                    ball_to_remove = -1

                    running = True
                    while running:
                        dt = clock.tick(30)

                        # 2. 이벤트 처리(키보드, 마우스 등)
                        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                                running = False  # 게임이 진행중이 아님

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                                    character_to_x -= character_speed
                                elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                                    character_to_x += character_speed
                                elif event.key == pygame.K_SPACE:  # 무기 발사
                                    weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                                    weapon_y_pos = character_y_pos
                                    weapons.append([weapon_x_pos, weapon_y_pos])

                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    character_to_x = 0

                        # 3. 게임 캐릭터 위치 정의

                        character_x_pos += character_to_x

                        if character_x_pos < 0:
                            character_x_pos = 0
                        elif character_x_pos > screen_width - character_width:
                            character_x_pos = screen_width - character_width

                        # 무기 위치 조정
                        weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # 무기 위치를 위#

                        # 천장에 닿은 무기 없애기
                        weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

                        # 공 위치 정의
                        for ball_idx, ball_val in enumerate(balls):
                            ball_pos_x = ball_val["pos_x"]
                            ball_pos_y = ball_val["pos_y"]
                            ball_img_idx = ball_val["img_idx"]

                            ball_size = ball_images[ball_img_idx].get_rect().size
                            ball_width = ball_size[0]
                            ball_height = ball_size[1]

                            # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                            if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
                                ball_val["to_x"] = ball_val["to_x"] * -1

                            # 세로 위치
                            if ball_pos_y >= screen_height - stage_height - ball_height:
                                ball_val["to_y"] = ball_val["init_spd_y"]
                            else:  # 그 외의 모든 경우에는 속도를 증가
                                ball_val["to_y"] += 0.5

                            ball_val["pos_x"] += ball_val["to_x"]
                            ball_val["pos_y"] += ball_val["to_y"]

                        # 4. 충돌 처리

                        # 캐릭터 rect 정보 업데이트
                        character_rect = character.get_rect()
                        character_rect.left = character_x_pos
                        character_rect.top = character_y_pos

                        for ball_idx, ball_val in enumerate(balls):
                            ball_pos_x = ball_val["pos_x"]
                            ball_pos_y = ball_val["pos_y"]
                            ball_img_idx = ball_val["img_idx"]

                            # 공 rect 정보 업데이트
                            ball_rect = ball_images[ball_img_idx].get_rect()
                            ball_rect.left = ball_pos_x
                            ball_rect.top = ball_pos_y

                            # 공과 캐릭터 충돌 처리
                            if character_rect.colliderect(ball_rect):
                                running = False
                                break

                            # 공과 무기들 충돌 처리
                            for weapon_idx, weapon_val in enumerate(weapons):
                                weapon_pos_x = weapon_val[0]
                                weapon_pos_y = weapon_val[1]

                                # 무기 rect 정보 업데이트
                                weapon_rect = weapon.get_rect()
                                weapon_rect.left = weapon_pos_x
                                weapon_rect.top = weapon_pos_y

                                # 충돌 체크
                                if weapon_rect.colliderect(ball_rect):
                                    weapon_to_remove = weapon_idx  # 해당 무기 없애기 위한 값 설정
                                    ball_to_remove = ball_idx

                                    # 가장 작은 크기의 공이 아니라면 다음단계의 공으로 나눠주기
                                    if ball_img_idx < 3:
                                        # 현재 공 크기 정보를 가지고 옴
                                        ball_width = ball_rect.size[0]
                                        ball_height = ball_rect.size[1]

                                        # 나눠진 공 정보
                                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                                        small_ball_width = small_ball_rect.size[0]
                                        small_ball_height = small_ball_rect.size[1]

                                        # 왼쪽으로 튕겨나가는 작은 공
                                        balls.append({
                                            "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),  # 공의 x 좌표
                                            "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                                            # 공의 y 좌표
                                            "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                                            "to_x": -3,  # x 축 이동방향,
                                            "to_y": -6,  # y 축 이동방향
                                            "init_spd_y": ball_speed_y[ball_img_idx + 1]})  # y 최초 속도

                                        # 오른쪽으로 튕겨나가는 작은 공
                                        balls.append({
                                            "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),  # 공의 x 좌표
                                            "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                                            # 공의 y 좌표
                                            "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                                            "to_x": 3,  # x 축 이동방향,
                                            "to_y": -6,  # y 축 이동방향
                                            "init_spd_y": ball_speed_y[ball_img_idx + 1]})  # y 최초 속도

                                    break

                        # 충돌된 공 or 무기 없애기
                        if ball_to_remove > -1:
                            del balls[ball_to_remove]
                            ball_to_remove = -1

                        if weapon_to_remove > -1:
                            del weapons[weapon_to_remove]
                            weapon_to_remove = -1

                        # 다 없앴으면 이긴다
                        if len(balls) == 0:
                            print("You win!")
                            running = False

                        # 5. 화면에 그리기
                        screen.blit(background, (0, 0))

                        for weapon_x_pos, weapon_y_pos in weapons:
                            screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

                        for idx, val in enumerate(balls):
                            ball_pos_x = val["pos_x"]
                            ball_pos_y = val["pos_y"]
                            ball_img_idx = val["img_idx"]
                            screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

                        screen.blit(stage, (0, screen_height - stage_height))
                        screen.blit(character, (character_x_pos, character_y_pos))

                        pygame.display.update()

                    pygame.time.delay(680)  # 1.5초 정도 대기(ms)
                    pygame.quit()
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            if choose_rooms == '3':
                ans = input("Good, do you wanna play flappy bird? (yes or no) : ")
                if ans == "yes":
                    print("Let's play flappy bird! (Press the space bar)")
                    ######################################################
                    # flappy bird game

                    # 게임값
                    FPS = 32  # 값을 높이면 게임의 템포가 빨라집니다
                    SCREENWIDTH = 289
                    SCREENHEIGHT = 511
                    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
                    GROUNDY = SCREENHEIGHT * 0.8
                    GAME_SPRITES = {}
                    GAME_SOUNDS = {}
                    PLAYER = 'gallery/sprites/bird.png'
                    BACKGROUND = 'gallery/sprites/background.png'
                    PIPE = 'gallery/sprites/pipe.png'


                    def welcomeScreen():
                        """
                        Shows welcome images on the screen
                        """

                        playerx = int(SCREENWIDTH / 5)
                        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
                        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
                        messagey = int(SCREENHEIGHT * 0.13)
                        basex = 0
                        while True:
                            for event in pygame.event.get():
                                # 유저가 X를 누르면 게임을 종료
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()

                                # 유저가 스페이스, 윗 키를 누르는 경우 게임을 진행
                                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                                    return
                                else:
                                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                                    SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                                    pygame.display.update()
                                    FPSCLOCK.tick(FPS)


                    def mainGame():
                        score = 0
                        playerx = int(SCREENWIDTH / 5)
                        playery = int(SCREENWIDTH / 2)
                        basex = 0

                        # 2개의 파이프를 랜덤으로 가져옵니다 이는 맨 위에있는 랜덤 모듈에서 기인합니다.
                        newPipe1 = getRandomPipe()
                        newPipe2 = getRandomPipe()

                        # 윗 파이프의 리스트
                        upperPipes = [
                            {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
                            {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
                        ]
                        # 아랫 파이프의 리스트
                        lowerPipes = [
                            {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
                            {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
                        ]

                        pipeVelX = -4

                        playerVelY = -9
                        playerMaxVelY = 10
                        playerMinVelY = -8
                        playerAccY = 1

                        playerFlapAccv = -8  # velocity while flapping
                        playerFlapped = False  # It is true only when the bird is flapping

                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                                    if playery > 0:
                                        playerVelY = playerFlapAccv
                                        playerFlapped = True
                                        GAME_SOUNDS['wing'].play()

                            crashTest = isCollide(playerx, playery, upperPipes,
                                                  lowerPipes)  # This function will return true if the player is crashed
                            if crashTest:
                                return

                                # 점수 확인
                            playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
                            for pipe in upperPipes:
                                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
                                if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                                    score += 1
                                    print(f"Your score is {score}")
                                    GAME_SOUNDS['point'].play()

                            if playerVelY < playerMaxVelY and not playerFlapped:
                                playerVelY += playerAccY

                            if playerFlapped:
                                playerFlapped = False
                            playerHeight = GAME_SPRITES['player'].get_height()
                            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

                            # 파이프는 지속적으로 좌측을 향해 이동시키는 코드입니다.
                            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                                upperPipe['x'] += pipeVelX
                                lowerPipe['x'] += pipeVelX

                            # 왼쪽 모서리족으로 파이프가 도달하고 지워질때 새로운 파이프를 오른쪽에서 만들어내는 코드입니다.
                            if 0 < upperPipes[0]['x'] < 5:
                                newpipe = getRandomPipe()
                                upperPipes.append(newpipe[0])
                                lowerPipes.append(newpipe[1])

                            # 파이프가 스크린을 벗어난다면 지워내야합니다.
                            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                                upperPipes.pop(0)
                                lowerPipes.pop(0)

                            # blit은 이미지를 복사하는 코드입니다.
                            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

                            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                            myDigits = [int(x) for x in list(str(score))]
                            width = 0
                            for digit in myDigits:
                                width += GAME_SPRITES['numbers'][digit].get_width()
                            Xoffset = (SCREENWIDTH - width) / 2

                            for digit in myDigits:
                                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.12))
                                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
                            pygame.display.update()
                            FPSCLOCK.tick(FPS)


                    def isCollide(playerx, playery, upperPipes, lowerPipes):
                        if playery > GROUNDY - 25 or playery < 0:
                            GAME_SOUNDS['hit'].play()
                            return True

                        for pipe in upperPipes:
                            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
                            if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][
                                0].get_width()):
                                GAME_SOUNDS['hit'].play()
                                return True

                        for pipe in lowerPipes:
                            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(
                                    playerx - pipe['x']) < \
                                    GAME_SPRITES['pipe'][0].get_width():
                                GAME_SOUNDS['hit'].play()
                                return True

                        return False


                    def getRandomPipe():
                        """
                        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
                        """
                        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
                        offset = SCREENHEIGHT / 3
                        y2 = offset + random.randrange(0, int(
                            SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
                        pipeX = SCREENWIDTH + 10
                        y1 = pipeHeight - y2 + offset
                        pipe = [
                            {'x': pipeX, 'y': -y1},  # 위에 파이프
                            {'x': pipeX, 'y': y2}  # 아래파이프 이처럼 y엑시즈를 변경함을 통해 장애물을 조절할 수 있습니다.
                        ]
                        return pipe


                    if __name__ == "__main__":
                        # 게임이 시작하는 메인포인
                        pygame.init()  # 파이게임 모듈의 시작을 알립니다
                        FPSCLOCK = pygame.time.Clock()
                        pygame.display.set_caption('Flappy Bird by DongJun\'s Datum')
                        GAME_SPRITES['numbers'] = (
                            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
                            pygame.image.load('gallery/sprites/9.png').convert_alpha(),
                        )

                        GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.jpg').convert_alpha()
                        GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
                        GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                                                pygame.image.load(PIPE).convert_alpha()
                                                )

                        # 게임 소리설정과 관련된 코드
                        GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
                        GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
                        GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
                        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
                        GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

                        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
                        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

                        # while True:
                        welcomeScreen()  # 버튼을 누를때까지 게임창만 띄워줍니다
                        mainGame()  # 메인게임을 실행합니다

                    pygame.time.delay(680)  # 1.5초 정도 대기(ms)
                    pygame.quit()
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            if choose_rooms == '4':
                ans = input("Good, do you wanna play T-REX game? (yes or no) : ")
                if ans == "yes":
                    print("Let's play T-REX game!")
                    ######################################################
                    # T-REX game
                    __author__ = "Shivam Shekhar"

                    from pygame import *

                    pygame.mixer.pre_init(44100, -16, 2, 2048)  # fix audio delay
                    pygame.init()

                    scr_size = (width, height) = (600, 150)
                    FPS = 60
                    gravity = 0.6

                    black = (0, 0, 0)
                    white = (255, 255, 255)
                    background_col = (235, 235, 235)

                    high_score = 0

                    screen = pygame.display.set_mode(scr_size)
                    clock = pygame.time.Clock()
                    pygame.display.set_caption("T-Rex Rush")

                    jump_sound = pygame.mixer.Sound('sprites/jump.wav')
                    die_sound = pygame.mixer.Sound('sprites/die.wav')
                    checkPoint_sound = pygame.mixer.Sound('sprites/checkPoint.wav')


                    def load_image(
                            name,
                            sizex=-1,
                            sizey=-1,
                            colorkey=None,
                    ):

                        fullname = os.path.join('sprites', name)
                        image = pygame.image.load(fullname)
                        image = image.convert()
                        if colorkey is not None:
                            if colorkey is -1:
                                colorkey = image.get_at((0, 0))
                            image.set_colorkey(colorkey, RLEACCEL)

                        if sizex != -1 or sizey != -1:
                            image = pygame.transform.scale(image, (sizex, sizey))

                        return (image, image.get_rect())


                    def load_sprite_sheet(
                            sheetname,
                            nx,
                            ny,
                            scalex=-1,
                            scaley=-1,
                            colorkey=None,
                    ):
                        fullname = os.path.join('sprites', sheetname)
                        sheet = pygame.image.load(fullname)
                        sheet = sheet.convert()

                        sheet_rect = sheet.get_rect()

                        sprites = []

                        sizex = sheet_rect.width / nx
                        sizey = sheet_rect.height / ny

                        for i in range(0, ny):
                            for j in range(0, nx):
                                rect = pygame.Rect((j * sizex, i * sizey, sizex, sizey))
                                image = pygame.Surface(rect.size)
                                image = image.convert()
                                image.blit(sheet, (0, 0), rect)

                                if colorkey is not None:
                                    if colorkey is -1:
                                        colorkey = image.get_at((0, 0))
                                    image.set_colorkey(colorkey, RLEACCEL)

                                if scalex != -1 or scaley != -1:
                                    image = pygame.transform.scale(image, (scalex, scaley))

                                sprites.append(image)

                        sprite_rect = sprites[0].get_rect()

                        return sprites, sprite_rect


                    def disp_gameOver_msg(retbutton_image, gameover_image):
                        retbutton_rect = retbutton_image.get_rect()
                        retbutton_rect.centerx = width / 2
                        retbutton_rect.top = height * 0.52

                        gameover_rect = gameover_image.get_rect()
                        gameover_rect.centerx = width / 2
                        gameover_rect.centery = height * 0.35

                        screen.blit(retbutton_image, retbutton_rect)
                        screen.blit(gameover_image, gameover_rect)


                    def extractDigits(number):
                        if number > -1:
                            digits = []
                            i = 0
                            while (number / 10 != 0):
                                digits.append(number % 10)
                                number = int(number / 10)

                            digits.append(number % 10)
                            for i in range(len(digits), 5):
                                digits.append(0)
                            digits.reverse()
                            return digits


                    class Dino():
                        def __init__(self, sizex=-1, sizey=-1):
                            self.images, self.rect = load_sprite_sheet('dino.png', 5, 1, sizex, sizey, -1)
                            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png', 2, 1, 59, sizey, -1)
                            self.rect.bottom = int(0.98 * height)
                            self.rect.left = width / 15
                            self.image = self.images[0]
                            self.index = 0
                            self.counter = 0
                            self.score = 0
                            self.isJumping = False
                            self.isDead = False
                            self.isDucking = False
                            self.isBlinking = False
                            self.movement = [0, 0]
                            self.jumpSpeed = 11.5

                            self.stand_pos_width = self.rect.width
                            self.duck_pos_width = self.rect1.width

                        def draw(self):
                            screen.blit(self.image, self.rect)

                        def checkbounds(self):
                            if self.rect.bottom > int(0.98 * height):
                                self.rect.bottom = int(0.98 * height)
                                self.isJumping = False

                        def update(self):
                            if self.isJumping:
                                self.movement[1] = self.movement[1] + gravity

                            if self.isJumping:
                                self.index = 0
                            elif self.isBlinking:
                                if self.index == 0:
                                    if self.counter % 400 == 399:
                                        self.index = (self.index + 1) % 2
                                else:
                                    if self.counter % 20 == 19:
                                        self.index = (self.index + 1) % 2

                            elif self.isDucking:
                                if self.counter % 5 == 0:
                                    self.index = (self.index + 1) % 2
                            else:
                                if self.counter % 5 == 0:
                                    self.index = (self.index + 1) % 2 + 2

                            if self.isDead:
                                self.index = 4

                            if not self.isDucking:
                                self.image = self.images[self.index]
                                self.rect.width = self.stand_pos_width
                            else:
                                self.image = self.images1[(self.index) % 2]
                                self.rect.width = self.duck_pos_width

                            self.rect = self.rect.move(self.movement)
                            self.checkbounds()

                            if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
                                self.score += 1
                                if self.score % 100 == 0 and self.score != 0:
                                    if pygame.mixer.get_init() != None:
                                        checkPoint_sound.play()

                            self.counter = (self.counter + 1)


                    class Cactus(pygame.sprite.Sprite):
                        def __init__(self, speed=5, sizex=-1, sizey=-1):
                            pygame.sprite.Sprite.__init__(self, self.containers)
                            self.images, self.rect = load_sprite_sheet('cacti-small.png', 3, 1, sizex, sizey, -1)
                            self.rect.bottom = int(0.98 * height)
                            self.rect.left = width + self.rect.width
                            self.image = self.images[random.randrange(0, 3)]
                            self.movement = [-1 * speed, 0]

                        def draw(self):
                            screen.blit(self.image, self.rect)

                        def update(self):
                            self.rect = self.rect.move(self.movement)

                            if self.rect.right < 0:
                                self.kill()


                    class Ptera(pygame.sprite.Sprite):
                        def __init__(self, speed=5, sizex=-1, sizey=-1):
                            pygame.sprite.Sprite.__init__(self, self.containers)
                            self.images, self.rect = load_sprite_sheet('ptera.png', 2, 1, sizex, sizey, -1)
                            self.ptera_height = [height * 0.82, height * 0.75, height * 0.60]
                            self.rect.centery = self.ptera_height[random.randrange(0, 3)]
                            self.rect.left = width + self.rect.width
                            self.image = self.images[0]
                            self.movement = [-1 * speed, 0]
                            self.index = 0
                            self.counter = 0

                        def draw(self):
                            screen.blit(self.image, self.rect)

                        def update(self):
                            if self.counter % 10 == 0:
                                self.index = (self.index + 1) % 2
                            self.image = self.images[self.index]
                            self.rect = self.rect.move(self.movement)
                            self.counter = (self.counter + 1)
                            if self.rect.right < 0:
                                self.kill()


                    class Ground():
                        def __init__(self, speed=-5):
                            self.image, self.rect = load_image('ground.png', -1, -1, -1)
                            self.image1, self.rect1 = load_image('ground.png', -1, -1, -1)
                            self.rect.bottom = height
                            self.rect1.bottom = height
                            self.rect1.left = self.rect.right
                            self.speed = speed

                        def draw(self):
                            screen.blit(self.image, self.rect)
                            screen.blit(self.image1, self.rect1)

                        def update(self):
                            self.rect.left += self.speed
                            self.rect1.left += self.speed

                            if self.rect.right < 0:
                                self.rect.left = self.rect1.right

                            if self.rect1.right < 0:
                                self.rect1.left = self.rect.right


                    class Cloud(pygame.sprite.Sprite):
                        def __init__(self, x, y):
                            pygame.sprite.Sprite.__init__(self, self.containers)
                            self.image, self.rect = load_image('cloud.png', int(90 * 30 / 42), 30, -1)
                            self.speed = 1
                            self.rect.left = x
                            self.rect.top = y
                            self.movement = [-1 * self.speed, 0]

                        def draw(self):
                            screen.blit(self.image, self.rect)

                        def update(self):
                            self.rect = self.rect.move(self.movement)
                            if self.rect.right < 0:
                                self.kill()


                    class Scoreboard():
                        def __init__(self, x=-1, y=-1):
                            self.score = 0
                            self.tempimages, self.temprect = load_sprite_sheet('numbers.png', 12, 1, 11,
                                                                               int(11 * 6 / 5), -1)
                            self.image = pygame.Surface((55, int(11 * 6 / 5)))
                            self.rect = self.image.get_rect()
                            if x == -1:
                                self.rect.left = width * 0.89
                            else:
                                self.rect.left = x
                            if y == -1:
                                self.rect.top = height * 0.1
                            else:
                                self.rect.top = y

                        def draw(self):
                            screen.blit(self.image, self.rect)

                        def update(self, score):
                            score_digits = extractDigits(score)
                            self.image.fill(background_col)
                            for s in score_digits:
                                self.image.blit(self.tempimages[s], self.temprect)
                                self.temprect.left += self.temprect.width
                            self.temprect.left = 0


                    def introscreen():
                        temp_dino = Dino(44, 47)
                        temp_dino.isBlinking = True
                        gameStart = False

                        callout, callout_rect = load_image('call_out.png', 196, 45, -1)
                        callout_rect.left = width * 0.05
                        callout_rect.top = height * 0.4

                        temp_ground, temp_ground_rect = load_sprite_sheet('ground.png', 15, 1, -1, -1, -1)
                        temp_ground_rect.left = width / 20
                        temp_ground_rect.bottom = height

                        logo, logo_rect = load_image('logo.png', 240, 40, -1)
                        logo_rect.centerx = width * 0.6
                        logo_rect.centery = height * 0.6
                        while not gameStart:
                            if pygame.display.get_surface() == None:
                                print("Couldn't load display surface")
                                return True
                            else:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return True
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                                            temp_dino.isJumping = True
                                            temp_dino.isBlinking = False
                                            temp_dino.movement[1] = -1 * temp_dino.jumpSpeed

                            temp_dino.update()

                            if pygame.display.get_surface() != None:
                                screen.fill(background_col)
                                screen.blit(temp_ground[0], temp_ground_rect)
                                if temp_dino.isBlinking:
                                    screen.blit(logo, logo_rect)
                                    screen.blit(callout, callout_rect)
                                temp_dino.draw()

                                pygame.display.update()

                            clock.tick(FPS)
                            if temp_dino.isJumping == False and temp_dino.isBlinking == False:
                                gameStart = True


                    def gameplay():
                        global high_score
                        gamespeed = 4
                        startMenu = False
                        gameOver = False
                        gameQuit = False
                        playerDino = Dino(44, 47)
                        new_ground = Ground(-1 * gamespeed)
                        scb = Scoreboard()
                        highsc = Scoreboard(width * 0.78)
                        counter = 0

                        cacti = pygame.sprite.Group()
                        pteras = pygame.sprite.Group()
                        clouds = pygame.sprite.Group()
                        last_obstacle = pygame.sprite.Group()

                        Cactus.containers = cacti
                        Ptera.containers = pteras
                        Cloud.containers = clouds

                        retbutton_image, retbutton_rect = load_image('replay_button.png', 35, 31, -1)
                        gameover_image, gameover_rect = load_image('game_over.png', 190, 11, -1)

                        temp_images, temp_rect = load_sprite_sheet('numbers.png', 12, 1, 11, int(11 * 6 / 5), -1)
                        HI_image = pygame.Surface((22, int(11 * 6 / 5)))
                        HI_rect = HI_image.get_rect()
                        HI_image.fill(background_col)
                        HI_image.blit(temp_images[10], temp_rect)
                        temp_rect.left += temp_rect.width
                        HI_image.blit(temp_images[11], temp_rect)
                        HI_rect.top = height * 0.1
                        HI_rect.left = width * 0.73

                        while not gameQuit:
                            while startMenu:
                                pass
                            while not gameOver:
                                if pygame.display.get_surface() == None:
                                    print("Couldn't load display surface")
                                    gameQuit = True
                                    gameOver = True
                                else:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            gameQuit = True
                                            gameOver = True

                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_SPACE:
                                                if playerDino.rect.bottom == int(0.98 * height):
                                                    playerDino.isJumping = True
                                                    if pygame.mixer.get_init() != None:
                                                        jump_sound.play()
                                                    playerDino.movement[1] = -1 * playerDino.jumpSpeed

                                            if event.key == pygame.K_DOWN:
                                                if not (playerDino.isJumping and playerDino.isDead):
                                                    playerDino.isDucking = True

                                        if event.type == pygame.KEYUP:
                                            if event.key == pygame.K_DOWN:
                                                playerDino.isDucking = False
                                for c in cacti:
                                    c.movement[0] = -1 * gamespeed
                                    if pygame.sprite.collide_mask(playerDino, c):
                                        playerDino.isDead = True
                                        if pygame.mixer.get_init() != None:
                                            die_sound.play()

                                for p in pteras:
                                    p.movement[0] = -1 * gamespeed
                                    if pygame.sprite.collide_mask(playerDino, p):
                                        playerDino.isDead = True
                                        if pygame.mixer.get_init() != None:
                                            die_sound.play()

                                if len(cacti) < 2:
                                    if len(cacti) == 0:
                                        last_obstacle.empty()
                                        last_obstacle.add(Cactus(gamespeed, 40, 40))
                                    else:
                                        for l in last_obstacle:
                                            if l.rect.right < width * 0.7 and random.randrange(0, 50) == 10:
                                                last_obstacle.empty()
                                                last_obstacle.add(Cactus(gamespeed, 40, 40))

                                if len(pteras) == 0 and random.randrange(0, 200) == 10 and counter > 500:
                                    for l in last_obstacle:
                                        if l.rect.right < width * 0.8:
                                            last_obstacle.empty()
                                            last_obstacle.add(Ptera(gamespeed, 46, 40))

                                if len(clouds) < 5 and random.randrange(0, 300) == 10:
                                    Cloud(width, random.randrange(height / 5, height / 2))

                                playerDino.update()
                                cacti.update()
                                pteras.update()
                                clouds.update()
                                new_ground.update()
                                scb.update(playerDino.score)
                                highsc.update(high_score)

                                if pygame.display.get_surface() != None:
                                    screen.fill(background_col)
                                    new_ground.draw()
                                    clouds.draw(screen)
                                    scb.draw()
                                    if high_score != 0:
                                        highsc.draw()
                                        screen.blit(HI_image, HI_rect)
                                    cacti.draw(screen)
                                    pteras.draw(screen)
                                    playerDino.draw()

                                    pygame.display.update()
                                clock.tick(FPS)

                                if playerDino.isDead:
                                    gameOver = True
                                    if playerDino.score > high_score:
                                        high_score = playerDino.score

                                if counter % 700 == 699:
                                    new_ground.speed -= 1
                                    gamespeed += 1

                                counter = (counter + 1)

                            if gameQuit:
                                break

                            while gameOver:
                                if pygame.display.get_surface() == None:
                                    print("Couldn't load display surface")
                                    gameQuit = True
                                    gameOver = False
                                else:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            gameQuit = True
                                            gameOver = False
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_ESCAPE:
                                                gameQuit = True
                                                gameOver = False

                                            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                                                gameOver = False
                                                gameplay()
                                highsc.update(high_score)
                                if pygame.display.get_surface() != None:
                                    disp_gameOver_msg(retbutton_image, gameover_image)
                                    if high_score != 0:
                                        highsc.draw()
                                        screen.blit(HI_image, HI_rect)
                                    pygame.display.update()
                                clock.tick(FPS)

                        pygame.quit()
                        quit()


                    def main():
                        isGameQuit = introscreen()
                        if not isGameQuit:
                            gameplay()

                    main()

                    pygame.quit()
                    ######################################################
                    print("Game is over. Back to the main room")
                    break

                elif ans == "no":
                    print("Then we go back to the main room")
                    break

            else:
                print("Please answer correctly")


    elif to_play == "no":
        while True:
            quit_ans = input("Do you really wanna quit? : (yes or no) ")
            if quit_ans == "yes":
                print("Goodbye, {}".format(name))
                total_running = False
                break
            elif quit_ans == "no":
                break
            else:
                print("Please answer 'yes or 'no'")

    else:
        print("Please answer 'yes or 'no'")