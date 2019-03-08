from pygame import image, display,FULLSCREEN
import os

bg = image.load(os.path.join("graphics","backgrounds", "back2.png"))

enemySrc = [ {
        "left": [
image.load(os.path.join("graphics", "sprites", "enemy_1_left0.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left1.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left2.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left3.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left4.png"))],

        "right": [
image.load(os.path.join("graphics", "sprites", "enemy_1_right0.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right1.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right2.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right3.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right4.png"))]
    },
 {
        "left": [
image.load(os.path.join("graphics", "sprites", "enemy_1_left0.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left1.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left2.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left3.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left4.png"))],

        "right": [
image.load(os.path.join("graphics", "sprites", "enemy_1_right0.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right1.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right2.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right3.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right4.png"))]
    }
]

plr_graphics = {
    "move_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "walk_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_left_005.png"))], 
    "move_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "walk_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "walk_right_005.png"))],    
    "idle_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_left_005.png"))],
    "idle_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Idle_right_005.png"))],
    "run_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "Run_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_right_005.png"))],
    "run_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "Run_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Run_left_005.png"))],
    "jump_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_left_005.png"))],
    "jump_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Jump_right_005.png"))],
    "shot_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_left_005.png"))],
    "shot_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "shot1_right_005.png"))],
    "crawl_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_left_005.png"))],
    "crawl_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Crawl_right_005.png"))],
    "death_left": [image.load(os.path.join("graphics", "sprites", "astronaut", "Death_left_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_left_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_left_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_left_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_left_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_left_005.png"))],
    "death_right": [image.load(os.path.join("graphics", "sprites", "astronaut", "Death_right_000.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_right_001.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_right_002.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_right_003.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_right_004.png")), image.load(os.path.join("graphics", "sprites", "astronaut", "Death_right_005.png"))]
}

projectiles = {
    "rocket": {
        "left": image.load(os.path.join("graphics", "sprites", "astronaut", "left_rocket.png")),
        "right": image.load(os.path.join("graphics", "sprites", "astronaut", "right_rocket.png"))
    }
} 

enemySrc = [ 
    {
        "left": [
image.load(os.path.join("graphics", "sprites", "enemy_1_left0.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left1.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left2.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left3.png")),
image.load(os.path.join("graphics", "sprites", "enemy_1_left4.png"))],

        "right": [
image.load(os.path.join("graphics", "sprites", "enemy_1_right0.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right1.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right2.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right3.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_1_right4.png"))]
    },
    {
  
        "left": [
image.load(os.path.join("graphics", "sprites", "enemy_3_left0.png")),
image.load(os.path.join("graphics", "sprites", "enemy_3_left1.png")),
image.load(os.path.join("graphics", "sprites", "enemy_3_left2.png")),
image.load(os.path.join("graphics", "sprites", "enemy_3_left3.png")),
image.load(os.path.join("graphics", "sprites", "enemy_3_left4.png"))],

        "right": [
image.load(os.path.join("graphics", "sprites", "enemy_3_right0.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_3_right1.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_3_right2.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_3_right3.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_3_right4.png"))]   
    },
    {
  
        "left": [
image.load(os.path.join("graphics", "sprites", "enemy_2_left0.png")),
image.load(os.path.join("graphics", "sprites", "enemy_2_left1.png")),
image.load(os.path.join("graphics", "sprites", "enemy_2_left2.png")),
image.load(os.path.join("graphics", "sprites", "enemy_2_left3.png"))],

        "right": [
image.load(os.path.join("graphics", "sprites", "enemy_2_right0.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_2_right1.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_2_right2.png")), 
image.load(os.path.join("graphics", "sprites", "enemy_2_right3.png"))]   
    }
]

itemsSrc = {
    "gem": image.load(os.path.join("graphics", "items", "diamond.png")),
    "exit_door": image.load(os.path.join("graphics", "items", "door.png"))
}

explosionsSrc = [
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0001.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0002.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0003.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0004.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0005.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0006.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0007.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0008.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0009.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0010.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0011.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0012.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0013.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0014.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0015.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0016.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0017.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0018.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0019.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0020.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0021.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0022.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0023.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0024.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0025.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0026.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0027.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0028.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0029.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0030.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0031.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0032.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0033.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0034.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0035.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0036.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0037.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0038.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0039.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0040.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0041.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0042.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0043.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0044.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0045.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0046.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0047.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0048.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0049.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0050.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0051.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0052.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0053.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0054.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0055.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0056.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0057.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0058.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0059.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0060.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0061.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0062.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0063.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0064.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0065.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0066.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0067.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0068.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0069.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0070.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0071.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0072.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0073.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0074.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0075.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0076.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0077.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0078.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0079.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0080.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0081.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0082.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0083.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0084.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0085.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0086.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0087.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0088.png")),
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0089.png")), 
image.load(os.path.join("graphics", "sprites", "explosions", "explosion1_0090.png"))
]

ui_elems = {
    "bar": image.load(os.path.join("graphics", "ui", "bars.png")),
    "missile": image.load(os.path.join("graphics", "ui", "missile.png"))
}

tilesSrc = {
    "X": image.load(os.path.join("graphics", "tiles", "X.png")),
    "Y": image.load(os.path.join("graphics", "tiles", "X.png")),
    "1": image.load(os.path.join("graphics", "tiles", "1.png")),
    "2": image.load(os.path.join("graphics", "tiles", "2.png")),
    "3": image.load(os.path.join("graphics", "tiles", "3.png")),
    "4": image.load(os.path.join("graphics", "tiles", "4.png")),
    "5": image.load(os.path.join("graphics", "tiles", "5.png")),
    "6": image.load(os.path.join("graphics", "tiles", "6.png")),
    "7": image.load(os.path.join("graphics", "tiles", "7.png"))   

}

bg = image.load(os.path.join("graphics","backgrounds", "back2.png"))

