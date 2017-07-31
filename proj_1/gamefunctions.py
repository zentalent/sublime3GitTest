import sys
import pygame
from setting import Settings
from bullet import Bullet
from alien import Alien
from random import randint



def check_keydown_event(event,ship,bullets,gamesetting,screen):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = True
		#trace_shipmoving_event(event,ship)
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = True
		#trace_shipmoving_event(event,ship)
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = True
	elif event.key ==pygame.K_j or event.key == pygame.K_SPACE:
		fire_bullet(ship,bullets,gamesetting,screen)

def fire_bullet(ship,bullets,gamesetting,screen):
	if len(bullets) <= gamesetting.bullet_allow:
		new_bullet = Bullet(gamesetting,screen,ship)
		bullets.add(new_bullet)

def check_keyup_event(event,ship):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	elif event.key ==pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = False
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = False

def trace_shipmoving_event(event,gamesetting,ship,screen,bullets):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			print 'move right'
		elif event.type == pygame.KEYDOWN and event.key ==pygame.K_LEFT:
			print 'move left'

def check_events(gamesetting,ship,screen,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT :
			sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ship,bullets,gamesetting,screen)

		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)

def get_number_alien_x(gamesetting,alien_width):
	availuable_space_x = gamesetting.screen_width - 2*alien_width
	print 'there s ',availuable_space_x,' spaces on the screen'
	number_alien_x =int (availuable_space_x / (2 * alien_width) )
	print 'it can be set ' ,number_alien_x,' aliens'
	return number_alien_x



def create_alien(gamesetting,screen,aliens,alien_number,row_number,random_number):
	alien = Alien(screen,gamesetting)
	alien_width = alien.rect.width
	
	alien.x = alien_width + 2 * alien_width * alien_number +random_number
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number +random_number
	alien.rect.x = alien.x
	aliens.add(alien)


def create_fleet(gamesetting,screen,ship,aliens):
	alien = Alien(screen,gamesetting)
	number_alien_x = get_number_alien_x(gamesetting,alien.rect.width)
	number_rows = get_number_rows(gamesetting,ship.rect.height,alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_alien_x):
			random_number = randint(-30,30)
			create_alien(gamesetting,screen,aliens,alien_number,row_number,random_number)
		print 'created ', number_alien_x , ' aliens'

def get_number_rows(gamesetting,ship_height,alien_height):
	availuable_space_y =(gamesetting.screen_height -(3*alien_height) - ship_height)
	number_rows = int(availuable_space_y /(2*alien_height))
	return number_rows


def update_screen(gamesetting,screen,ship,alien,bullets):
	screen.fill(gamesetting.screen_bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.draw(screen)
	pygame.display.flip()

def update_bullets(aliens,bullets,gamesetting,screen,ship):
		bullets.update()
		for bullet in bullets.copy():
			if bullet.rect.bottom < 0:
				bullets.remove(bullet)
		
		collisions =pygame.sprite.groupcollide(bullets,aliens,True,True)

		if len(aliens) == 0 :
			bullets.empty()
			create_fleet(gamesetting,screen,ship,aliens)



def check_fleet_edges(gamesetting,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(gamesetting,aliens)
			break
def change_fleet_direction(gamesetting,aliens):
	for alien in aliens.sprites():
		alien.rect.y += gamesetting.fleet_drop_speed
	gamesetting.fleet_direction *= -1

def update_aliens(gamesetting,aliens):
	check_fleet_edges(gamesetting,aliens)
	aliens.update()
