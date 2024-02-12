#Password Generator Project
from random import *
from math import floor,ceil

dic = {'ido':20,'yoav': 30, 'roi':10, 'ofer':55, 'hilla':25 }
list1 = [1, 2, 3, 4, 5]







player_position = -6
enemy_position = 8



# player_position = round(player_position)
# enemy_position = round(enemy_position)
if enemy_position <= player_position <= enemy_position + 20 or enemy_position -20 <= player_position <= enemy_position:
    print('collision')

print(player_position)
print(enemy_position)
#
# if player_position // 10:
#     print('collision')
# else:
#     print("didn't collide")
