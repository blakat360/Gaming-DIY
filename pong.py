import pygame
import random

pygame.init

def init_ball(x, y):	#generate initial velocity of ball
	return random.choice([1,-1]) * random.randint(x,y)
	

white = (255, 255, 255)
black = (0, 0, 0)
window_height = 500
window_width = 700
paddle_width = 12
paddle_height = 0.15 * window_height
paddle_buffer = 10 + paddle_width/2
paddle_speed = 5
player1_input = 0
player2_input = 0
ball_radius = 5
ball_Xpos = (window_width - ball_radius)/2
ball_Ypos = (window_height - ball_radius)/2
ball_Xvel = init_ball(2,3)
ball_Yvel = init_ball(1,2)
p1_won = False
p2_won = False
Clock = pygame.time.Clock()
frame_rate = 60

win = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Pong")

while not p1_won and not p2_won:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_w]:	#player one's input
		if window_height/2 - paddle_height/2 - player1_input >= 0:
			player1_input += paddle_speed
	if keys[pygame.K_s]:
		if window_height/2 + paddle_height/2 - player1_input <= window_height:
			player1_input += - paddle_speed
	
	
	if keys[pygame.K_UP]:	#player two's input
		if window_height/2 - paddle_height/2 - player2_input >= 0:
			player2_input += paddle_speed
	if keys[pygame.K_DOWN]:
		if window_height/2 + paddle_height/2 - player2_input <= window_height:
			player2_input += - paddle_speed
	
	win.fill(black)
	
	
	if ball_Ypos <= 0 or ball_Ypos >= window_height: #check if ball is touching bottom or top edges of screen
		ball_Yvel = -1 * ball_Yvel
	
	if ball_Ypos >= window_height/2 - paddle_height/2 - player1_input and ball_Ypos <= window_height/2 + paddle_height/2 - player1_input:
		if ball_Xpos >= paddle_buffer - paddle_width/2 and ball_Xpos <= paddle_buffer + paddle_width/2:
			if abs(ball_Xvel) < paddle_width:
				ball_Xvel = (-1 * ball_Xvel) + 1
				paddle_speed += 0.5
			else:
				ball_Xvel = (-1 * ball_Xvel)
			
	if ball_Ypos >= window_height/2 - paddle_height/2 - player2_input and ball_Ypos <= window_height/2 + paddle_height/2 - player2_input:
		if ball_Xpos >= window_width - paddle_buffer - paddle_width and ball_Xpos <= window_width - paddle_buffer:
			if abs(ball_Xvel) < paddle_width:
				ball_Xvel = (-1 * ball_Xvel) - 1
				paddle_speed += 0.5
			else:
				ball_Xvel = (-1 * ball_Xvel)
				
	ball_Xpos += ball_Xvel
	ball_Ypos += ball_Yvel
	pygame.draw.rect(win, white, #redraw ball
				  (ball_Xpos, ball_Ypos, ball_radius, ball_radius))
	
	
	pygame.draw.rect(win, white, #redraw player one's paddle
				  (paddle_buffer, window_height/2 - paddle_height/2 - player1_input,
			      paddle_width, paddle_height))
	
	
	pygame.draw.rect(win, white, #redraw player two's paddle
				  (window_width - paddle_buffer - paddle_width, window_height/2 - paddle_height/2 - player2_input,
			      paddle_width, paddle_height))
	
	if ball_Xpos <= 0:
		p2_won = True
	elif ball_Xpos >= window_width:
		p1_won = True
		
	pygame.display.update()
	Clock.tick(frame_rate)
	
print(ball_Xvel)		
pygame.quit()
