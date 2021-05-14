import random
import pygame
pygame.init()

W = 1280
H = 720
fps = 60
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Miner's adventure")
pygame.display.set_icon(pygame.image.load('img/ico.jpg'))

loose = False
a = 0
score = 0
extra_score = 0
skin1_fl = True
skin2_fl = False
tutor = True
bonus_fl = False


def skin_screen():
    while True:
        global skin1_fl
        global skin2_fl
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        bg = pygame.Surface((1280, 720))
        skin1 = pygame.image.load('img/hero.png').convert_alpha()
        skin1_rect = skin1.get_rect(center=(320, 350))
        skin2 = pygame.image.load('img/hero1.png').convert_alpha()
        skin2_rect = skin2.get_rect(center=(960, 350))
        back = pygame.image.load('img/back.png').convert_alpha()
        back_rect = back.get_rect(center=(100, 460))
        selected = pygame.image.load('img/selected.png').convert_alpha()
        sc.blit(bg, (0, 0))
        sc.blit(skin1, skin1_rect)
        sc.blit(skin2, skin2_rect)

        if skin1_rect.collidepoint(mouse):
            if click and skin2_fl:
                skin1_fl = True
                skin2_fl = False

        if skin2_rect.collidepoint(mouse):
            if click and skin1_fl:
                skin1_fl = False
                skin2_fl = True

        if skin1_fl:
            sc.blit(selected, (260, 415))
        if skin2_fl:
            sc.blit(selected, (900, 415))

        sc.blit(back, back_rect)
        if back_rect.collidepoint(mouse):
            if click:
                menu()

        pygame.display.update()


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        bg = pygame.image.load('img/menubg.png').convert_alpha()
        exit_act = pygame.image.load('img/exitact.png').convert_alpha()
        exit_rect = exit_act.get_rect(center=(620, 600))
        exit_pass = pygame.image.load('img/exitpass.png').convert_alpha()
        play_act = pygame.image.load('img/playact.png').convert_alpha()
        play_rect = play_act.get_rect(center=(620, 400))
        play_pass = pygame.image.load('img/playpass.png').convert_alpha()
        skins = pygame.image.load('img/skins.png').convert_alpha()
        skins_rect = skins.get_rect(center=(620, 500))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        sc.blit(bg, (0, 0))
        sc.blit(skins, skins_rect)
        if exit_rect.collidepoint(mouse):
            sc.blit(exit_act, exit_rect)
            if click:
                exit()
        else:
            sc.blit(exit_pass, exit_rect)

        if play_rect.collidepoint(mouse):
            sc.blit(play_act, play_rect)
            if click:
                loop()
        else:
            sc.blit(play_pass, play_rect)

        if skins_rect.collidepoint(mouse):
            if click:
                skin_screen()

        pygame.display.update()


def defeat():
    global loose
    global score
    global extra_score
    while loose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        picture = pygame.Surface((500, 400))
        picture.fill((0,0,0))
        button = pygame.image.load('img/again.png').convert_alpha()
        button1 = pygame.image.load('img/menuback.png').convert_alpha()
        button_rect = button.get_rect(center=(740, 420))
        button1_rect = button1.get_rect(center=(500, 420))

        picture_rect = picture.get_rect(center=(630, 315))
        sc.blit(picture, picture_rect)
        font = pygame.font.SysFont('arial', 40)
        text = font.render('Проиграно!', True, (255,255,255))
        text1 = font.render('Твой счет: ' + str(score + extra_score), True, (255, 255, 255))
        if button_rect.collidepoint(mouse):
            if click:
                loop()
        if button1_rect.collidepoint(mouse):
            if click:
                menu()

        sc.blit(button, button_rect)
        sc.blit(button1, button1_rect)
        sc.blit(text, (520, 200))
        sc.blit(text1, (510, 270))


        pygame.display.update()

def loop():
    global score
    global loose
    global skin1_fl
    global skin2_fl
    global tutor


    #downloads
    bonus1_img = pygame.image.load('img/bonus1.png').convert_alpha()
    bonus2_img = pygame.image.load('img/bonus2.png').convert_alpha()
    elon_bad = pygame.image.load('img/elon-bad.png').convert_alpha()
    elon_good = pygame.image.load('img/elon-good.png').convert_alpha()
    bg_img = pygame.image.load('img/background.png').convert_alpha()
    ground_img = pygame.image.load('img/ground.png').convert_alpha()
    enemy1_img = pygame.image.load('img/enemy1.png').convert_alpha()
    enemy2_img = pygame.image.load('img/enemy2.png').convert_alpha()
    enemy3_img = pygame.image.load('img/enemy3.png').convert_alpha()
    enemy4_img = pygame.image.load('img/enemy4.png').convert_alpha()
    enemy5_img = pygame.image.load('img/enemy5.png').convert_alpha()
    tutor_img = pygame.image.load('img/tutor.png').convert_alpha()
    if skin1_fl:
        hero_img = pygame.image.load('img/hero.png').convert_alpha()
    if skin2_fl:
        hero_img = pygame.image.load('img/hero1.png').convert_alpha()

    enemy_list = [enemy1_img, enemy2_img, enemy3_img,enemy4_img,enemy5_img]
    enemy1 = enemy1_img
    enemy2 = enemy2_img
    bonus_list = [bonus1_img, bonus2_img, elon_bad, elon_good]
    bonus = bonus1_img

    #rect
    hero_rect = hero_img.get_rect(midbottom=(120, 550))
    enemy_rect = enemy1.get_rect(midbottom=(1300, 550))
    enemy2_rect = enemy2.get_rect(midbottom=(1850, 550))
    bonus_rect = bonus.get_rect(midbottom=(1400, 330))


    #ground move int
    i = 0

    #jump
    jump_fl = False
    vel_y = 22

    #score

    global extra_score
    global a
    extra_score = 0
    a = 0
    Bonus_on = pygame.USEREVENT
    pygame.time.set_timer(Bonus_on, 7000)


    global bonus_fl

    enemy_speed = 5
    randint = 0
    randint2 = 0

    run = True
    loose = False
    ####################################################################### main loop
    while True:
        if loose == True:
            defeat()

        score = a // 60  #'a' points per second       <---- score counter

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == Bonus_on:
                bonus_fl = True

        if run == True: #USELESS FLAG NEVERMIND
            # -------------------------------------------------------------------------
            #jump
            butt = pygame.key.get_pressed()
            if jump_fl is False and butt[pygame.K_SPACE]:
                jump_fl = True

            if jump_fl is True:
                hero_rect.y -= vel_y
                vel_y -= 1
                if vel_y < -22:
                    jump_fl = False
                    vel_y = 22
            #end jump

            if butt[pygame.K_LEFT]:
                hero_rect.x -= 4

            if butt[pygame.K_RIGHT]:
                hero_rect.x += 4

            if hero_rect.x <= 0:
                hero_rect.x = 0
            if hero_rect.x >=1220:
                hero_rect.x = 1220


        #collision
            if hero_rect.colliderect(enemy_rect) and loose == False:
                loose = True
            if hero_rect.colliderect(enemy2_rect) and loose == False:
                loose = True

            if hero_rect.colliderect(bonus_rect):
                extra_score += 10
            if hero_rect.colliderect(bonus_rect) and bonus == elon_good:
                extra_score += 40
            if hero_rect.colliderect(bonus_rect) and bonus == elon_bad:
                extra_score -= 110


            #ground moving
            sc.blit(bg_img, (0, 0))
            sc.blit(ground_img, (i, 0))
            sc.blit(ground_img, (W + i, 0))
            if i == -W:
                sc.blit(ground_img, (W + i, 0))
                i = 0
            i -= 1

            #hero blit
            sc.blit(hero_img, hero_rect)

            #enemy blit and move
            sc.blit(enemy1, enemy_rect)
            enemy_rect.x -= enemy_speed
            if enemy_rect.x <= -150:
                enemy1 = random.choice(enemy_list)
                enemy_rect = enemy1.get_rect(midbottom=(1300, 550))
                enemy_rect.x = 1300 + randint2
                randint2 = random.randint(0, 200)
            sc.blit(enemy2, enemy2_rect)
            enemy2_rect.x -= enemy_speed
            if enemy2_rect.x <= -150:
                enemy2 = random.choice(enemy_list)
                enemy2_rect = enemy2.get_rect(midbottom=(1400, 550))
                enemy2_rect.x = 1400 + randint
                randint = random.randint(600, 1100)


            #bonus staff
            if bonus_rect.x <= -100 or hero_rect.colliderect(bonus_rect):
                bonus_fl = False
                bonus = random.choice(bonus_list)
                bonus_rect = bonus.get_rect(midbottom=(1400, 330))
                bonus_rect.x = 1300

            if bonus_fl:
                sc.blit(bonus, bonus_rect)
                bonus_rect.x -= 10

            #bonus ends
            #score blit and render
            font = pygame.font.SysFont('arial', 30)
            text = font.render('Score: ' + str(score), True, (0,0,0))
            sc.blit(text, (10, 10))
            text1 = font.render('Binance savings: ' + str(extra_score) + 'BTC', True, (0, 0, 0))
            sc.blit(text1, (10, 40))

            #game speed
            if score // 11 and enemy_speed <= 15:
                enemy_speed += 0.003

            #tutorial imput
            if tutor and score <=3:
                sc.blit(tutor_img, (450, 50))
            else:
                tutor = False

            a += 1
            pygame.display.update()
            clock.tick(fps)

menu()


