class Constants:
    from pygame import display

    display.init()

    __dimensions = display.Info()
    __height = __dimensions.current_h
    __90_percent_screen_height = __height * 0.9

    GAME_WIDTH = 500
    GAME_HEIGHT = min(__90_percent_screen_height - (__90_percent_screen_height % 10), 700)
    GAME_VELOCITY = 0.02
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
