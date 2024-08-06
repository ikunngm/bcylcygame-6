import pygame
pygame.init()

#创建一个屏幕并设置屏幕大小
screen = pygame.display.set_mode((1000,500))

#设置屏幕标题
pygame.display.set_caption("bcylcygame")

#加载背景
background = pygame.image.load("图片/ground.png").convert()

#加载石头
stone_left = pygame.image.load("图片/stone/stone-left.png").convert()

stone_right = pygame.image.load("图片/stone/stone-right.png").convert()

#字体
font_30_size = pygame.font.Font("字体/HarmonyOS_Sans_SC_Light.ttf",30)

#不允许背景向右方移动
background_move_right = False

#不允许背景向左方移动
background_move_left = False

#不允许背景向下方移动
background_move_down = False

#背景初始位置
background_x = 0

background_y = 200

#勇者是否在地面
on_ground = True

#魔王移动的距离
enemy_move_x = 0

#魔王血量
enemy_hp = 2500

#勇者血量
soldier_hp = 250

#设置已关闭
set_enter = False

#设置界面特效X轴上移动的距离
move_set_x = 0

#设置界面特效y轴上移动的距离
move_set_y = 0

#游戏未结束
game_over = False

#文本
text_set = font_30_size.render(("设置"),True,(0,0,0))

text_back = font_30_size.render(("返回"),True,(0,0,0))

text_none_winner = font_30_size.render(("你与魔王同归于尽了"),True,(0,0,0))

text_win = font_30_size.render(("你赢了"),True,(255,255,0))

text_die = font_30_size.render(("你死了"),True,(255,0,0))