

import arcade
import random
SW = 600
SH = 600

class line():
    def __init__(self,pos_x,pos_y,dx,dy,rad,hue):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.hue = hue

    def draw_line(self):
        arcade.draw_line(self.pos_x,self.pos_y, self.dx,self.dy,self.hue)

    def update_line(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        # bounce ball of edge of screen
        if self.pos_x < self.rad:
            self.dx *= -1
        if self.pos_x > SW - self.rad:
            self.dx *= -1
        if self.pos_y < self.rad:
            self.dy *= -1
        if self.pos_y > SH - self.rad:
            self.dy *= -1





class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.line_list=[]
        for i in range (1):
            rad = random.randint(3, 9)
            x = random.randint(rad,SW-rad)
            y = random.randint(rad,SH-rad)
            dx = random.randint(1,1)
            dy = random.randint(0, 0)
            hue = (random.randint(0,200),random.randint(40, 230),random.randint(200, 230))
            hue = (arcade.color.RED)
            # if dx == 0:
            #     dx = random.randint(1, 3)
            # if dy == 0:
            #     dy = random.randint(-3, -1)
            self.line = line(x,y,dx,dy,rad,hue)
            self.line_list.append(self.line)
    def on_draw(self):
        arcade.start_render()
        for i in (self.line_list):
            i.draw_line()

    def on_update(self, dt):
        for i in (self.line_list):
            i.update_line()
        rad = random.randint(5, 40)
        x = random.randint(40,560)
        y = random.randint(40,560)
        dx = random.randint(1, 1)
        dy = random.randint(0, 0)
        hue = (random.randint(0,200),random.randint(40, 230),random.randint(200, 230))
        # hue = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        chance = random.randint(0,30)

        if chance == 0:
            self.line = line(x, y, dx, dy, rad, hue)
            self.line_list.append(self.line)




def main():
    window = MyGame(SW,SH,"Beamlights")
    arcade.run()

if __name__ == "__main__":
    main()