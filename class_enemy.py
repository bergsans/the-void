from pygame import Rect
import copy

class Enemy:
    def __init__(self, typeOf, numberOfSprites, pos, pattern, hp, speed):

        self.typeOf = typeOf
        self.sprite_counter = 0
        self.numberOfSprites = numberOfSprites
        self.pos = pos
        self.pattern = pattern
        self.hp = hp
        self.speed = speed
        self.walkCounter = 0
        self.status = "active"
        self.loadStatus = 0
        self.temp_count = 0

    def inc(self):
        self.temp_count += 1
        if self.temp_count == 2:
            self.sprite_counter += 1
            self.temp_count = 0

        if self.sprite_counter >= self.numberOfSprites:
            self.sprite_counter = 0
 
    def move(self, graphics, tiles):
        
        if self.pattern is "left":
            if not self.collision_test_move(self.pos, tiles, "left") and self.collision_test_move_vert(self.pos, tiles, "left"):
                self.pos.x -= self.speed
            else:
                self.pattern = "right"

        elif self.pattern is "right":
            if not self.collision_test_move(self.pos, tiles, "right") and self.collision_test_move_vert(self.pos, tiles, "right"):
                self.pos.x += self.speed
            else:
                self.pattern = "left" 
  
    def collision_test_move(self, rect, tiles, direction):
        temp_pos = copy.deepcopy(rect)
        if direction is "left":
            temp_pos.x -= (self.speed + 4)

        elif direction is "right":
            temp_pos.x += (self.speed + 4)
        
        hit_list = []
        for tile in tiles:
            if temp_pos.colliderect(tile):
                return True
        return False

    def collision_test_move_vert(self, rect, tiles, direction):
        temp_pos = copy.deepcopy(rect)
      
        if direction is "left":
            temp_pos.x -= (self.speed + 60)

        elif direction is "right":
            temp_pos.x += (self.speed + 60)
  
        temp_pos.y += self.speed + 4
        
        hit_list = []
        for tile in tiles:
            if temp_pos.colliderect(tile):
                return True
        return False

    def collision_test(self, rect, foe):
        hit_list = []
        
        if rect.colliderect(foe):
            return True
        return False

    def draw(self, plr_x, screen, graphics):
        if not self.status is "active":
            return        

        if self.pos.x <= plr_x:
            temp_x = 320 - abs(plr_x - self.pos.x)
        elif self.pos.x > plr_x:
            temp_x = 320 + abs(plr_x - self.pos.x)
        temp_y = self.pos.y
        i = 0
        if self.typeOf == "e0":
            i = 0
        elif self.typeOf == "e1":
            i = 1
        elif self.typeOf == "e2":
            i = 2

        screen.blit(graphics[i][self.pattern][self.sprite_counter], (temp_x, temp_y))
        self.inc()

