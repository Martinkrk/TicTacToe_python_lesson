import pygame
import random
from player import Player
from setting import Setting

class Grid(Player):
    def __init__(self,setting):
        self.rows = setting.rows + 1
        self.cols = setting.cols + 1
        self.cell_size = setting.cell_size
        self.screen = setting.window
        self.winline = setting.winline
        self.width = setting.width
        #
        self.cgrid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.setting = setting
        self.screen.fill((255,255,255))
        pygame.draw.line(self.screen,(0,0,0),(1*self.cell_size,0),(1*setting.cell_size,setting.height-self.cell_size),5)
        pygame.draw.line(self.screen,(0,0,0),(2*self.cell_size,0),(2*setting.cell_size,setting.height-self.cell_size),5)
        [pygame.draw.line(self.screen,(0,0,0),(0,x*self.cell_size),(setting.width,x*setting.cell_size),5) for x in range(self.rows)]
        pygame.draw.line(self.screen,(0,0,0),(0,3*self.cell_size),(setting.width,3*setting.cell_size),5)
                

    def ResetGrid(self):
        self.__init__(self.setting)

    def ResetGame(self):
        for obj in Player.p_list:
            obj.score = 0
        self.__init__(self.setting)

    def Instantiate(self,x,y,xo):
        try:
            if self.cgrid[x-1][y-1] != 0:
                return 0
            self.cgrid[x-1][y-1] = xo
        except:
            pass
        
        if xo == 1:
            pygame.draw.line(self.screen,(0,0,0),(x*200-self.cell_size/3-100,y*200-self.cell_size/3-100),(x*200+self.cell_size/3-100,y*200+self.cell_size/3-100),15)
            pygame.draw.line(self.screen,(0,0,0),(x*200+self.cell_size/3-100,y*200-self.cell_size/3-100),(x*200-self.cell_size/3-100,y*200+self.cell_size/3-100),15)
        else:
            pygame.draw.circle(self.screen,(0,0,0),(x*200-(self.cell_size/2),y*200-(self.cell_size/2)), 75,15)

    def win_check(self, pmark):
        for i in range(3):
            if (self.cgrid[0:-1][i].count(pmark) == 3) or (self.cgrid[0][i] == pmark and self.cgrid[1][i] == pmark and self.cgrid[2][i] == pmark) or (self.cgrid[0][0] == pmark and
             self.cgrid[1][1] == pmark and self.cgrid[2][2] == pmark) or (self.cgrid[2][0] == pmark and self.cgrid[1][1] == pmark and self.cgrid[0][2] == pmark):
                return 1
        return 0

    def draw_check(self):
        total = 0
        for i in range(1,3):
            for x in range(3):
                total += self.cgrid[x].count(i)
        return total
