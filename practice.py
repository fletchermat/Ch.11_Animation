import arcade
import random
SW = 640
SH = 480

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
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        #bounce ball of edge of screen
        if self.pos_x < self.rad or self.pos_x > SW-self.rad:
            self.dx*=-1
        if self.pos_y < self.rad or self.pos_y > SH-self.rad:
            self.dy*=-1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball_list=[]
        for i in range (110):
            rad = random.randint(10, 100)
            x = random.randint(rad,SW-rad)
            y = random.randint(rad,SH-rad)
            dx = random.randint(-2,2)
            dy = random.randint(-2, 2)
            hue = (random.randint(200, 230),random.randint(0, 200),random.randint(50, 255))
            if dx == 0:
                dx = random.randint(1, 3)
            if dy == 0:
                dy = random.randint(1, 3)
            self.ball = Ball(x,y,dx,dy,rad,hue)
            self.ball_list.append(self.ball)
    def on_draw(self):
        arcade.start_render()
        for i in (self.ball_list):
            i.draw_ball()

    def on_update(self, dt):
        for i in (self.ball_list):
            i.update_ball()

def main():
    window = MyGame(SW,SH,"Drawing Example")
    arcade.run()

if __name__ == "__main__":
    main()