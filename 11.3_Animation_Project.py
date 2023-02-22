'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
# splatter drip
import arcade
import random
SW = 600
SH = 600

class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,hue):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.hue = hue

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.hue)

    def update_ball(self):
        chance = random.randint(0,2)
        # if self.rad > 0 :
        #     self.rad-=self.dx
        # if self.rad == 0:
        #     del self
        if chance == 0:
            self.hue = (random.randint(200, 230), random.randint(0, 200), random.randint(50, 255))

        if self.rad > 0:
            self.rad-=self.dx
            # self.rad *= -1
        self.dx += 2




class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_list=[]
        for i in range (1):
            rad = random.randint(3, 9)
            x = random.randint(rad,SW-rad)
            y = random.randint(rad,SH-rad)
            dx = random.randint(1,1)
            dy = random.randint(0, 0)
            hue = (random.randint(200, 230),random.randint(0, 200),random.randint(50, 255))
            hue = (arcade.color.RED)
            if dx == 0:
                dx = random.randint(1, 3)
            if dy == 0:
                dy = random.randint(-3, -1)
            self.ball = Ball(x,y,dx,dy,rad,hue)
            self.ball_list.append(self.ball)
    def on_draw(self):
        arcade.start_render()
        for i in (self.ball_list):
            i.draw_ball()

    def on_update(self, dt):
        for i in (self.ball_list):
            i.update_ball()
        rad = random.randint(5, 10)
        x = random.randint(0,600)
        y = random.randint(0,600)
        dx = random.randint(1, 1)
        dy = random.randint(0, 0)
        hue = (random.randint(200, 230), random.randint(0, 200), random.randint(50, 255))
        chance = random.randint(0,0)
        if chance == 0:
            self.ball = Ball(x, y, dx, dy, rad, hue)
            self.ball_list.append(self.ball)




def main():
    window = MyGame(SW,SH,"Twinkle")
    arcade.run()

if __name__ == "__main__":
    main()