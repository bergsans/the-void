from pygame import Rect, font

#from graphics_sources import bg
from math import floor


from levels import levels

class Level:
    def __init__(self, identifier):
        self.identifier = identifier
        self.map = levels[self.identifier]
        self.is_inited = False
        self.score = 0
        self.status = "play"

    def init_map(self):
        y = 0
        temp = []
        for layer in self.map:
            x = 0
            for tile in layer:
                if tile != "0":
                    temp.append(Rect(x * 50, y * 50, 50, 50))
                x += 1
            y += 1
        return temp
      
    def draw(self, pos_tiles, screen, plr_pos_x, plr_pos_y, stance, speed, tilesSrc, bg, time):
        screen.blit(bg, (0, 0))
        y = 0 
  
        for layer in self.map:       
            x = 0      
            for tile in layer:
                temp_x = ((x * 50) + 320) - plr_pos_x
                if tile != "0":
                    #self..append(Rect(x * 50, y * 50, 50, 50))
                    screen.blit(tilesSrc[tile],(temp_x, y * 50))
                x += 1
            y += 1
        self.is_inited = True
            
        display_time = "TIME: {0:d}".format(time)
        display_score = "SCORE: {0:d}".format(self.score)  
        this_font = font.SysFont('comicsans', 30, True)
        time = this_font.render(display_time, 1, (0,230,0))
        score = this_font.render(display_score, 1, (0,230,0))
        
        
        screen.blit(time, (300, 10))
        screen.blit(score, (450, 10))

        if self.status is "game_over":

            GAME_OVER_FONT = font.SysFont('comicsans', 90, True)
            game_over_text = "GAME OVER"
            game_over = GAME_OVER_FONT.render(game_over_text, 1, (0,230,0))
            screen.blit(game_over, (100, 200))

        if self.status is "level_success":
            LEVEL_SUCCESS_FONT = font.SysFont('comicsans', 90, True)
            SUCCESS_text = "SUCCESS"
            success = LEVEL_SUCCESS_FONT.render(SUCCESS_text, 1, (0,230,0))
            screen.blit(success, (100, 200))

            success_score_font = font.SysFont('comicsans', 50, True)
            success_score_font.render(display_score, 1, (0,230,0))
            screen.blit(score, (100, 350))
            








