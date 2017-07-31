import pygame

class Settings():
	def __init__(self):

		self.screen_width = 600
		self.screen_height = 800
		self.screen_bg_color = (230,230,230)

		self.ship_speed_factor = 1.0

		self.bullet_speed_factor = 2.0 
		self.bullet_width = 1
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allow = 3

		self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10

		self.fleet_direction = 1

		#self.screen_bg_img = pygame.image.load('images/bg.bmp')

