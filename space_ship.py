class space_ship(object):
    def __init__(self, width, height, ship):
        self.ship = ship
        self.width = width
        self.height = height
        self.top = 7*height

    def movement(self, move_x, state1, state2):
        if state1 and not state2:
            move_x += (-1)*self.width
            if move_x < 50:
                move_x = 50
        elif state2 and not state1:
            move_x += self.width
            if move_x > 750:
                move_x = 750
        return move_x
