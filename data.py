import os
from levels import levels
from pygame import Rect
from helpers import create_fi_pattern
from class_item import Item
from class_enemy import Enemy
from class_astronaut import Astronaut 
from class_level import Level
from class_projectiles import Projectile
from class_explosion import Explosion


foes = []

for enemy in levels['enemies']:
    foes.append(Enemy(typeOf = enemy['id'], numberOfSprites = 4, pos = Rect(enemy['x'], enemy['y'], enemy['w'], enemy['h']), pattern = "left", hp = 1, speed = 1))

items = []

for item in levels['items']:   
    items.append(Item(item['id'],Rect(item['x'],item['y'],item['w'],item['h'])))

level = Level("l_1")
plr = Astronaut(Rect(800, 0, 40, 60), "idle_right")
shots = []
explodingProjectiles = []
pos_tiles = level.init_map()
