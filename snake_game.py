import pygame
import time
import random


pygame.init()
pygame.mixer.init()

dis = pygame.display.set_mode([800,600])
pygame.display.set_caption("Snake Game Starting Menu !")

FPS = 60
fpsClock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

def First_line():
	start_point = 0,10
	end_point = 800,10

	pygame.draw.line(dis, green, start_point, end_point, 1)

def Second_line():
	start_point = 0, 100 
	end_point = 800, 100

	pygame.draw.line(dis, green, start_point, end_point, 5)

# def Game_open():
# 	first_image = pygame.image.load(r"")

# def Game_start():
# 	start_image = pygame.image.load(r"") 

def eat():
	pygame.mixer.music.load("beep.wav")
	pygame.mixer.music.play()

def death():
	pygame.mixer.music.load("death_sound.mp3")
	pygame.mixer.music.play()

def game_sound():
	pygame.mixer.music.load("game_audio.mp3")
	pygame.mixer.music.play(1)

font = pygame.font.SysFont('Forte', 50)	
start_button = font.render("Start", True, green)
quit_button = font.render("Quit", True, green)
Top_text = font.render("SNAKE GAME", True, red)


click = False
game_sound()
def main_menu():


	while True:

		game_sound()

		dis.fill(black)
		dis.blit(Top_text,[248,27])
		#dis.blit(text,[0,0])

		First_line()
		Second_line()

		mox, moy = pygame.mouse.get_pos()
	    
	    #----------pygame.Rect(x, y, width, height)
		button_1 = pygame.Rect(299, 241, 200, 75)
		button_2 = pygame.Rect(299, 411, 200, 75)

		pygame.draw.rect(dis, red, button_1 )
		pygame.draw.rect(dis, red, button_2 )


		if button_1.collidepoint((mox, moy)):
			if click:
				Start()
		if button_2.collidepoint([mox, moy]):
			if click:
				Quit()
		'''if button_3.collidepoint([mox, moy]):
			if click:
				Difficulty()'''

		dis.blit(start_button, [345, 248])
		dis.blit(quit_button, [345,422])

		click = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		fpsClock.tick(FPS)


def Start():
	game_sound()
	click = False

	running = True

	while running:

		font1 = pygame.font.SysFont('Forte', 60)
		font2 = pygame.font.SysFont('Forte', 20)
		font3 = pygame.font.SysFont("Lucida Fax" ,30)


		start_menu = font1.render("Main Menu", True, red)
		esc_exit = font2.render("ESC(Back)", True, white)
		button_1_text = font3.render("EASY", True, white)
		button_2_text = font3.render("MEDIUM", True, white)
		button_3_text = font3.render("IMPOSSIBLE", True, white)
		
		dis.fill(black)

		First_line()
		Second_line()

		mox, moy = pygame.mouse.get_pos()

		dis.blit(start_menu,[250,27])
		dis.blit(esc_exit, [0,10])

	    #----------pygame.Rect(x, y, width, height)
		button_3 = pygame.Rect(297, 170, 200, 75)
		button_4 = pygame.Rect(297, 285, 200, 75)
		button_5 = pygame.Rect(297, 400, 200, 75)

		pygame.draw.rect(dis, red, button_3)
		pygame.draw.rect(dis, red, button_4)
		pygame.draw.rect(dis, red, button_5)

		dis.blit(button_1_text, [358, 190])
		dis.blit(button_2_text, [326, 305])
		dis.blit(button_3_text, [305, 420])

		if button_3.collidepoint([mox, moy]):
			if click:
				easy() 

		if button_4.collidepoint([mox, moy]):
			if click:
				medium()

		if button_5.collidepoint([mox, moy]):
			if click:
				impossible()

		click = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		fpsClock.tick(FPS)

def easy():
	 
	dis_width = 800 
	dis_height = 600

	easy_fps = 20
	fpsClock = pygame.time.Clock()

	dis = pygame.display.set_mode([dis_width,dis_height])
	pygame.display.set_caption("Snake Game ")

	snake_block = 20


	score_font = pygame.font.SysFont("Algerian", 35)
	finish_font = pygame.font.SysFont("copper", 55)

	back_image = pygame.image.load("back_ground2.jpg")
	game_finish = pygame.image.load("finish.jpg")
	 
	last_score = pygame.font.SysFont("Algerian", 35)
	finish_score = last_score.render("Your Score", True, black)

	def Your_score(score):
	    value = score_font.render("Your Score: " + str(score), True, red)
	    dis.blit(value, [20, 20])
	           
	def our_snake(snake_block, snake_list):
	    for x in snake_list:
	        #dis.blit(snake_logo,[x[0], x[1], snake_block, snake_block])

	        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
	 
	def message(msg, color):
	    mesg = finish_font.render(msg, True, color)
	    dis.blit(mesg, [130, 468])
	 
	 
	def gameLoop():

	    game_over = False
	    game_close = False
	 
	    x1 = dis_width / 2
	    y1 = dis_height / 2
	 
	    x1_change = 0
	    y1_change = 0
	 
	    snake_List = []
	    Length_of_snake = 1
	 
	    foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
	    foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20
	 

	    while not game_over:
	 
	        while game_close == True:

	            dis.blit(game_finish,[-130,0])

	            message("Press C-Play Again or Q-Quit", white)
	            Your_score(Length_of_snake - 1)

	            pygame.display.update()
	 
	            for event in pygame.event.get():
	                if event.type == pygame.KEYDOWN:
	                    if event.key == pygame.K_q:
	                        game_over = True
	                        game_close = False
	                    if event.key == pygame.K_c:
	                        gameLoop()
	                    if event.type == pygame.QUIT:
	                        game_over = True

	                    if event.type == pygame.KEYDOWN:
	                        if event.key == pygame.K_ESCAPE:
	                            pygame.quit()
	                            quit()
	 
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                game_over = True

	            if event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_LEFT:
	                    x1_change = -snake_block
	                    y1_change = 0
	                elif event.key == pygame.K_RIGHT:
	                    x1_change = snake_block
	                    y1_change = 0
	                elif event.key == pygame.K_UP:
	                    y1_change = -snake_block
	                    x1_change = 0
	                elif event.key == pygame.K_DOWN:
	                    y1_change = snake_block
	                    x1_change = 0
	 
	        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
	            # pygame.mixer.music.load("death_sound.mp3")
	            # pygame.mixer.music.play()
	            death()
	            game_close = True
	            

	        x1 += x1_change
	        y1 += y1_change
	    
	        dis.blit(back_image,[0,0])

	        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
	        #pygame.draw.circle(dis, white, [foodx, foody], 15,0)

	        snake_Head = []
	        snake_Head.append(x1)
	        snake_Head.append(y1)
	        snake_List.append(snake_Head)

	        if len(snake_List) > Length_of_snake:
	            del snake_List[0]
	 
	        for x in snake_List[:-1]:
	            if x == snake_Head:
	                game_close = True
	 
	        our_snake(snake_block, snake_List)
	        Your_score(Length_of_snake - 1)
	         
	        pygame.display.update()
	 
	        if x1 == foodx and y1 == foody:

	            # pygame.mixer.music.load("beep.wav")
	            # pygame.mixer.music.play()
	            eat()

	            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
	            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
	            Length_of_snake += 1
	             
	            if event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_ESCAPE:
	                    pygame.quit()
	                    quit()        
	            

	        fpsClock.tick(easy_fps)
	 
	    pygame.quit()
	    quit()
	 
	 
	gameLoop()


def medium():

	dis_width = 800 
	dis_height = 600

	medium_fps = 30
	fpsClock = pygame.time.Clock()

	dis = pygame.display.set_mode([dis_width,dis_height])
	pygame.display.set_caption("Snake Game ")

	snake_block = 20


	score_font = pygame.font.SysFont("Algerian", 35)
	finish_font = pygame.font.SysFont("copper", 55)

	back_image = pygame.image.load("back_ground2.jpg")
	game_finish = pygame.image.load("finish.jpg")
	 
	last_score = pygame.font.SysFont("Algerian", 35)
	finish_score = last_score.render("Your Score", True, black)

	def Your_score(score):
	    value = score_font.render("Your Score: " + str(score), True, red)
	    dis.blit(value, [20, 20])
	           
	def our_snake(snake_block, snake_list):
	    for x in snake_list:
	        #dis.blit(snake_logo,[x[0], x[1], snake_block, snake_block])

	        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
	 
	def message(msg, color):
	    mesg = finish_font.render(msg, True, color)
	    dis.blit(mesg, [130, 468])
	 
	 
	def gameLoop():

	    game_over = False
	    game_close = False
	 
	    x1 = dis_width / 2
	    y1 = dis_height / 2
	 
	    x1_change = 0
	    y1_change = 0
	 
	    snake_List = []
	    Length_of_snake = 1
	 
	    foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
	    foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20
	 

	    while not game_over:
	 
	        while game_close == True:

	            dis.blit(game_finish,[-130,0])

	            message("Press C-Play Again or Q-Quit", white)
	            Your_score(Length_of_snake - 1)

	            pygame.display.update()
	 
	            for event in pygame.event.get():
	                if event.type == pygame.KEYDOWN:
	                    if event.key == pygame.K_q:
	                        game_over = True
	                        game_close = False
	                    if event.key == pygame.K_c:
	                        gameLoop()
	                    if event.type == pygame.QUIT:
	                        game_over = True

	                    if event.type == pygame.KEYDOWN:
	                        if event.key == pygame.K_ESCAPE:
	                            pygame.quit()
	                            quit()
	 
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                game_over = True

	            if event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_LEFT:
	                    x1_change = -snake_block
	                    y1_change = 0
	                elif event.key == pygame.K_RIGHT:
	                    x1_change = snake_block
	                    y1_change = 0
	                elif event.key == pygame.K_UP:
	                    y1_change = -snake_block
	                    x1_change = 0
	                elif event.key == pygame.K_DOWN:
	                    y1_change = snake_block
	                    x1_change = 0
	 
	        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:

	            # pygame.mixer.music.load("death_sound.mp3")
	            # pygame.mixer.music.play()
	            death()
	            game_close = True
	            

	        x1 += x1_change
	        y1 += y1_change
	    
	        dis.blit(back_image,[0,0])

	        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
	        #pygame.draw.circle(dis, white, [foodx, foody], 15,0)

	        snake_Head = []
	        snake_Head.append(x1)
	        snake_Head.append(y1)
	        snake_List.append(snake_Head)

	        if len(snake_List) > Length_of_snake:
	            del snake_List[0]
	 
	        for x in snake_List[:-1]:
	            if x == snake_Head:
	                game_close = True
	 
	        our_snake(snake_block, snake_List)
	        Your_score(Length_of_snake - 1)
	         
	        pygame.display.update()
	 
	        if x1 == foodx and y1 == foody:

	            # pygame.mixer.music.load("beep.wav")
	            # pygame.mixer.music.play()
	            eat()

	            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
	            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
	            Length_of_snake += 1
	             
	            if event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_ESCAPE:
	                    pygame.quit()
	                    quit()        
	            

	        fpsClock.tick(medium_fps)
	 
	    pygame.quit()
	    quit()
	 
	 
	gameLoop()


def impossible():

	dis_width = 800 
	dis_height = 600

	impossible_fps = 40
	fpsClock = pygame.time.Clock()

	dis = pygame.display.set_mode([dis_width,dis_height])
	pygame.display.set_caption("Snake Game ")

	snake_block = 20


	score_font = pygame.font.SysFont("Algerian", 35)
	finish_font = pygame.font.SysFont("copper", 55)

	back_image = pygame.image.load("back_ground2.jpg")
	game_finish = pygame.image.load("finish.jpg")
	 
	last_score = pygame.font.SysFont("Algerian", 35)
	finish_score = last_score.render("Your Score", True, black)

	def Your_score(score):
	    value = score_font.render("Your Score: " + str(score), True, red)
	    dis.blit(value, [20, 20])
	           
	def our_snake(snake_block, snake_list):
	    for x in snake_list:
	        #dis.blit(snake_logo,[x[0], x[1], snake_block, snake_block])

	        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
	 
	def message(msg, color):
	    mesg = finish_font.render(msg, True, color)
	    dis.blit(mesg, [130, 468])
	 
	 
	def gameLoop():

	    game_over = False
	    game_close = False
	 
	    x1 = dis_width / 2
	    y1 = dis_height / 2
	 
	    x1_change = 0
	    y1_change = 0
	 
	    snake_List = []
	    Length_of_snake = 1
	 
	    foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
	    foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20
	 

	    while not game_over:
	 
	        while game_close == True:

	            dis.blit(game_finish,[-130,0])

	            message("Press C-Play Again or Q-Quit", white)
	            Your_score(Length_of_snake - 1)

	            pygame.display.update()
	 
	            for event in pygame.event.get():
	                if event.type == pygame.KEYDOWN:
	                    if event.key == pygame.K_q:
	                        game_over = True
	                        game_close = False
	                    if event.key == pygame.K_c:
	                        gameLoop()
	                    if event.type == pygame.QUIT:
	                        game_over = True

	                    if event.type == pygame.KEYDOWN:
	                        if event.key == pygame.K_ESCAPE:
	                            pygame.quit()
	                            quit()
	 
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                game_over = True

	            if event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_LEFT:
	                    x1_change = -snake_block
	                    y1_change = 0
	                elif event.key == pygame.K_RIGHT:
	                    x1_change = snake_block
	                    y1_change = 0
	                elif event.key == pygame.K_UP:
	                    y1_change = -snake_block
	                    x1_change = 0
	                elif event.key == pygame.K_DOWN:
	                    y1_change = snake_block
	                    x1_change = 0
	 
	        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:

	            # pygame.mixer.music.load("death_sound.mp3")
	            # pygame.mixer.music.play()
	            death()
	            game_close = True
	            

	        x1 += x1_change
	        y1 += y1_change
	    
	        dis.blit(back_image,[0,0])

	        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
	        #pygame.draw.circle(dis, white, [foodx, foody], 15,0)

	        snake_Head = []
	        snake_Head.append(x1)
	        snake_Head.append(y1)
	        snake_List.append(snake_Head)

	        if len(snake_List) > Length_of_snake:
	            del snake_List[0]
	 
	        for x in snake_List[:-1]:
	            if x == snake_Head:
	                game_close = True
	 
	        our_snake(snake_block, snake_List)
	        Your_score(Length_of_snake - 1)
	         
	        pygame.display.update()
	 
	        if x1 == foodx and y1 == foody:

	            # pygame.mixer.music.load("beep.wav")
	            # pygame.mixer.music.play()
	            eat()

	            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
	            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
	            Length_of_snake += 1
	             
	            if event.type == pygame.KEYDOWN:
	                if event.key == pygame.K_ESCAPE:
	                    pygame.quit()
	                    quit()        
	            

	        fpsClock.tick(impossible_fps)
	 
	    pygame.quit()
	    quit()
	 
	 
	gameLoop()



def Quit():

	while True:

		pygame.quit()
		quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

		pygame.display.update()
		fpsClock.tick(FPS)


main_menu()

















