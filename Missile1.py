from Missile import Missile


class Missile1(Missile):
    def draw(self, screen, bullet1):
        screen.blit(bullet1, (self.left, self.top))

    def update(self, screen):
        self.top -= self.height/2
        if self.top < 0:
            self.is_alive = False
