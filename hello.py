print("Hello World")
print("Hello World1")
import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 蛇的初始位置和大小
snake_block = 20
snake_speed = 15
snake_list = []
snake_length = 1

# 初始化蛇的位置
x1 = width / 2
y1 = height / 2

# 初始化移动方向
x1_change = 0
y1_change = 0

# 生成食物
def our_food():
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
    return foodx, foody

foodx, foody = our_food()

# 游戏主循环
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # 移动蛇
    x1 += x1_change
    y1 += y1_change

    # 检查是否吃到食物
    if x1 == foodx and y1 == foody:
        foodx, foody = our_food()
        snake_length += 1

    # 绘制游戏元素
    window.fill(black)
    pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
    
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block, snake_block])

    pygame.display.update()

    # 控制游戏速度
    clock.tick(snake_speed)

# 退出游戏
pygame.quit()