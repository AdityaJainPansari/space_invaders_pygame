class Missile(object):
    def __init__(self, x, screen):
        self.width = (int)(screen.get_width()/8)
        self.height = (int)(screen.get_height()/9)
        self.top = screen.get_height()-2*self.height
        self.left = x
        self.is_alive = True
