#from graphics_sources import explosionsSrc

class Explosion:
    def __init__(self, status, x, y, abs_x, abs_y):
        self.status = status
        self.x = x
        self.y = y
        self.abs_x = abs_x
        self.abs_y = abs_y
        self.sprite_count = 0
        self.max_sprites = 90
    
    def sprite_count_inc(self):
        self.sprite_count += 1
        if self.sprite_count >= self.max_sprites:
            self.status = "not_active"   

    def draw(self, plr_direction, plr_vel_x, screen, explosionsSrc):
        if plr_direction is "move_left" or plr_direction is "run_left" or plr_direction is "jump_left" or plr_direction is "crawl_left" and plr_vel_x > 0:   
            self.x += plr_vel_x
        elif plr_direction is "move_right" or plr_direction is "run_right" or plr_direction is "jump_right" or plr_direction is "crawl_left" and plr_vel_x > 0:
            self.x -= plr_vel_x

        screen.blit(explosionsSrc[self.sprite_count], (self.x, self.y))
        self.sprite_count_inc()
