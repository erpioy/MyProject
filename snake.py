import pygame
import sys
import random

# pygame初始化
pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode((600, 600))

# 设置窗口标题
pygame.display.set_caption('Snake Game')

# 初始化 混音器
pygame.mixer.init()

# 添加背景音乐
pygame.mixer.music.load('ifyou.ogg')

pygame.mixer.music.set_volume(0.5)  # 设置音量为 50%
pygame.mixer.music.play(-1)  # 循环播放

# 颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

x, y = 0, 0


class Snack:
    def __init__(self, size):
        self.body = []
        self.size = size
        self.width = 25
        self.height = 25
        self.direction = 'A'

    def set_body(self):
        _x, _y = 300, 300
        for i in range(self.size):
            snack_rect = pygame.Rect(_x, _y, self.width, self.height)
            self.body.append(snack_rect)
            _x += 25

    def del_tail(self):
        self.body.pop()

    def add_head(self):
        if self.direction == 'A':
            _x = self.body[0].left - 25
            _y = self.body[0].top
        elif self.direction == 'D':
            _x = self.body[0].left + 25
            _y = self.body[0].top
        elif self.direction == 'W':
            _x = self.body[0].left
            _y = self.body[0].top - 25
        elif self.direction == 'S':
            _x = self.body[0].left
            _y = self.body[0].top + 25
        snack_rect = pygame.Rect(_x, _y, self.width, self.height)
        self.body.insert(0, snack_rect)

    def is_dead(self):
        flag = False
        if not (0 < self.body[0].left < 600 and 0 < self.body[0].top < 600):
            flag = True
        if self.body[0] in self.body[1:]:
            flag = True
        return flag


class Food:
    def __init__(self):
        self.width = 25
        self.height = 25
        self.rect = None

    def set_food(self):
        _x = self.width * random.randint(4, 20)
        _y = self.height * random.randint(4, 20)
        self.rect = pygame.Rect(_x, _y, self.width, self.height)


def set_font(text, left, top, size):
    font = pygame.font.Font('msyh.ttc', size)
    font_color = (227, 29, 18)
    text_surface = font.render(text, True, font_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (left, top)
    screen.blit(text_surface, text_rect)


def main():
    snake = Snack(5)
    snake.set_body()
    food = Food()
    food.set_food()

    # 游戏主循环
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_SPACE] and snake.is_dead():
                return main()

        # 改变移动方向

        if keys[pygame.K_a] and snake.direction != 'D':
            snake.direction = 'A'
        elif keys[pygame.K_d] and snake.direction != 'A':
            snake.direction = 'D'
        if keys[pygame.K_w] and snake.direction != 'S':
            snake.direction = 'W'
        elif keys[pygame.K_s] and snake.direction != 'W':
            snake.direction = 'S'

        # 填充颜色
        screen.fill(WHITE)
        # 蛇头
        if not snake.is_dead():
            snake.del_tail()
            snake.add_head()
        for body in snake.body:
            pygame.draw.rect(screen, PURPLE, body)
        # 食物
        pygame.draw.rect(screen, RED, food.rect)
        if snake.body[0].left == food.rect.left and snake.body[0].top == food.rect.top:
            snake.add_head()
            food.set_food()

        # TODO 计分功能

        if snake.is_dead():
            set_font('GAME OVER', 300, 200, 80)
            set_font('点击空格重新开始', 300, 250, 20)

        # 更新显示内容
        pygame.display.flip()

        # 设置帧率
        pygame.time.Clock().tick(10)


if __name__ == '__main__':
    main()
