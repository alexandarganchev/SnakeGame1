import pygame
import time
import random

# Initialize the pygame library
pygame.init()

# Load and resize images
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (600, 400))
snake_head_image = pygame.image.load('snake.png')
snake_head_image = pygame.transform.scale(snake_head_image, (30, 30))  # Increased size
food_image = pygame.image.load('food.png')
food_image = pygame.transform.scale(food_image, (30, 30))  # Increased size

# Define colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
black = (0, 0, 0)

# Define display dimensions
dis_width = 600
dis_height = 400

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Define the clock
clock = pygame.time.Clock()
snake_block = 25
snake_speed = 8  # Reduced speed

# Define the font style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def our_snake(snake_list):
    for i, segment in enumerate(snake_list):
        if i == 0:
            dis.blit(snake_head_image, (segment[0], segment[1]))
        else:
            pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close == True:
            dis.blit(background_image, [0, 0])
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.blit(background_image, [0, 0])
        dis.blit(food_image, [foodx, foody])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.insert(0, snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[-1]

        for segment in snake_List[1:]:
            if segment == snake_Head:
                game_close = True

        our_snake(snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
