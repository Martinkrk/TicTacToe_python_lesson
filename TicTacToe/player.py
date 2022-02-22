from pygame.constants import SRCCOLORKEY


class Player:
    p_list = []
    count = 0
    def __init__(self):
        self.score = 0
        Player.count += 1
        Player.p_list.append(self)
        self.mark = Player.count