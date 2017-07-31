import pygame
import sys
from setting import *
from SpriteBackGround import BackGroundimage
from ship import Ship
import gamefunctions as gf
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien

def run_game():
	pygame.init()
	gamesetting = Settings()
	
	screen = pygame.display.set_mode((gamesetting.screen_width,gamesetting.screen_height))
	pygame.display.set_caption("Alien Invasion")


	ship = Ship(gamesetting,screen)
	bullets = Group()
	alien = Group()
	
	gf.create_fleet(gamesetting,screen,ship,alien)

	while True:
		gf.check_events(gamesetting,ship,screen,bullets)
		ship.update()
		gf.update_bullets(alien,bullets,gamesetting,screen,ship)
		gf.update_aliens(gamesetting,alien)
		gf.update_screen(gamesetting,screen,ship,alien,bullets)
		
run_game()