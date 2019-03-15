from pygame import Rect, quit

#from data import level

class Astronaut:

    def __init__(self, pos, direction):
        self.pos = pos
        self.w = 29
        self.h = 62
        self.direction = direction
        self.ammo = 15
        self.sprite_count = 0
        self.vel_x = 3
        self.vel_y = 0
        self.count_time_in_air = 0
        self.is_jumping = False
        self.is_shooting = False
        self.crawl_move = False  
        self.acc = 0   
        self.status = "alive"  

    def set_direction(self, direction): 

        self.previous_dir = self.direction
        self.direction = direction
        
    def sprite_count_inc(self):
        
        self.sprite_count += 1    

        if self.sprite_count > 5:
            self.sprite_count = 0
            if self.direction is "shot_right":
                self.direction = "idle_right"
            elif self.direction is "shot_left":
               self.direction = "idle_left"          
               self.is_shooting = False
    
    def die(self, plr_graphics):

        if self.direction is "idle_right" or self.direction is "crawl_right" or self.direction is "jump_right" or self.direction is "move_right":
            self.set_direction("death_right")
        else: 
            self.set_direction("death_left")
            self.status = "dead"
            self.sprite_count = 0

    def set_size(self):
        temp_x = self.pos.left
        temp_y = self.pos.top   
        if self.direction is "crawl_left" or "crawl_right":
            temp_w = 62
            temp_h = 47

        elif self.direction is "move_right" or self.direction is "move_left" or self.direction is "jump_left" or self.direction is "jump_right":
            temp_w = 40
            temp_h = 60
        else: 
            temp_w = 30
            temp_h = 40

        self.pos = Rect(temp_x, temp_y, temp_w, temp_h)

    def draw(self, screen, plr_graphics):
        temp_dir = self.direction
        if self.acc > 40 and not self.status is "dead":
            if self.direction is "move_left":
                temp_dir = "run_left"
            elif self.direction is "move_right":
                temp_dir = "run_right"
            self.vel_x = 4
        if self.acc <= 40 and self.direction is "move_left" or self.direction is "move_left" and not self.status is "dead":
            self.vel_x = 3
         
        screen.blit(plr_graphics[temp_dir][self.sprite_count], (320, self.pos.y))
        self.sprite_count_inc()

    def collision_test2(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                return True
        return False

    def collision_test(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def shot(self, direction):     
        if not self.status is "dead": 
            self.is_shooting = True        
            self.acc = 0
            self.sprite_count = 0
            self.ammo -= 1
            if direction is "left":
                self.direction = "shot_left"
            if direction is "right":
                self.direction = "shot_right"

    def jump(self):
        if not self.is_jumping:
            if self.count_time_in_air < 6:
                self.vel_y = -7

            self.acc = 0
            self.acc_counter = 0       
            self.is_jumping = True

            if self.direction is "move_right" or self.direction is "idle_right":
                self.set_direction("jump_right")
            elif self.direction is "move_left" or self.direction is "idle_left":
                self.set_direction("jump_left")

    def move(self, moves, pos, is_jumping, tiles, plr_graphics, level): 
   
         if self.direction is "idle_left" or self.direction is "idle_right":
              self.acc = 0
          
         if moves["right"] is True:
             self.set_direction("move_right")
             self.pos.left += self.vel_x
             self.acc += 1
         elif moves["left"] is True:
             self.set_direction("move_left")
             self.pos.left -= self.vel_x
             self.acc += 1

         hit_list = self.collision_test(self.pos, tiles)

         for tile in hit_list:
             if moves["right"] is True:
                 self.pos.right = tile.left 
             elif moves["left"] is True:
                 self.pos.left = tile.right 

         self.pos.y += self.vel_y  
         self.vel_y += 0.2

         if self.pos.y > 480:
             level.status = "game_over"

         if self.vel_y > 3:
              self.vel_y = 3  
         
         hit_list = self.collision_test(self.pos, tiles)
         #print(hit_list)

         for tile in hit_list:
             if self.vel_y > 0:                                 
                 self.pos.y -= self.vel_y
                 self.pos.bottom = tile.top 
                 self.vel_y = 0
                 self.count_time_in_air = 0
                 self.is_jumping = False
                 if self.direction is "jump_right":
                      self.set_direction("idle_right")
                 elif self.direction is "jump_left":
                      self.set_direction("idle_left")
             if self.vel_y < 0:
                 self.pos.top = tile.bottom
                 self.vel_y += 1
        
