from pygame import Rect

class Item:
    def __init__(self, typeOf, pos):
        self.typeOf = typeOf
        self.pos = pos
        self.status = "active"

    def change_status(self, new_status):
        self.status = new_status

    def collision_test(self, items):
        hit_list = []
        
        if self.pos.colliderect(items):
            return True
        return False
  
    def draw(self, pic, screen, plr_x):
        if self.pos.x <= plr_x:
            temp_x = 320 - abs(plr_x - self.pos.x)
        elif self.pos.x > plr_x:
            temp_x = 320 + abs(plr_x - self.pos.x)  
        temp_y = self.pos.y

        screen.blit(pic[self.typeOf], (temp_x, temp_y))


