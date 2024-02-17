#import...
import pgzrun
import pygame
from typing import List, Tuple
import os
import random
import keyboard
import math
import time
from pgzhelper import *




#base app
os.environ["SDL_VIDEO_CENTERED"] = '1'
TITLE = "Olders Game"
WIDTH = 1000
HEIGHT = 700

#-------------

gap = random.randint(50, 150)

#-------------


#call images with Actor.
Menu = Actor('menu_game_1', (500 , 350 ))
Menu.images = ['menu_game_2','menu_game_3','menu_game_4']
Menu.fps = 9999

music_on = Actor('music_active', (500,350))
music_off = Actor('music_mute', (500,350))

olders_game = Actor('oleders_game', (470 , 580 ))

button_soccer = Actor('game_1', (960 , 130 ))
button_soccer.images = ['game_1','game_1_min']
button_soccer.fps = 60

pixel_button = Actor('pixel_button', (960 , 200))
pixel_button.images = ['game_1','game_1_min']
pixel_button.fps = 60

button_jumpy_game = Actor('jump_game', (960 , 270 ))
button_jumpy_game.images = ['game_1','game_1_min']
button_jumpy_game.fps = 60


setting_button = Actor('setting', (960 , 340))
setting_button.images = ['setting_2','setting_3']
setting_button.fps = 60

setting_part1 = Actor('setting_part', (500 , 300))

explain_game = Actor('about_game', (500,150))

reminder_button = Actor('reminder', (300,350))

developed_1 = Actor('developer_s' , (500,150))
 
developed_button = Actor('developer_btn', (400, 350))

button_pos = (0,0)

Exit_meno = Actor('exit_meno', (50 , 50 ))


stadium_1 = Actor('stadium_1', (500 , 350 ))
stadium_2 = Actor('stadium_2', (500 , 350 ))
player1 = Actor('player_1', (500, 620))
player2 = Actor('player_2', (500, 90))
player3 = Actor('player_3', (676.0, 252.0))
ball = Actor('ball_1', (500, 350))
goal = Actor('goal', (500.0, 15.0))
end_time = Actor('winner_football_1', (500.0, 300.0))
rule_football = Actor('rule_football', (500.0, 350.0))
button_1 = Actor('rule_button', (810.0, 110.0))
button_1.images = ['rule_button_1','rule_button_2']
button_1.fps = 60
button_ready = Actor('ready_button1', (500, 300))

button_yes = Actor('yes', (500, 400))


button_2 = Actor('exit_button1', (200, 50))

bg = Actor('bgg', (500, 350))

exit_jumpy = Actor('exit_button1_jumpy', (950,50))

bird = Actor('bird', (100,200))
bird.images = ['bird', 'bird1', 'bird2', 'bird3']
bird_dead = Actor('birddead', (0, 0))
bird.fps = 10

game_over1 = Actor('gameover', (500, 300))
game_over1.scale = 0.5

top_pipe = Actor('top', (WIDTH, -100))
bottom_pipe = Actor('bottom', (WIDTH, top_pipe.height + gap))


#score get points random from here.
point_list = random.randrange(3,5)

#time_part.
start_time = time.time()

#score_part.
score = 0

#speed_part.

speed_player_1 = 8
speed_ball = 10
speed_player_2 = 5
speed_player_3 = 7
bird_speed = 1
gravity = 0.1
scroll_speed = -3.75 #pipe speed

#time_part.
elapsed_time = time.time() - start_time
minutes, seconds = divmod(elapsed_time, 60)


#etc.



#all bools.

timer_running = False

Soccer_Stars = False

start_game_bool = False

Ready_1 = False

game_over = False

rule_1 = False

pixel_game = False

setting_1 = False

dev = False

dev_1 = False

sound_all = False

text_1 = False
text_2 = False
text_3 = False
text_4 = False
text_5 = False

alive = True

jumpy = False
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
pygame.init()

# Set window size and title
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define snake and food properties
snake_block_size = 10
snake_speed = 15

# Define font for displaying score
font_style = pygame.font.SysFont(None, 30)

#---------------------------------------------------------------------------------------------------------

def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, black)
    window.blit(score_text, [10, 10])

def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])


#---------------------------------------------------------------------------------------------------------
# start using any def we need .
def update():
    global player1, game_over, speed_player_1, ball,bird_speed, alive, bird, gravity, gap, score, timer_running ,score, player2, speed_player_2, end_time, start_time, minutes, seconds, speed_player_3, rule_1, button_1, button_min

    Menu.animate()
    Menu == Menu.images

    #for soccer start game before game start
    if start_game_bool:
        button_ready.x = button_yes.x = 1500
    else :
        button_ready.x = 500
        button_yes.x = 500

    # Player 1 movement
    movement = {
        'right': (speed_player_1, 0),
        'left': (-speed_player_1, 0),
        'up': (0, -speed_player_1),
        'down': (0, speed_player_1)
    }
    for key, (dx, dy) in movement.items():
        if keyboard.is_pressed(key):
            player1.x = max(326, min(676, player1.x + dx))
            player1.y = max(76, min(629, player1.y + dy))

    # Player 2 movement
    player2.x += speed_player_2
    player2.x = max(320, min(670, player2.x))
    speed_player_2 *= -1 if player2.x in (320, 670) else 1

    # Player 3 movement
    player3.x += speed_player_3
    player3.x = max(500, min(676, player3.x))
    speed_player_3 *= -1 if player3.x in (500, 676) else 1

    ball.x = max(320, min(670, ball.x))

    # Player 1 holding ball
    if player1.colliderect(ball) and keyboard.is_pressed('space'):
        player_x, player_y = player1.x, player1.y
        ball.x, ball.y = player_x + player1.width // -70, player_y + player1.height // -2.5
        vector_x, vector_y = ball.x - player_x, ball.y - player_y
        vector_length = math.hypot(vector_x, vector_y)
        if vector_length:
            normalized_vector_x, normalized_vector_y = vector_x / vector_length, vector_y / vector_length
            ball.x += normalized_vector_x * speed_ball
            ball.y += normalized_vector_y * speed_ball

    # Ball touch goal
    if ball.colliderect(goal):
        sounds.goal1.play()
        score += point_list
        ball.x, ball.y = 500, 350
        player1.x, player1.y = 500, 620

    # Ball touch player2
    if ball.colliderect(player2):
        score -= 3
        ball.x, ball.y = 500, 350
        player1.x, player1.y = 500, 500

    # Ball touch player3
    if ball.colliderect(player3):
        score -= 2
        ball.x, ball.y = 500, 350
        player1.x, player1.y = 500, 500

    #time.....
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    

    # Game over conditions
    if (time.time() - start_time) >= 60 or score >= 50 or score <= -50:
        game_over = True
        start_time = speed_player_1 = speed_player_2 = speed_player_3 = 0

        if game_over and keyboard.is_pressed('enter'):
            score = 0
            start_time = time.time()
            ball.x, ball.y = 500, 350
            player1.x, player1.y = 500, 620
            game_over = False
            speed_player_1, speed_player_2, speed_player_3 = 8, 5, 7



    #-----------------------------------------------------------------------------------------
    if jumpy :
        if alive == True:

            bird.animate()
            bird.y += bird_speed
            bird_speed += gravity
            if bird.y >= 520:
                alive = False
            if bird.y <= 2:
                alive = False
        
        top_pipe.x += scroll_speed
        bottom_pipe.x += scroll_speed
        
        if top_pipe.x < -50 :
            global respawn_gap
            respawn_gap = random.uniform(-50, -220)
            top_pipe.pos = (WIDTH, respawn_gap)
            bottom_pipe.pos = (WIDTH, respawn_gap + top_pipe.height + gap)
            score += 1
            if not  sound_all :
                sounds.point.play()
           # bottom_pipe.midleft(WIDTH, )
        if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
            alive = False
        if alive == False:
            bird_speed = 0
            bird.image = bird_dead.image
            bird.y = 200
            if not  sound_all :
                sounds.die.play()
        #---------------------------------------------
    #pixel  game 
    if pixel_game :
        #def for snake
        def snake_game():
            global pixel_game
            game_over = False
            game_close = False

    # Snake initial position and movement
            x1 = window_width / 2
            y1 = window_height / 2
            x1_change = 0
            y1_change = 0

            # Snake body
            snake_list = []
            length_of_snake = 1

            # Generate food position
            food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

            while not game_over:

                while game_close:
                    window.fill(white)
                    game_over_text = font_style.render("Game Over! Press Q-Quit game or C-Play Again", True, red)
                    window.blit(game_over_text, [window_width / 6, window_height / 2])
                    display_score(length_of_snake - 1)
                    pygame.display.update()

                    # Check user input to either quit the game or play again
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                                pixel_game = False
                            if event.key == pygame.K_c:
                                snake_game()

                # Event handling
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        pixel_game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block_size
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block_size
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block_size
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block_size
                            x1_change = 0

                # Check if snake hits the boundaries
                if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                window.fill(white)
                pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])
                snake_head = []
                snake_head.append(x1)
                snake_head.append(y1)
                snake_list.append(snake_head)
                if len(snake_list) > length_of_snake:
                    del snake_list[0]

                # Check if snake hits itself
                for x in snake_list[:-1]:
                    if x == snake_head:
                        game_close = True

                draw_snake(snake_block_size, snake_list)
                display_score(length_of_snake - 1)

                # Check if snake eats the food
                if x1 == food_x and y1 == food_y:
                    food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
                    food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
                    length_of_snake += 1

                pygame.display.update()

                # Set the movement speed of the snake
                clock = pygame.time.Clock()
                clock.tick(snake_speed)

            #pygame.quit()

        # Start the game
        snake_game()

    
            
    


#def draw our Actors
def draw():
    global minutes , seconds, start_game_bool , jumpy
    
    

    Menu.draw()
    olders_game.draw()
    button_soccer.draw()
    pixel_button.draw()
    setting_button.draw()
    button_jumpy_game.draw()
    Exit_meno.draw()

    if setting_1 :
        setting_part1.draw()
        reminder_button.draw()
        developed_button.draw()
        
        if sound_all :
            music_off.draw()
        elif not sound_all :
            music_on.draw()

        if dev :
            explain_game.draw()
        elif dev_1 :
            developed_1.draw()

    #soccer bool
    if Soccer_Stars:

        stadium_1.draw()
        stadium_2.draw()
        
        button_ready.draw()
        
        button_yes.draw()

        if start_game_bool == True :
            
            if Ready_1 == False :

                button_2.draw()
                player1.draw()
                player2.draw()
                player3.draw()
                ball.draw()
                goal.draw()
                button_1.draw()
                screen.draw.text(f"{int(minutes)}:{int(seconds)}", (880, 80), fontsize = 80, color = 'blue')
                screen.draw.text(f"{score}", (890.0,580.0), fontsize = 80, color = 'green')
            
                if game_over:
                    end_time.draw()
                    screen.draw.text(f"{score}", (540.0, 180.0), fontsize = 45, color = 'green')
                    
                    if not score >= 0 : 
                        screen.draw.text("You lost the match !", (415.0, 220.0), fontsize = 20, color = 'red')
                    elif score >= 0  : 
                        screen.draw.text("You won the match !", (415.0, 220.0), fontsize = 20, color = 'gold')
                    elif time == 60 and score >= 0 :
                        screen.draw.text("You lost the match !", (415.0, 220.0), fontsize = 20, color = 'red')

                if not score >= 0 :
                    screen.draw.text("..your score is going to fall , get up and fight.. !", (755.0, 550.0), fontsize = 15, color = 'white')

                if button_1 == True :
                    rule_1.draw()

                if rule_1 == True :
                    rule_football.draw()
            #
    if jumpy :
        bg.draw()
        
        if alive:
            bird.draw()
            top_pipe.draw()
            bottom_pipe.draw()
        else:
            game_over1.draw()
            screen.draw.text('Click to play again', color= 'white', center= (500, 500), shadow= (0.5, 0.5), scolor= 'black')
            top_pipe.x = WIDTH
            bottom_pipe.x = WIDTH
            exit_jumpy.draw()

        screen.draw.text( f'Score:{score} ', color= 'white', midtop= (50,10), shadow= (0.5, 0.5), scolor= 'black', fontsize= 30, )

    if not Soccer_Stars and not jumpy :

        if text_1 :
            screen.draw.text("Soccer Star Game", (759 , 118), fontsize = 30, color = 'white')
        elif text_2 :
            screen.draw.text("Snake Game(pixel_mode)", (680 , 188), fontsize = 30, color = 'white')
        elif text_3 :
            screen.draw.text("Exit", (30 , 78), fontsize = 30, color = 'red')
        elif text_4 :
            screen.draw.text("Setting", (850 , 330), fontsize = 30, color = 'white')
        elif text_5 :
            screen.draw.text("Flappy Bird", (810 , 260), fontsize = 30, color = 'white')
#click mouse def
def on_mouse_down(pos):
    global rule_1,Exit_meno,bird_speed,jumpy, alive,score,music_off,music_on, button_1,text_3,sound_all,developed_1,dev,reminder_button,dev,dev_1, button_soccer ,setting_1,pixel_game ,pixel_button, Soccer_Stars, Ready_1, button_yes, button_ready, start_game_bool, start_time, timer_running
    


    if not Soccer_Stars :
    
        if Exit_meno.collidepoint(pos) :
            if not  sound_all :
                sounds.buttons_click.play()
            exit()

        
        elif pixel_button.collidepoint(pos) and pixel_game == False : 
            if not  sound_all :
                sounds.buttons_click.play()
            pixel_game = True


        elif button_soccer.collidepoint(pos) and Soccer_Stars == False :
            if not  sound_all :
                sounds.buttons_click.play()
            Ready_1 = True
            Soccer_Stars = True

        elif button_jumpy_game.collidepoint(pos) and jumpy == False :
            if not  sound_all :
                sounds.buttons_click.play()
            jumpy = True

        elif setting_button.collidepoint(pos) and setting_1 == False :
            if not  sound_all :
                sounds.buttons_click.play()
            setting_1 = True

        elif setting_button.collidepoint(pos) and setting_1 == True :
            if not  sound_all :
                sounds.buttons_click.play()
            setting_1 = False
        
        if reminder_button.collidepoint(pos) and dev == False : 
            if not  sound_all :
                sounds.buttons_click.play()
            dev = True

        elif reminder_button.collidepoint(pos) and dev == True :
            if not  sound_all :
                sounds.buttons_click.play()
            dev = False

        if developed_button.collidepoint(pos) and dev_1 == False : 
            if not  sound_all :
                sounds.buttons_click.play()
            dev_1 = True
        elif developed_button.collidepoint(pos) and dev_1 == True :
            if not  sound_all :
                sounds.buttons_click.play()
            dev_1 = False
        
        if music_on.collidepoint(pos) and sound_all == False :
            sound_all = True
        elif music_off.collidepoint(pos) and sound_all == True :
            sound_all = False


    if button_yes.collidepoint(pos) and Ready_1 == True :
        if not  sound_all :
            sounds.buttons_click.play()

        start_time = time.time()
        timer_running = True
        start_game_bool = True
        Ready_1 = False

    if Soccer_Stars :

        if button_1.collidepoint(pos) and rule_1 == False :

            if not  sound_all :
                sounds.buttons_click.play()

            rule_1 = True

        elif button_1.collidepoint(pos) and rule_1 ==True :

            if not  sound_all :
                sounds.buttons_click.play()

            rule_1 = False

        if button_2.collidepoint(pos):
            if not  sound_all :
                sounds.buttons_click.play()
            
            Soccer_Stars = False
            start_game_bool = False

    if jumpy :
        
        if alive:
            bird_speed -=6.5
            if not  sound_all :
                sounds.wing.play()
        else:
            alive = True
            bird.x = 100
            bird.y = 200
            score = 0
        if exit_jumpy.collidepoint(pos) :
           jumpy = False

#move mouse def for our effects
def on_mouse_move(pos):
    global  rule_1, button_1, button_soccer, button_pos, pixel_button , text_1, text_2, text_3, text_4, text_5

    button_pos = pos

    if Exit_meno.collidepoint(pos) :
        text_3 = True
    else :
        text_3 = False



    if setting_button.collidepoint(pos) :
        setting_button.animate()
        text_4 = True
    else :
        setting_button.image = 'setting'
        text_4 = False

    if button_soccer.collidepoint(pos) :
        button_soccer.animate()
        text_1 = True
    else :
        button_soccer.image = 'game_1'
        text_1 = False

    if pixel_button.collidepoint(pos) :
        pixel_button.animate()
        text_2 = True
    else :
        pixel_button.image = 'pixel_button'
        text_2 = False

    if button_jumpy_game.collidepoint(pos) :
        button_jumpy_game.animate()
        text_5 = True
    else :
        button_jumpy_game.image = 'jump_game'
        text_5 = False
    if Soccer_Stars :
        if button_1.collidepoint(pos) :
            button_1.animate()
        




#to run the code.
pgzrun.go()