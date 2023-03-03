'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''

import arcade
import random
SW = 600
SH = 600
hue1 = (random.randint(200, 230), random.randint(0, 200), random.randint(50, 255))
hue2 = (random.randint(0,200),random.randint(40, 230),random.randint(200, 230))
hue3 = (random.randint(200, 255), random.randint(60, 235), random.randint(0, 150))
hue4 = (random.randint(0, 200), random.randint(200, 235), random.randint(50, 235))
# hue1 = arcade.color.RED
# hue2 = arcade.color.BLUE
# hue3 = arcade.color.GREEN
# hue4 = arcade.color.YELLOW
class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,hue,tilt,sides):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.hue = hue
        self.tilt = tilt
        self.sides = sides

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.hue,self.tilt,self.sides)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        #bounce ball of edge of screen
        if self.pos_x < self.rad+22:
            self.dx *= -1
            self.hue = hue1
        if self.pos_x > SW-self.rad-22:
            self.dx*=-1
            self.hue = hue3
        if self.pos_y < self.rad+22:
            self.dy *= -1
            self.hue = hue2
        if self.pos_y > SH-self.rad-22:
            self.dy*=-1
            self.hue = hue4

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball_list=[]
        for i in range (30):
            rad = random.randint(10, 50)
            x = random.randint(rad+24,SW-rad-24)
            y = random.randint(rad+24,SH-rad-24)
            # x = 300
            # y = 300
            dx = random.randint(-5,5)
            dy = random.randint(-5, 5)
            hue = (random.randint(220, 255),random.randint(230, 255),random.randint(240, 255))
            if dx == 0:
                dx = random.randint(1, 3)
            if dy == 0:
                dy = random.randint(1, 3)
            self.ball = Ball(x,y,dx,dy,rad,hue,45,4)
            self.ball_list.append(self.ball)
    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, 30, 600, 0, hue1)
        arcade.draw_lrtb_rectangle_filled(0, 600, 30, 0, hue2)
        arcade.draw_lrtb_rectangle_filled(570, 600, 600, 0, hue3)
        arcade.draw_lrtb_rectangle_filled(0, 600, 600, 570, hue4)
        for i in (self.ball_list):
            i.draw_ball()

    def on_update(self, dt):
        for i in (self.ball_list):
            i.update_ball()
        # klk = random.randint(0,3)
        # if klk == 0:
        #     arcade.set_background_color(arcade.color.RED)
        # if klk == 1:
        #     arcade.set_background_color(arcade.color.BLUE)
        # if klk == 2:
        #     arcade.set_background_color(arcade.color.GREEN)
        # if klk == 3:
        #     arcade.set_background_color(arcade.color.YELLOW)
        # arcade.set_background_color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

def main():
    window = MyGame(SW,SH,"30 boxes")
    arcade.run()

if __name__ == "__main__":
    main()
    # blue light color scheme
    # random.randint(0, 255), random.randint(30, 255), random.randint(220, 255)