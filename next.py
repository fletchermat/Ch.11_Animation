

import arcade
import random
SW = 600
SH = 600

class Ball():
    def __init__(self,pos_x,pos_y,pos_x2,pos_y2,dx,dy,dx2,dy2,rad,hue):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.pos_x2 = pos_x2
        self.pos_y2 = pos_y2
        self.dx2 = dx2
        self.dy2 = dy2
        self.rad = rad
        self.hue = hue

    def draw_ball(self):
        arcade.draw_line(self.pos_x,self.pos_y, self.pos_x2,self.pos_y2,self.hue,self.rad)

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        self.pos_x2 += self.dx2
        self.pos_y2 += self.dy2
        # bounce ball of edge of screen
        if self.pos_x < 0:
            self.dx *= -1
        if self.pos_x > SW:
            self.dx *= -1
        if self.pos_y < 0:
            self.dy *= -1
        if self.pos_y > SH:
            self.dy *= -1

        if self.pos_x2 < 0:
            self.dx2 *= -1
        if self.pos_x2 > SW:
            self.dx2 *= -1
        if self.pos_y2 < 0:
            self.dy2 *= -1
        if self.pos_y2 > SH:
            self.dy2 *= -1





class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_list=[]
        for i in range (1):
            rad = random.randint(1, 3)
            x = random.randint(40, 560)
            y = random.randint(40, 560)
            x2 = random.randint(40, 560)
            y2 = random.randint(40, 560)
            dx = random.randint(1,1)
            dy = random.randint(0, 1)
            dx2 = random.randint(1, 1)
            dy2 = random.randint(1, 1)
            hue = (arcade.color.RED)
            if dx == 0:
                dx = random.randint(1, 3)
            if dy == 0:
                dy = random.randint(-3, -1)
            if dx2 == 0:
                dx2 = random.randint(1, 3)
            if dy2 == 0:
                dy2 = random.randint(-3, -1)
            self.ball = Ball(x, y, x2, y2, dx, dy, dx2, dy2, rad, hue)
            self.ball_list.append(self.ball)
    def on_draw(self):
        arcade.start_render()
        for i in (self.ball_list):
            i.draw_ball()

    def on_update(self, dt):
        for i in (self.ball_list):
            i.update_ball()
        rad = random.randint(1, 3)
        x = random.randint(40,560)
        y = random.randint(40,560)
        x2 = random.randint(40, 560)
        y2 = random.randint(40, 560)
        dx = random.randint(1, 3)
        dy = random.randint(1, 3)
        dx2 = random.randint(1, 3)
        dy2 = random.randint(1, 3)
        hue = (random.randint(0,200),random.randint(40, 230),random.randint(200, 230))
        chance = random.randint(0,10)
        if chance == 0:
            self.ball = Ball(x, y, x2, y2, dx, dy, dx2, dy2, rad, hue)
            self.ball_list.append(self.ball)





def main():
    window = MyGame(SW,SH,"Rainfall")
    arcade.run()

if __name__ == "__main__":
    main()