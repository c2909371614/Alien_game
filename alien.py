
import pygame 
from pygame.sprite import Sprite
from settings import Settings 
import sys

class Alien(Sprite):
	"""表示单个外星人的类"""
	
	def __init__(self, ai_settings, screen):
		"""初始化外星人并设置其起始位置"""
		super(Alien, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		
		#加载外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#每个外星人最初都在屏幕左上角附近
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#存储外星人的准确位置
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		# self.alien_speed_factor = ai_settings.alien_speed_factor
		# self.fleet_drop_speed = ai_settings.fleet_drop_speed
		# self.fleet_direction = ai_settings.fleet_direction
		
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""Move the alien right"""
		self.x += (self.ai_settings.alien_speed_factor * 
			self.ai_settings.fleet_direction)
		# print('direction:',self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		'''return the is_edge of the screen'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			# self.rect.right -= 1
			return True
		elif self.rect.left <= screen_rect.left:
			# self.rect.left += 1
			return True
		elif self.rect.bottom >= screen_rect.bottom:
			return True
		# print('no edge')
		return False

if __name__ == "__main__":
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	alien = Alien(ai_settings, screen)
	# os.system('pause')

