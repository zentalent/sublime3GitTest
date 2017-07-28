import pygame

class eventlogs(ship):
	def __init__(self,event,screen,ship):
		self.screen = screen
		self.ship = ship
		self.event = event

	def showlogs(screen):

	def trace_shipmoving_event(event,ship):
		if event.type == event.KEYDOWN and event.key == pygame.K_RIGHT:
			print 'move right'
		elif event.type == event.KEYDOWN and event.key ==pygame.K_LEFT:
			print 'move left'