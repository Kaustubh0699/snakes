import pygame
import random

display_width = 600
display_height = 600
green = (0,255,0)
red = (255,0,0)
black = (255,255,255)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()

def apple(x,y,w,h):
    pygame.draw.rect(gameDisplay , red ,(x,y,w,h))

def snake(snakeList,w,h):
    for x in snakeList:
        pygame.draw.rect(gameDisplay ,green, (x[0],x[1],w,h))

def end():
    pygame.quit()
    quit()

    
def main_func():
    snake_x = display_width//2
    snake_y = display_height//2
    snake_x_move = 0
    snake_y_move = 0
    snake_height =30
    snake_width = 30

    snakeList = []
    snakelen = 1

    apple_x = random.randrange(0,display_width)
    apple_y = random.randrange(0,display_height)
    apple_height = 30
    apple_width = 30
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_y_move = 0
                    snake_x_move = -10
                if event.key == pygame.K_RIGHT:
                    snake_y_move = 0
                    snake_x_move = 10
                if event.key == pygame.K_UP:
                    snake_x_move = 0
                    snake_y_move = -10
                if event.key == pygame.K_DOWN:
                    snake_x_move = 0
                    snake_y_move = 10

        if (snake_x <= 0):
            snake_x = display_width
        elif(snake_x >= display_width):
            snake_x = 0
        elif(snake_y <= 0):
            snake_y = display_height
        elif(snake_y >=display_width):
            snake_y =0
        snake_x += snake_x_move
        snake_y += snake_y_move
        gameDisplay.fill(black)

        snakeHead = []
        snakeHead.append(snake_x)
        snakeHead.append(snake_y)
        snakeList.append(snakeHead)

        if(len(snakeList) > snakelen):
            del(snakeList[0])

        for element in snakeList[:-1]:
            if(element == snakeHead):
                end()

        snake(snakeList,snake_width,snake_height)

        apple(apple_x,apple_y,apple_width,apple_height)

        if((snake_x + snake_width >= apple_x) and (snake_x <= apple_x + apple_width)):
            if ((snake_y + snake_height >= apple_y) and (snake_y <= apple_y + apple_height)):
                apple_x = random.randrange(0, display_width)
                apple_y = random.randrange(0, display_height)
                apple(apple_x, apple_y, apple_width, apple_height)
                snakelen +=5
        pygame.display.update()

        clock.tick(30)


main_func()
end()



