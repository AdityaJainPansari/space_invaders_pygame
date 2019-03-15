
class Alien(object):
    def __init__(self, screen, tim, temp1, temp2):
        self.width = (int)(screen.get_width()/8)
        self.height = (int)(screen.get_height()/9)
        self.temp1 = temp1
        self.temp2 = temp2
        self.top = screen.get_height()-(7+temp1)*self.height
        self.left = screen.get_width()*temp2/8
        self.is_alive = 2
        self.alive_time = tim+8000

    def draw(self, screen, alien):
        if self.is_alive != -1:
            screen.blit(alien, (self.left, self.top))
        if self.is_alive == 0:
            self.is_alive = -1
