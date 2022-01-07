class Constants:
    from pygame import display

    display.init()

    __dimensions = display.Info()
    __width = __dimensions.current_w
    __height = __dimensions.current_h
    __90_percent_screen_width = __height * 0.9

    GAME_WIDTH = min(__width * 0.9, 600)
    GAME_HEIGHT = __90_percent_screen_width - (__90_percent_screen_width % 10)
    GAME_VELOCITY = 0.1
    SIZE = (GAME_WIDTH, GAME_HEIGHT)
    BREAKPOINT = GAME_HEIGHT // 2
    MAX_DISTANCE_TO_PARTICLES = 300

    class Colors:
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        YELLOW = (246, 255, 0)
        GRAY = (62, 62, 71)
        SMOOTH_BLACK = (46, 46, 46)

        LIST = YELLOW, RED, GREEN, WHITE
