from pygame import Rect

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
 
    def move(self, graphics):
        
        if self.pattern[self.walkCounter] is "left":
            self.pos.x -= self.speed
        else:
            self.pos.x += self.speed

        self.walkCounter += 1

        if self.walkCounter >= len(self.pattern):
            self.walkCounter = 0
  
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
        if self.typeOf is "e0":
            i = 0
        elif self.typeOf is "e1":
            i = 1
        elif self.typeOf is "e2":
            i = 2

        screen.blit(graphics[i][self.pattern[self.walkCounter]][self.sprite_counter], (temp_x, temp_y))
        self.inc()

