import os
from pygame import Rect
from helpers import create_fi_pattern
from class_item import Item
from class_enemy import Enemy
from class_astronaut import Astronaut 
from class_level import Level
from class_projectiles import Projectile
from class_explosion import Explosion

foes = []
foes.append(Enemy("e0", 4, Rect(550, 140, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(1050, 290, 60, 60), create_fi_pattern(["left", "left", "left", "left","right", "right","right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(2400, 290, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))
foes.append(Enemy("e0", 5, Rect(2500, 290, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))
foes.append(Enemy("e2", 4, Rect(2800, 232, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))
foes.append(Enemy("e2", 4, Rect(3000, 382, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e2", 4, Rect(3250, 332, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))
foes.append(Enemy("e2", 4, Rect(4000, 282, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(4600, 240, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e2", 4, Rect(5000, 234, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e2", 4, Rect(5300, 136, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e2", 4, Rect(5700, 330, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e2", 4, Rect(5900, 332, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(6300, 290, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(6800, 342, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(7050, 290, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))
foes.append(Enemy("e2", 4, Rect(7200, 284, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e2", 4, Rect(7500, 332, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 1))
foes.append(Enemy("e0", 5, Rect(8200, 392, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))
foes.append(Enemy("e0", 5, Rect(8900, 392, 60, 60), create_fi_pattern(["left", "left", "left", "right", "right", "right"], 2), 1, 2))

items = []
items.append(Item("exit_door",Rect(9100,322,128,128)))
items.append(Item("gem",Rect(410,160,22,25)))
items.append(Item("gem",Rect(440,160,22,25)))
items.append(Item("gem",Rect(410,260,22,25)))
items.append(Item("gem",Rect(800,300,22,25)))
items.append(Item("gem",Rect(830,300,22,25)))
items.append(Item("gem",Rect(910,160,22,25)))
items.append(Item("gem",Rect(1150,310,22,25)))
items.append(Item("gem",Rect(1200,310,22,25)))
items.append(Item("gem",Rect(1500,260,22,25)))
items.append(Item("gem",Rect(1700,200,22,25)))
items.append(Item("gem",Rect(1730,200,22,25)))
items.append(Item("gem",Rect(2410,230,22,25)))
items.append(Item("gem",Rect(2500,200,22,25)))
items.append(Item("gem",Rect(2550,260,22,25)))
items.append(Item("gem",Rect(3000,260,22,25)))
items.append(Item("gem",Rect(3030,260,22,25)))
items.append(Item("gem",Rect(4000,300,22,25)))
items.append(Item("gem",Rect(4030,300,22,25)))
items.append(Item("gem",Rect(4050,300,22,25)))
items.append(Item("gem",Rect(4500,250,22,25)))
items.append(Item("gem",Rect(4600,260,22,25)))
items.append(Item("gem",Rect(5000,260,22,25)))
items.append(Item("gem",Rect(5300,160,22,25)))
items.append(Item("gem",Rect(5330,160,22,25)))
items.append(Item("gem",Rect(5600,260,22,25)))
items.append(Item("gem",Rect(5900,260,22,25)))
items.append(Item("gem",Rect(5950,200,22,25)))
items.append(Item("gem",Rect(5700,250,22,25)))
items.append(Item("gem",Rect(6500,50,22,25)))
items.append(Item("gem",Rect(6600,50,22,25)))
items.append(Item("gem",Rect(6500,350,22,25)))
items.append(Item("gem",Rect(6600,350,22,25)))
items.append(Item("gem",Rect(7050,260,22,25)))
items.append(Item("gem",Rect(7030,260,22,25)))
items.append(Item("gem",Rect(7000,260,22,25)))
items.append(Item("gem",Rect(7720,100,22,25)))
items.append(Item("gem",Rect(7850,200,22,25)))
items.append(Item("gem",Rect(8450,160,22,25)))
items.append(Item("gem",Rect(8420,160,22,25)))
items.append(Item("gem",Rect(8400,100,22,25)))
items.append(Item("gem",Rect(8670,60,22,25)))
items.append(Item("gem",Rect(8700,60,22,25)))
items.append(Item("gem",Rect(8730,60,22,25)))

level = Level("l_1")
plr = Astronaut(Rect(800, 0, 40, 60), "idle_right")
shots = []
explodingProjectiles = []
pos_tiles = level.init_map()
