#from graphics_sources import projectiles

class Projectile:
    def __init__(self, direction, x, y, abs_x, abs_y):
        self.status = "active"
        self.direction = direction
        self.x = x
        self.y = y
        self.abs_x = abs_x
        self.abs_y = abs_y
        self.dist = 250

    def collision_test(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                return True
        return False

    def collision_test2(self, rect, foe):
        hit_list = []
        
        if rect.colliderect(foe):
            return True
        return False


    def draw(self, plr_absX, plr_absY, screen, projectiles):

        if self.abs_x <= plr_absX:  
            self.x = 320 - abs(plr_absX - self.abs_x)            
        else:
            self.x = 320 + abs(plr_absX - self.abs_x)

        screen.blit(projectiles["rocket"][self.direction], (self.x, self.y))
 



        
