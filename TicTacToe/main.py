from pygame.constants import SCRAP_SELECTION
from setting import Setting
from grid import Grid
from player import Player
import pygame
from math import ceil

setting = Setting()
p1 = Player()
p2 = Player()

screen = pygame.display.set_mode(setting.size)
setting.window = screen
clock = pygame.time.Clock()
pygame.display.flip()
grid = Grid(setting)

won = False
is_first = True
going = True
while going:
    clock.tick(setting.fps)
    pygame.display.set_caption("Tic-Tac-Toe by Martin")
    pygame.font.init()
    bottom_font = pygame.font.SysFont('Comic Sans MS', 60)

    big_x = bottom_font.render('X', False, (0, 0, 0))
    screen.blit(big_x,(setting.width/2-setting.bottom_box-setting.cell_size/4,setting.height-setting.bottom_box/2-setting.bottom_box/2))
    big_xm = bottom_font.render(f'{p1.score}', False, (0, 0, 0))
    screen.blit(big_xm,(setting.width/2-setting.bottom_box-setting.cell_size/4,setting.height-setting.bottom_box/2-setting.bottom_box/8))

    big_o = bottom_font.render('O', False, (0, 0, 0))
    screen.blit(big_o,(setting.width/2+setting.bottom_box,setting.height-setting.bottom_box/2-setting.bottom_box/2))
    big_om = bottom_font.render(f'{p2.score}', False, (0, 0, 0))
    screen.blit(big_om,(setting.width/2+setting.bottom_box,setting.height-setting.bottom_box/2-setting.bottom_box/8))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False
            if event.key == pygame.K_r:
                grid.ResetGame()
                is_first = True
                won = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if won:
                won = False
                is_first = True
                grid.ResetGrid()
            else:
                mx,my = pygame.mouse.get_pos()
                x = ceil(mx/setting.cell_size)
                y = ceil(my/setting.cell_size)
                if y == 4:
                    pass
                else:
                    if is_first:
                        if grid.Instantiate(x,y,p1.mark) != 0:
                            is_first = False
                            if grid.win_check(p1.mark):
                                center_message = bottom_font.render('X won!', False, (0, 0, 0))
                                screen.blit(center_message,(setting.width/2-setting.bottom_box/2,setting.height-setting.bottom_box/2-setting.bottom_box/4))
                                won = True
                                p1.score += 1

                    elif not is_first:
                        if grid.Instantiate(x,y,p2.mark) != 0:
                            is_first = True
                            if grid.win_check(p2.mark):
                                center_message = bottom_font.render('O won!', False, (0, 0, 0))
                                screen.blit(center_message,(setting.width/2-setting.bottom_box/2,setting.height-setting.bottom_box/2-setting.bottom_box/4))
                                won = True
                                p2.score += 1
            if grid.draw_check() == 9:
                grid.ResetGrid()
                is_first = True

    pygame.display.flip()
