#设置了中文unicode(UTF-8)

#import sys#game_functions模块中已经导入

import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group

import game_functions as gf#导入game_functons取名为gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	# print(ai_settings.screen_width);
	#(ai_settings.screen_width, ai_settings.screen_height)是元组
	#screen是pygame中的surface对象
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("alien_invasion")
	
	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	# aliens = Alien(ai_settings, screen)wwwwww
	
	#创建一个用于储存子弹的编组
	bullets = Group()
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		#直接更改ship
		gf.check_events(ai_settings, screen, ship, bullets)
		#ship动作更新
		ship.update()
		#更新子弹的位置，并删除已消失的子弹
		gf.update_bullets(bullets, aliens)
		gf.update_aliens(ai_settings, aliens)
		#更新屏幕上的图像，并切换到新屏幕
		gf.update_screen(ai_settings,screen,ship , aliens, bullets)
		# print('running')
run_game()
		





