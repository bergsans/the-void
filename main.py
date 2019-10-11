from pygame import init, display, mouse, FULLSCREEN, time, event, draw, QUIT, quit, K_ESCAPE, K_DOWN, K_LEFT, K_RIGHT, K_s, K_SPACE, K_UP, key, image, font, time, Rect, KEYDOWN, KEYUP, mixer

import os
from math import floor

from class_item import Item
from class_enemy import Enemy
from class_astronaut import Astronaut 
from class_level import Level
from class_projectiles import Projectile
from class_explosion import Explosion
from helpers import create_fi_pattern, check_items, check_death_by_foe, render_explosions, move_projectiles, render_ui_missile, render_foes, render_items
from data import foes, items, level, plr, shots, explodingProjectiles, pos_tiles
from graphics_sources import ui_elems, explosionsSrc, plr_graphics, bg, tilesSrc, projectiles, enemySrc, itemsSrc
init()
clock = time.Clock()
mouse.set_visible(False)
screen = display.set_mode((640, 480))

moves_right = False
moves_left = False
is_jumping = False
is_crawling = False
is_shooting = False
time = 150
temp_time = 0

is_game_ongoing = True

#mixer.music.load(os.path.join("sounds", "background.mp3"))
#mixer.music.play(-1)


while is_game_ongoing is True:

    moves_bools = {
        "right": moves_right,
        "left": moves_left,
        "is_crawling": is_crawling       
    }
    
    level.draw(pos_tiles, screen, plr.pos.x, plr.pos.y, plr.direction, plr.vel_x, tilesSrc, bg, time)
    
    temp_time += 1
    if temp_time > 30:
        temp_time = 0
        time -= 1
    if time <= 0: 
        level.status = "game_over"
        
    render_ui_missile(plr.ammo, screen, ui_elems)
  
    if not plr.status is "dead" or level.status is "level_success":
        plr.move(moves_bools, plr.pos, is_jumping, pos_tiles, plr_graphics, level)  
    
    plr.draw(screen, plr_graphics)
    render_explosions(explodingProjectiles, screen, explosionsSrc, plr)                          
    move_projectiles(shots, pos_tiles, foes, plr, screen, projectiles, explodingProjectiles, Explosion)
    render_items(itemsSrc, screen, items, plr.pos.x)
    check_items(items, itemsSrc, plr.pos, level)
    render_foes(plr.pos.x, foes, screen, enemySrc, pos_tiles)

    check_death_by_foe(foes, plr_graphics, plr.pos, level, plr)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
       
        if ev.type == KEYDOWN:

            if ev.key == K_ESCAPE:
                quit()

            elif not(plr.direction is "shot_left" or plr.direction is "shot_right" or is_jumping) and is_crawling is False:

                if ev.key == K_RIGHT:
                    moves_right = True
                    
                elif ev.key == K_LEFT:
                    moves_left = True

                elif ev.key == K_s:
                    if plr.ammo > 0:
                        is_shooting = True 
                        if plr.direction is "move_right" or plr.direction is "idle_right":
                            plr.shot("right")
                            shots.append(Projectile("right", 360, (plr.pos.y + 30), plr.pos.x, (plr.pos.y + 40)))
                        elif plr.direction is "move_left" or plr.direction is "idle_left":
                            plr.shot("left")
                            shots.append(Projectile("left", 320, (plr.pos.y + 30), plr.pos.x, (plr.pos.y + 40)))

                if ev.key == K_SPACE:
                    plr.jump()

            elif is_crawling is True:

               plr.crawl_move = False    
               if ev.key == K_LEFT:
                   plr.crawl_move = True
               elif ev.key == K_RIGHT:
                   plr.crawl_move = True
                              
        if ev.type == KEYUP:
            plr.acc = 0
         
            if ev.key == K_RIGHT:          
                moves_right = False
                is_crawling = False
                plr.set_direction("idle_right")
            elif ev.key == K_LEFT:
                moves_left = False
                is_crawling = False
                plr.set_direction("idle_left")
         
            elif not plr.direction is "is_jumping":
                is_jumping = False
                plr.crawl_move = False
        if plr.is_shooting is False:
            is_shooting = False

    display.update()
    clock.tick(30)

