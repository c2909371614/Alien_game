
import pygame
class Settings():
	"""储存《外星人入侵》的所有设置的类""" 
	def __init__(self):
		"""初始化游戏设置"""
		#屏幕设置 
		self.screen_width = 840
		self.screen_height = 650 
		self.bg_color = (255, 255, 255) 
		
		#飞船的设置
		self.ship_speed_factor = 0.5
		
		#子弹设置
		self.bullet_speed_factor = 0.35
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 30

		#Alien settings
		self.alien_speed_factor = 0.05
		self.fleet_direction = 1#move right, -1 left
		image = pygame.image.load('images/alien.bmp')
		self.fleet_drop_speed = int(image.get_rect().height / 2)

		
