import pygame
import pygame.locals
import random
import time

debug = False

# These are just shortcuts for the different colors I use.
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
white = (255,255,255)

players = int(raw_input("How many players? (1, 2, 3, or 4) ")) # Self explanatory.

# Help System
##############################################################################################
help = raw_input("Review controls? (Type \"yes\" or \"no\") ")
if help == "yes":
	if players == 1:
		print "Up: Up Arrow\nDown: Down Arrow\n"
	if players == 2:
		print "P1:\n\tUp: A\n\tDown: Z\n\nP2:\n\tUp: Up Arrow\n\tDown: Down Arrow\n"
	if players >= 3:
		print "P1:\n\tUp: A\n\tDown: Z\n\nP2:\n\tUp: P\n\tDown: L\n\nP3:\n\tLeft: Q\n\tRight: W\n"
		if players == 4:
			print "P4:\n\tLeft: N\n\tRight: M\n"
##############################################################################################

# Solo Game
##############################################################################################
if players == 1:
	vscomp = raw_input("Vs. Computer? (Type \"yes\" or \"no\") ")

	# Practice Mode
	if vscomp != "yes":
		ballspeed = int(raw_input("Ball speed? (5 recommended) "))
		if ballspeed == -100:
			ballspeed = 5
			print "\nDebug Mode Activated\nBall only moves if \"Y\" is pushed\n"
			debug = True
	
		score1 = 0
		height = int(raw_input("Height? (800 reccomended) "))
		width = int(raw_input("Width? (800 recommended) "))
	
		pygame.init()
		myWindow = pygame.display.set_mode((width,height))
		pygame.display.set_caption("Ultimate Pong: Practice")
	
		myCanvas = pygame.Surface(myWindow.get_size())
		myCanvas.fill((0,0,0))
	
		myClock = pygame.time.Clock()
	
		myFont = pygame.font.Font(None,48)
	
		score1display = myFont.render(str(score1),True,(255,255,255))
		score1rect = score1display.get_rect()
		score1rect.centerx = width - 24
		score1rect.centery = height / 2
		
		player1y = ((height / 2) - 100)
	
		ballx = (height / 2) - 25
		bally = (height / 2) - 50
		ballxvel = random.choice([ballspeed,-1*ballspeed])
		ballyvel = random.choice([ballspeed,-1*ballspeed])
	
		myCanvas.fill((0,0,0))
		pygame.draw.rect(myCanvas,(255,255,255),(100,player1y,20,100),0)
		pygame.draw.rect(myCanvas,(255,255,255),(ballx,bally,20,20),0)
		myWindow.blit(myCanvas,(0,0))
		myWindow.blit(score1display,score1rect)
		pygame.display.flip()
		time.sleep(1)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print "\nFinal Score:",score1
					print
					exit()
			myClock.tick(50)
		
			# Drawing the field, players, score, and ball
			myCanvas.fill((0,0,0))
			pygame.draw.rect(myCanvas,(255,255,255),(100,player1y,20,100),0)
			pygame.draw.rect(myCanvas,(255,255,255),(ballx,bally,20,20),0)
			myWindow.blit(myCanvas,(0,0))
			myWindow.blit(score1display,score1rect)
			pygame.display.flip()
	
			# Displaying score
			score1display = myFont.render(str(score1),True,(255,255,255))
			score1rect = score1display.get_rect()
			score1rect.centerx = width - 24
			score1rect.centery = width / 2
		
			# End game if ball leaves field
			if ballx <= -20:
				time.sleep(1)
				print "\nFinal Score:",score1
				print
				exit()
		
			keys = pygame.key.get_pressed()
	
			# Player 1 (left)
			if keys[pygame.locals.K_UP] == True and player1y >= 0:
				player1y -= 10
			if keys[pygame.locals.K_DOWN] == True and player1y <= (height - 100):
				player1y += 10
	
			# Moving The Ball
			if bally <= 0 or bally >= (height - 20):
				if ballx > 100:
					ballyvel = ballyvel * -1
			if ballx >= (width - 20):
				ballxvel = ballxvel * -1
			if ballx >= 100 and ballx <= 120 and bally >= player1y and bally <= (player1y + 80):
				ballxvel = ballxvel * -1
				ballx = 120
	                        score1 += 1 # This keeps score, but I put it under ball movement. Don't ask.
	
			if debug == False:
				ballx += ballxvel
				bally += ballyvel
			elif keys[pygame.locals.K_y] == True:
				ballx += ballxvel
				bally += ballyvel
	# Vs. Computer
	elif vscomp == "yes":
		ballspeed = int(raw_input("Ball speed? (5 recommended) "))
		if ballspeed == -100:
			ballspeed = 5
			print "\nDebug Mode Activated\nBall only moves if \"Y\" is pushed\n"
			debug = True
	
		score1 = 0
		score2 = 0
		if debug == False:
			height = int(raw_input("Height? (800 reccomended) "))
			width = int(raw_input("Width? (800 recommended) "))
		else:
			height = int(raw_input("Height? (800 reccomended) "))
			width = int(raw_input("Width? (800 recommended) "))
	
		pygame.init()
		myWindow = pygame.display.set_mode((width,height))
		pygame.display.set_caption("Ultimate Pong: 1P (Vs. CPU)")
	
		myCanvas = pygame.Surface(myWindow.get_size())
		myCanvas.fill((0,0,0))
	
		myClock = pygame.time.Clock()
	
		myFont = pygame.font.Font(None,48)
	
		score1display = myFont.render(str(score1),True,(255,255,255))
		score1rect = score1display.get_rect()
		score2display = myFont.render(str(score2),True,(255,255,255))
		score2rect = score2display.get_rect()
		score1rect.centerx = (width / 4)
		score1rect.centery = 24
		score2rect.centerx = ((width / 4) * 3)
		score2rect.centery = 24
	
		player1y = ((height / 2) - 100)
		player2y = ((height / 2) - 100)
	
		ballx = (height / 2) - 25
		bally = (height / 2) - 50
		ballxvel = random.choice([ballspeed,-1*ballspeed])
		ballyvel = random.choice([ballspeed,-1*ballspeed])
	
		myCanvas.fill((0,0,0))
		pygame.draw.rect(myCanvas,(255,255,255),(100,player1y,20,100),0)
		pygame.draw.rect(myCanvas,(255,255,255),((width - 120),player2y,20,100),0)
		pygame.draw.rect(myCanvas,(255,255,255),(ballx,bally,20,20),0)
		myWindow.blit(myCanvas,(0,0))
		myWindow.blit(score1display,score1rect)
		myWindow.blit(score2display,score2rect)
		pygame.display.flip()
		time.sleep(1)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print "\nFinal Scores\n\tP1:",score1,"\n\tCPU:",score2
					if score1 > score2:
						print "P1 wins!"
					if score1 < score2:
						print "CPU wins!"
					if score1 == score2:
						print "Tie"
					exit()
			myClock.tick(50)
		
			# Drawing the field, players, score, and ball
			myCanvas.fill((0,0,0))
			pygame.draw.rect(myCanvas,(255,255,255),(100,player1y,20,100),0)
			pygame.draw.rect(myCanvas,(255,255,255),((width - 120),player2y,20,100),0)
			pygame.draw.rect(myCanvas,(255,255,255),(ballx,bally,20,20),0)
			myWindow.blit(myCanvas,(0,0))
			myWindow.blit(score1display,score1rect)
			myWindow.blit(score2display,score2rect)
			pygame.display.flip()
	
			# Keeping score
			if ballx <= -20:
				score2 += 1
			if ballx >= (width + 20):
				score1 += 1
			score1display = myFont.render(str(score1),True,white)
			score1rect = score1display.get_rect()
			score2display = myFont.render(str(score2),True,white)
			score2rect = score2display.get_rect()
			score1rect.centerx = (width / 4)
			score1rect.centery = 24
			score2rect.centerx = ((width / 4) * 3)
			score2rect.centery = 24
		
			# Reset if ball leaves field
			if ballx <= -20 or ballx >= (width + 20):
				time.sleep(1)
				player1y = ((height / 2) - 100)
				player2y = ((height / 2) - 100)
				ballx = (height / 2) - 25
				bally = (height / 2) - 50
				ballxvel = random.choice([ballspeed,-1*ballspeed])
				ballyvel = random.choice([ballspeed,-1*ballspeed])
		
			keys = pygame.key.get_pressed()
	
			# Player 1 (left)
			if keys[pygame.locals.K_UP] == True and player1y >= 0:
				player1y -= 10
			if keys[pygame.locals.K_DOWN] == True and player1y <= (height - 100):
				player1y += 10
	
			# Player 2 (right)
			if bally <= (player2y + 60) and player2y >= 0:
				player2y -= 10
			if bally >= (player2y + 60) == True and player2y <= (height - 100):
				player2y += 10
	
			# Moving The Ball
			if bally <= 0 or bally >= (height - 20):
				if ballx > 100 and ballx < (height - 120):
					ballyvel = ballyvel * -1
			if ballx >= 100 and ballx <= 120 and bally >= player1y and bally <= (player1y + 80):
				ballxvel = ballxvel * -1
				ballx = 120
			if (ballx + 20) >= (width - 120) and (ballx + 20) <= (width - 100) and bally >= player2y and bally <= (player2y + 80):
				ballx = width - 140
				ballxvel = ballxvel * -1
		
			if debug == False:
				ballx += ballxvel
				bally += ballyvel
			elif keys[pygame.locals.K_y] == True:
				ballx += ballxvel
				bally += ballyvel
##############################################################################################

# 2 Player Game
##############################################################################################
if players == 2:
	ballspeed = int(raw_input("Ball speed? (5 recommended) "))
	if ballspeed == -100:
		ballspeed = 5
		print "\nDebug Mode Activated\nBall only moves if \"Y\" is pushed\n"
		debug = True

	score1 = 0
	score2 = 0
	if debug == False:
		height = int(raw_input("Height? (800 reccomended) "))
		width = int(raw_input("Width? (800 recommended) "))
	else:
		height = int(raw_input("Height? (800 reccomended) "))
		width = int(raw_input("Width? (800 recommended) "))

	pygame.init()
	myWindow = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Ultimate Pong: 2P")

	myCanvas = pygame.Surface(myWindow.get_size())
	myCanvas.fill((0,0,0))

	myClock = pygame.time.Clock()

	myFont = pygame.font.Font(None,48)

	score1display = myFont.render(str(score1),True,(255,255,255))
	score1rect = score1display.get_rect()
	score2display = myFont.render(str(score2),True,(255,255,255))
	score2rect = score2display.get_rect()
	score1rect.centerx = (width / 4)
	score1rect.centery = 24
	score2rect.centerx = ((width / 4) * 3)
	score2rect.centery = 24

	player1y = ((height / 2) - 100)
	player2y = ((height / 2) - 100)

	ballx = (height / 2) - 25
	bally = (height / 2) - 50
	ballxvel = random.choice([ballspeed,-1*ballspeed])
	ballyvel = random.choice([ballspeed,-1*ballspeed])

	myCanvas.fill((0,0,0))
	pygame.draw.rect(myCanvas,(255,255,255),(100,player1y,20,100),0)
	pygame.draw.rect(myCanvas,(255,255,255),((width - 120),player2y,20,100),0)
	pygame.draw.rect(myCanvas,(255,255,255),(ballx,bally,20,20),0)
	myWindow.blit(myCanvas,(0,0))
	myWindow.blit(score1display,score1rect)
	myWindow.blit(score2display,score2rect)
	pygame.display.flip()
	time.sleep(1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "\nFinal Scores\n\tP1:",score1,"\n\tP2:",score2
				if score1 > score2:
					print "P1 wins!"
				if score1 < score2:
					print "P2 wins!"
				if score1 == score2:
					print "Tie"
				exit()
		myClock.tick(50)
	
		# Drawing the field, players, score, and ball
		myCanvas.fill((0,0,0))
		pygame.draw.rect(myCanvas,(255,255,255),(100,player1y,20,100),0)
		pygame.draw.rect(myCanvas,(255,255,255),((width - 120),player2y,20,100),0)
		pygame.draw.rect(myCanvas,(255,255,255),(ballx,bally,20,20),0)
		myWindow.blit(myCanvas,(0,0))
		myWindow.blit(score1display,score1rect)
		myWindow.blit(score2display,score2rect)
		pygame.display.flip()

		# Keeping score
		if ballx <= -20:
			score2 += 1
		if ballx >= (width + 20):
			score1 += 1
		score1display = myFont.render(str(score1),True,(255,255,255))
		score1rect = score1display.get_rect()
		score2display = myFont.render(str(score2),True,(255,255,255))
		score2rect = score2display.get_rect()
		score1rect.centerx = (width / 4)
		score1rect.centery = 24
		score2rect.centerx = ((width / 4) * 3)
		score2rect.centery = 24
	
		# Reset if ball leaves field
		if ballx <= -20 or ballx >= (width + 20):
			time.sleep(1)
			player1y = ((height / 2) - 100)
			player2y = ((height / 2) - 100)
			ballx = (height / 2) - 25
			bally = (height / 2) - 50
			ballxvel = random.choice([ballspeed,-1*ballspeed])
			ballyvel = random.choice([ballspeed,-1*ballspeed])
	
		keys = pygame.key.get_pressed()

		# Player 1 (left)
		if keys[pygame.locals.K_a] == True and player1y >= 0:
			player1y -= 10
		if keys[pygame.locals.K_z] == True and player1y <= (height - 100):
			player1y += 10

		# Player 2 (right)
		if keys[pygame.locals.K_UP] == True and player2y >= 0:
			player2y -= 10
		if keys[pygame.locals.K_DOWN] == True and player2y <= (height - 100):
			player2y += 10

		# Moving The Ball
		if bally <= 0 or bally >= (height - 20):
			if ballx > 100 and ballx < (height - 120):
				ballyvel = ballyvel * -1
		if ballx >= 100 and ballx <= 120 and bally >= player1y and bally <= (player1y + 80):
			ballxvel = ballxvel * -1
			ballx = 120
		if (ballx + 20) >= (width - 120) and (ballx + 20) <= (width - 100) and bally >= player2y and bally <= (player2y + 80):
			ballx = width - 140
			ballxvel = ballxvel * -1
	
		if debug == False:
			ballx += ballxvel
			bally += ballyvel
		elif keys[pygame.locals.K_y] == True:
			ballx += ballxvel
			bally += ballyvel
##############################################################################################

#3 Player Game
##############################################################################################
if players == 3:
	handicap1 = 0
	handicap2 = 0
	handicap3 = 0
	handicap = raw_input('Activate handicaps? (Type "yes" or "no") ')
	if handicap == "yes":
		handicap1 = int(raw_input("\tP1 handicap? "))
		handicap2 = int(raw_input("\tP2 handicap? "))
		handicap3 = int(raw_input("\tP3 handicap? "))
	ballspeed = int(raw_input("Ball speed? (5 recommended) "))
	if ballspeed == -100:
		ballspeed = 5
		print "\nDebug Mode Activated\nBall only moves if \"T\" is pushed\n"
		debug = True

	speedlist = [ballspeed,(-1*ballspeed),(ballspeed/2),(-1*(ballspeed/2))]

	score1 = 0
	score2 = 0
	score3 = 0

	height = int(raw_input("Height? (600 reccomended) "))
	width = int(raw_input("Width? (800 recommended) "))

	pygame.init()
	myWindow = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Ultimate Pong: 3P")

	myCanvas = pygame.Surface(myWindow.get_size())
	myCanvas.fill((0,0,0))

	myClock = pygame.time.Clock()

	myFont = pygame.font.Font(None,48)

	score1display = myFont.render(str(score1),True,red)
	score1rect = score1display.get_rect()
	score2display = myFont.render(str(score2),True,blue)
	score2rect = score2display.get_rect()
	score1rect.centerx = 24
	score1rect.centery = 24
	score2rect.centerx = width - 24
	score2rect.centery = 24
	score3display = myFont.render(str(score3),True,yellow)
	score3rect = score3display.get_rect()
	score3rect.centerx = 24
	score3rect.centery = height - 24

	player1y = ((height / 2) - 100)
	player2y = ((height / 2) - 100)
	player3x = ((width / 2) - 50)

	ballx = random.randint(300,(width-300))
	bally = random.randint(300,(height-300))
	ballxvel = random.choice(speedlist)
	ballxvar = ballxvel
	ballyvel = random.choice(speedlist)
	ballyvar = ballyvel

	myCanvas.fill((0,0,0))
	pygame.draw.rect(myCanvas,red,(0,player1y,20,(100 + handicap1)),0)
	pygame.draw.rect(myCanvas,blue,((width - 20),player2y,20,(100 + handicap2)),0)
	pygame.draw.rect(myCanvas,yellow,(player3x,0,(100 + handicap3),20),0)
	pygame.draw.rect(myCanvas,white,(ballx,bally,20,20),0)
	myWindow.blit(myCanvas,(0,0))
	myWindow.blit(score1display,score1rect)
	myWindow.blit(score2display,score2rect)
	myWindow.blit(score3display,score3rect)
	pygame.display.flip()
	time.sleep(1)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "\nFinal Scores\n\tP1:",score1,"\n\tP2:",score2,"\n\tP3:",score3
				if score1 > score2 and score1 > score3:
					print "P1 wins!"
				if score2 > score3 and score2 > score1:
					print "P2 wins!"
				if score2 < score3 and score3 > score1:
					print "P3 wins!"
				print
				exit()
		myClock.tick(50)
	
		# Drawing the field, players, score, and ball
		myCanvas.fill((0,0,0))
		pygame.draw.rect(myCanvas,red,(0,player1y,20,(100 + handicap1)),0)
		pygame.draw.rect(myCanvas,blue,((width - 20),player2y,20,(100 + handicap2)),0)
		pygame.draw.rect(myCanvas,yellow,(player3x,0,(100 + handicap3),20),0)
		pygame.draw.rect(myCanvas,white,(ballx,bally,20,20),0)
		myWindow.blit(myCanvas,(0,0))
		myWindow.blit(score1display,score1rect)
		myWindow.blit(score2display,score2rect)
		myWindow.blit(score3display,score3rect)
		pygame.display.flip()
	
		# Keeping score
		if ballx <= 0:
			score2 += 1
			score3 += 1
		if ballx >= (width - 20):
			score1 += 1
			score3 += 1
		if bally <= 0:
			score1 += 1
			score2 += 1
		score1display = myFont.render(str(score1),True,red)
		score1rect = score1display.get_rect()
		score2display = myFont.render(str(score2),True,blue)
		score2rect = score2display.get_rect()
		score1rect.centerx = 24
		score1rect.centery = 24
		score2rect.centerx = width - 24
		score2rect.centery = 24
		score3display = myFont.render(str(score3),True,yellow)
		score3rect = score3display.get_rect()
		score3rect.centerx = 24
		score3rect.centery = height - 24
	
		# Reset if ball leaves field
		if ballx <= 0 or ballx >= (width -20) or bally <= 0:
			time.sleep(1)
			player1y = ((height / 2) - (100 + handicap1))
			player2y = ((height / 2) - (100 + handicap2))
			player3x = ((width / 2) - (50 + handicap3))
			ballx = random.randint(300,(width-300))
			bally = random.randint(300,(height-300))
			ballxvel = random.choice(speedlist)
			ballyvel = random.choice(speedlist)
			ballxvar = ballxvel
			ballyvar = ballyvel

		keys = pygame.key.get_pressed()

		# Player 1 (red)
		if keys[pygame.locals.K_a] == True and player1y >= 0:
			player1y -= 10
		if keys[pygame.locals.K_z] == True and player1y <= (height - (100 + handicap1)):
			player1y += 10

		# Player 2 (blue)
		if keys[pygame.locals.K_p] == True and player2y >= 0:
			player2y -= 10
		if keys[pygame.locals.K_l] == True and player2y <= (height - (100 + handicap2)):
			player2y += 10

		# Player 3 (yellow)
		if keys[pygame.locals.K_q] == True and player3x >= 0:
			player3x -= 10
		if keys[pygame.locals.K_w] == True and player3x <= (width - (100 + handicap3)):
			player3x += 10

		# Moving The Ball
		if ballx <= 20 and bally >= player1y and bally <= (player1y + (80 + handicap1)):
			ballx = 20
			ballxvar = ballxvar * -1.1
			ballyvar = ballyvar * 1.1
		if ballx >= (width - 40) and bally >= player2y and bally <= (player2y + (80 + handicap2)):
			ballx = width - 40
			ballxvar = ballxvar * -1.1
			ballyvar = ballyvar * 1.1
		if bally <= 20 and ballx >= player3x and ballx <= (player3x + (80 + handicap3)):
			bally = 20
			ballyvar = ballyvar * -1.1
			ballxvar = ballxvar * 1.1
		if (bally + 20) >= height:
			ballyvar = ballyvar * -1
		if debug == False:
			ballx += ballxvar
			bally += ballyvar
		elif keys[pygame.locals.K_t] == True:
			ballx += ballxvar
			bally += ballyvar
##############################################################################################

#4 Player Game
##############################################################################################
if players == 4:
	handicap1 = 0
	handicap2 = 0
	handicap3 = 0
	handicap4 = 0
	handicap = raw_input('Activate handicaps? (Type "yes" or "no") ')
	if handicap == "yes":
		handicap1 = int(raw_input("\tP1 handicap? "))
		handicap2 = int(raw_input("\tP2 handicap? "))
		handicap3 = int(raw_input("\tP3 handicap? "))
		handicap4 = int(raw_input("\tP4 handicap? "))
	ballspeed = int(raw_input("Ball speed? (5 recommended) "))
	if ballspeed == -100:
		ballspeed = 5
		print "\nDebug Mode Activated\nBall only moves if \"T\" is pushed\n"
		debug = True

	speedlist = [ballspeed,(-1*ballspeed),(ballspeed/2),(-1*(ballspeed/2))]#,(ballspeed/3),(-1*(ballspeed/3))]

	score1 = 0
	score2 = 0
	score3 = 0
	score4 = 0

	height = int(raw_input("Height? (600 reccomended) "))
	width = int(raw_input("Width? (800 recommended) "))

	pygame.init()
	myWindow = pygame.display.set_mode((width,height))
	pygame.display.set_caption("Ultimate Pong: 4P")

	myCanvas = pygame.Surface(myWindow.get_size())
	myCanvas.fill((0,0,0))

	myClock = pygame.time.Clock()

	myFont = pygame.font.Font(None,48)

	score1display = myFont.render(str(score1),True,red)
	score1rect = score1display.get_rect()
	score2display = myFont.render(str(score2),True,blue)
	score2rect = score2display.get_rect()
	score1rect.centerx = 24
	score1rect.centery = 24
	score2rect.centerx = width - 24
	score2rect.centery = 24
	score3display = myFont.render(str(score3),True,yellow)
	score3rect = score3display.get_rect()
	score4display = myFont.render(str(score4),True,green)
	score4rect = score4display.get_rect()
	score3rect.centerx = 24
	score3rect.centery = height - 24
	score4rect.centerx = width - 24
	score4rect.centery = height - 24

	player1y = ((height / 2) - 100)
	player2y = ((height / 2) - 100)
	player3x = ((width / 2) - 50)
	player4x = ((width / 2) - 50)

	ballx = random.randint(300,(width-300))
	bally = random.randint(300,(height-300))
	ballxvel = random.choice(speedlist)
	ballxvar = ballxvel
	ballyvel = random.choice(speedlist)
	ballyvar = ballxvel

	myCanvas.fill((0,0,0))
	pygame.draw.rect(myCanvas,red,(0,player1y,20,(100 + handicap1)),0)
	pygame.draw.rect(myCanvas,blue,((width - 20),player2y,20,(100 + handicap2)),0)
	pygame.draw.rect(myCanvas,yellow,(player3x,0,(100 + handicap3),20),0)
	pygame.draw.rect(myCanvas,green,(player4x,(height - 20),(100 + handicap4),20),0)
	pygame.draw.rect(myCanvas,white,(ballx,bally,20,20),0)
	myWindow.blit(myCanvas,(0,0))
	myWindow.blit(score1display,score1rect)
	myWindow.blit(score2display,score2rect)
	myWindow.blit(score3display,score3rect)
	myWindow.blit(score4display,score4rect)
	pygame.display.flip()
	time.sleep(1)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print "\nFinal Scores\n\tP1:",score1,"\n\tP2:",score2,"\n\tP3:",score3,"\n\tP4:",score4
				if score1 > score2 and score1 > score3 and score1 > score4:
					print "P1 wins!"
				if score2 > score3 and score2 > score1 and score2 > score4:
					print "P2 wins!"
				if score2 < score3 and score3 > score1 and score3 > score4:
					print "P3 wins!"
				if score4 > score3 and score4 > score1 and score2 < score4:
					print "P4 wins!"
				print
				exit()
		myClock.tick(50)
	
		# Drawing the field, players, score, and ball
		myCanvas.fill((0,0,0))
		pygame.draw.rect(myCanvas,red,(0,player1y,20,(100 + handicap1)),0)
		pygame.draw.rect(myCanvas,blue,((width - 20),player2y,20,(100 + handicap2)),0)
		pygame.draw.rect(myCanvas,yellow,(player3x,0,(100 + handicap3),20),0)
		pygame.draw.rect(myCanvas,green,(player4x,(height - 20),(100 + handicap4),20),0)
		pygame.draw.rect(myCanvas,white,(ballx,bally,20,20),0)
		myWindow.blit(myCanvas,(0,0))
		myWindow.blit(score1display,score1rect)
		myWindow.blit(score2display,score2rect)
		myWindow.blit(score3display,score3rect)
		myWindow.blit(score4display,score4rect)
		pygame.display.flip()
	
		# Keeping score
		if ballx <= 0:
			score2 += 1
			score4 += 1
			score3 += 1
		if ballx >= (width - 20):
			score1 += 1
			score3 += 1
			score4 += 1
		if bally <= 0:
			score4 += 1
			score1 += 1
			score2 += 1
		if bally >= (height - 20):
			score1 += 1
			score2 += 1
			score3 += 1
		score1display = myFont.render(str(score1),True,red)
		score1rect = score1display.get_rect()
		score2display = myFont.render(str(score2),True,blue)
		score2rect = score2display.get_rect()
		score1rect.centerx = 24
		score1rect.centery = 24
		score2rect.centerx = width - 24
		score2rect.centery = 24
		score3display = myFont.render(str(score3),True,yellow)
		score3rect = score3display.get_rect()
		score4display = myFont.render(str(score4),True,green)
		score4rect = score4display.get_rect()
		score3rect.centerx = 24
		score3rect.centery = height - 24
		score4rect.centerx = width - 24
		score4rect.centery = height - 24
	
		# Reset if ball leaves field
		if ballx <= 0 or ballx >= (width -20) or bally <= 0 or bally >= (height - 20):
			time.sleep(1)
			player1y = ((height / 2) - (100 + handicap1))
			player2y = ((height / 2) - (100 + handicap2))
			player3x = ((width / 2) - (50 + handicap3))
			player4x = ((width / 2) - (50 + handicap4))
			ballx = random.randint(300,(width-300))
			bally = random.randint(300,(height-300))
			ballxvel = random.choice(speedlist)
			ballyvel = random.choice(speedlist)
			ballxvar = ballxvel
			ballyvar = ballyvel

		keys = pygame.key.get_pressed()

		# Player 1 (red)
		if keys[pygame.locals.K_a] == True and player1y >= 0:
			player1y -= 10
		if keys[pygame.locals.K_z] == True and player1y <= (height - (100 + handicap1)):
			player1y += 10

		# Player 2 (blue)
		if keys[pygame.locals.K_p] == True and player2y >= 0:
			player2y -= 10
		if keys[pygame.locals.K_l] == True and player2y <= (height - (100 + handicap2)):
			player2y += 10

		# Player 3 (yellow)
		if keys[pygame.locals.K_q] == True and player3x >= 0:
			player3x -= 10
		if keys[pygame.locals.K_w] == True and player3x <= (width - (100 + handicap3)):
			player3x += 10

		# Player 4 (green)
		if keys[pygame.locals.K_n] == True and player4x >= 0:
			player4x -= 10
		if keys[pygame.locals.K_m] == True and player4x <= (width - (100 + handicap4)):
			player4x += 10

		# Moving The Ball
		if ballx <= 20 and bally >= player1y and bally <= (player1y + (80 + handicap1)):
			ballx = 20
			ballxvar = ballxvar * -1.1
			ballyvar = ballyvel * 1.1
		if ballx >= (width - 40) and bally >= player2y and bally <= (player2y + (80 + handicap2)):
			ballx = width - 40
			ballxvar = ballxvar * -1.1
			ballyvar = ballyvar * 1.1
		if bally <= 20 and ballx >= player3x and ballx <= (player3x + (80 + handicap3)):
			bally = 20
			ballyvar = ballyvar * -1.1
			ballxvar = ballxvar * 1.1
		if bally >= (height - 40) and ballx >= player4x and ballx <= (player4x + (handicap4 + 80)):
			bally = height - 40
			ballyvar = ballyvar * -1.1
			ballxvar = ballxvar * 1.1
		if debug == False:
			ballx += ballxvar
			bally += ballyvar
		elif keys[pygame.locals.K_t] == True:
			ballx += ballxvar
			bally += ballyvar
##############################################################################################
