class Setting:
    width = 600
    height = 800
    bottom_box = 200
    size = (width,height)
    fps = 60
    window = None

    cell_size = 200
    cols = (height-bottom_box)//cell_size
    rows = (height-bottom_box)//cell_size

    black = (0,0,0)
    white = (255,255,255)
    winline = (0,255,0)
