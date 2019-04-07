from pygame import Rect, mixer
import os





def create_fi_pattern(moves, speed):
    tempAddMoves = [];
    for move in moves:
        for n in range(0,int(50 / speed)):
            tempAddMoves.append((move));
    return tempAddMoves;


def render_items(itemsSrc, screen, items, plr_x):
    for item in items:
        if item.status is "active":
            item.draw(itemsSrc, screen, plr_x)

def render_foes(plr_x, foes, screen, enemySrc):
    for foe in foes:
        foe.draw(plr_x, screen, enemySrc)
        foe.move(enemySrc)

def render_ui_missile(ammo, screen, ui_elems):
    for missile_index in range(ammo):
        screen.blit(ui_elems["missile"], (((6 * missile_index) + 5), 15))

def move_projectiles(shots, pos_tiles, enemies, plr, screen, projectiles, explodingProjectiles, Explosion):

    for shot in shots:
        if not shot.status is "not-active":
            if shot.direction is "right":
                shot.draw(plr.pos.x, plr.pos.y, screen, projectiles)
                shot.x += 15 - plr.vel_x
                shot.abs_x += 15
                shot.dist -= 15
            elif shot.direction is "left":
                shot.draw(plr.pos.x, plr.pos.y, screen, projectiles)
                shot.x -= 15 + plr.vel_x
                shot.abs_x -= 15
                shot.dist -= 15
            
            for enemy in enemies:
                if enemy.status is "active":
                    test_foe = shot.collision_test2(Rect(shot.abs_x, shot.abs_y, 25, 15), enemy.pos)
                    if test_foe is True:
                        shot.status = "not-active"
                        explosion_sound = mixer.Sound("sounds/explosion.wav");
                        explosion_sound.play()
                        if shot.direction is "right":
                            explodingProjectiles.append(Explosion("explode", (shot.x - 40), (shot.y - 70), (shot.abs_x - 40), (shot.abs_y - 70)))
                        else:
                            explodingProjectiles.append(Explosion("explode", (shot.x - 100), (shot.y - 70), (shot.abs_x - 100), (shot.abs_y - 70)))    
                        enemy.status = "inactive"    

            test_tiles = shot.collision_test(Rect(shot.abs_x, shot.abs_y, 25, 15), pos_tiles)         

            if shot.dist <= 0 or test_tiles is True:
                explosion_sound = mixer.Sound("sounds/explosion.wav");
                explosion_sound.play()
                shot.status = "not-active"
           
                if shot.direction is "right":
                    explodingProjectiles.append(Explosion("explode", (shot.x - 70), (shot.y - 70), (shot.abs_x - 70), (shot.abs_y - 70)))
                else:
                    explodingProjectiles.append(Explosion("explode", (shot.x - 70), (shot.y - 70), (shot.abs_x - 70), (shot.abs_y - 70)))        

def render_explosions(explosions, screen, explosionsSrc, plr):
    for explosion in explosions:
        if explosion.status is "explode":
            explosion.draw(plr.direction, plr.vel_x, screen, explosionsSrc)

def check_death_by_foe(enemies, plr_graphics, plr_pos, level, plr):
    for enemy in enemies:
        if enemy.status is "active":
            test_foe = enemy.collision_test(Rect(enemy.pos.x + 15, enemy.pos.y, 40, 55), plr_pos)
            if test_foe is True:
                plr.status = "dead"
                level.status = "game_over"

def check_items(stuffs, itemsSrc, plr_pos, level):

    for item in stuffs:
        if item.status is "active":
            test_item = item.collision_test(plr_pos)
            if test_item is True:
                if item.typeOf is "exit_door":
                    if not level.status is "level_success":
                        level.score += 1000

                    level.status = "level_success"
                    
                else:
                    item.status = "inactive"
                    level.score += 10

