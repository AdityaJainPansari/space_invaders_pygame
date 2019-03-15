from Missile import Missile


class Missile2(Missile):
    def draw(self, screen, bullet2):
        screen.blit(bullet2, (self.left, self.top))

    def update(self, screen):
        self.top -= self.height
        if self.top < 0:
            self.is_alive = False
