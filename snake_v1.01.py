import pygame
import random
import sys
from pygame import Vector2, Color, Rect

class GameMain:
    def __init__(self):
        print("Game Start...")
        pygame.init()
        self.s = Snake()
        self.f = Fruit()
        self.soc = Scores()
        self.speed = 1000

    def speed_plus(self, speed):
        pygame.time.set_timer(MYEVENT_TIME1, speed)

    def check_event(self):
        self.s.snake_draw()
        self.f.fruit_draw()
        self.soc.soc_draw(str(self.get_scores()))
        self.check_collision()

        if self.check_board() == 0:
            self.game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self.game_over()
                pygame.quit()
                sys.exit()
            if event.type == MYEVENT_TIME1:
                self.s.snake_update(self.s.get_direction())
                self.get_scores()
                # print("TIME1 work")
            if event.type == MYEVENT_TIME2:
                if self.speed > 100:
                    self.speed -= 100
                self.speed_plus(self.speed)
                print(self.speed)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("up")
                    if self.s.get_direction() != down:
                        self.s.snake_update(up)
                elif event.key == pygame.K_DOWN:
                    print("down")
                    if self.s.get_direction() != up:
                        self.s.snake_update(down)
                elif event.key == pygame.K_LEFT:
                    print("left")
                    if self.s.get_direction() != right:
                        self.s.snake_update(left)
                elif event.key == pygame.K_RIGHT:
                    print("right")
                    if self.s.get_direction() != left:
                        self.s.snake_update(right)

    def check_collision(self):
        if self.f.fruit_vect == self.s.snake[0]:
            print("we meet!")
            self.s.flag_collision = True
            self.f.fruit_update()

    def check_board(self):
        x = int(self.s.snake[0].x)
        y = int(self.s.snake[0].y)
        if x < 0 or x > screen_x-1:
            return 0
        if y < 0 or y > screen_y-1:
            return 0
        for s in self.s.snake[1:]:
            if self.s.snake[0] == s:
                return 0
    def get_scores(self):
        return (len(self.s.snake)-3)

    def game_over(self):
        self.__init__()

class Fruit:
    """
    1. 水果类
    """
    def __init__(self):
        self.fruit_vect = self.fruit_random()

    def fruit_draw(self):
        x = int(self.fruit_vect.x)*cell_size
        y = int(self.fruit_vect.y)*cell_size
        rect = Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, Color('red'), rect)

    def fruit_update(self):
        self.fruit_vect = self.fruit_random()

    def fruit_random(self):
        x = random.randint(1,screen_x - 1)
        y = random.randint(1, screen_y -1)
        return Vector2(x,y)

class Snake:
    """
    1. 蛇类
    """
    def __init__(self):
        self.snake = [Vector2(10,10), Vector2(9,10), Vector2(8,10)]
        self.flag_collision = False

    def snake_draw(self):
        for s in self.snake:
            x = int(s.x)*cell_size
            y = int(s.y)*cell_size
            rect = Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, Color('green'), rect)

    def snake_update(self, direction):
        head = self.snake[0]

        if self.flag_collision == False:
            body = self.snake[: -1]
        else:
            body = self.snake[:]

        # direction = self.snake[0] - self.snake[1]
        self.snake = [head + direction] + body
        self.flag_collision = False



    def get_direction(self):
        return self.snake[0] - self.snake[1]

class Scores:
    def __init__(self):
        pygame.font.init()
        self.myfont = pygame.font.Font(pygame.font.get_default_font(), 30)

    def soc_draw(self,scores):
        font_image = self.myfont.render(scores, False, Color('yellow'))
        screen.blit(font_image, (200, 0))


# 程序入口
if __name__ == "__main__":

    cell_size = 20
    screen_x, screen_y = 20, 30
    screen = pygame.display.set_mode((cell_size * screen_x, cell_size * screen_y))
    pygame.display.set_caption("Snake Game")

    # set clock
    MYEVENT_TIME1 = pygame.USEREVENT + 1
    MYEVENT_TIME2 = pygame.USEREVENT + 2

    clock = pygame.time.Clock()
    pygame.time.set_timer(MYEVENT_TIME1, 1000)
    pygame.time.set_timer(MYEVENT_TIME2, 10000)

    # define direction vector
    up = Vector2(0, -1)
    down = Vector2(0, 1)
    left = Vector2(-1, 0)
    right = Vector2(1, 0)

    game = GameMain()

    while True:
        screen.fill(Color('blue')) # 背景图

        game.check_event()      # 事件检测

        pygame.display.update()  # 刷新
        clock.tick(60)          # 刷新率 60fps



