from graphics import BulletinBoard, Poster
from graphics import Rectangle, Circle, TextBox


class BrickWall(Poster):

    def __init__(self, width, height, color_matrix,
                 color_map, outline_bricks):
        super().__init__()
        brick = Rectangle(width, height, "#0000FF",
                          filled=True, outlined=outline_bricks)
        self.pin(brick, 0, 0)


class BreakoutGame:

    def __init__(self, config):
        self.board = BulletinBoard(config.get_board_width(),
                                   config.get_board_height())
        self.wall = BrickWall(self.board.get_width(),
                              self.board.get_height()*0.3,
                              config.get_color_matrix(),
                              config.get_color_map(),
                              config.outline_bricks())
        self.board.pin(self.wall, 0, 0.1 * self.board.get_height())

    def start(self):
        pass