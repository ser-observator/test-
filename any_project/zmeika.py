import random 
import time
import curses
#кординаты поля
MAX_X=10
MIN_X=-10
MAX_Y=10
MIN_Y=-10
speed=1

def draw_flield(screen, snake, food):
    screen.clear()
    
    for row_index, y in enumerate(range(MAX_Y, MIN_Y - 1, -1)):
        row = ''
        for x in range(MIN_X, MAX_X + 1):
            if (x,y) == snake[0]:
                    row += 'H'
            elif (x,y) in snake:
                    row += 'o'
            elif (x,y) == food:
                    row += "*"
            else:
                    row +=" "
        screen.addstr(row_index, 0, row)
    screen.refresh()
def main(screen):
    snake = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    move= (0,-1)
    food= (
        random.randint(MIN_X, MAX_X), 
        random.randint(MIN_Y, MAX_Y)
           )
    moves_count=0
    game_running = True
    screen.nodelay(True)

    while game_running:
    
        key =  screen.getch()
        
        if key in (ord('w'), ord('W')) and move != (0,-1):
            move = (0,1)
        elif key in (ord('s'), ord('S')) and move != (0,1):
            move = (0,-1)
        elif key in (ord('a'), ord('A')) and move != (1,0):
            move = (-1,0)
        elif key in (ord('d'), ord('D')) and move != (-1,0):
            move = (1,0)
        elif key == (ord(' ')):
            break
        
        head_x, head_y = snake[0]
        new_head_x = head_x + move[0]
        new_head_y = head_y + move[1]
        new_head = (new_head_x, new_head_y)

        if new_head_x < MIN_X or new_head_x > MAX_X:
            game_running = False
        if new_head_y < MIN_Y or new_head_y > MAX_Y:
            game_running = False

        if new_head == food:
            food = (
                random.randint(MIN_X, MAX_X), 
                random.randint(MIN_Y, MAX_Y)
                )
        else:
            snake.pop()

        snake.insert(0, new_head)
        draw_flield(screen, snake, food)
        time.sleep(0.2/speed)


        moves_count += 1
        if moves_count > 100:
            game_running = False
            break
        
    # print (f'\n Game Over!')
    # print (f'Финал длина: {len(snake)}')
    # print (f'Позиция: {snake}')
curses.wrapper(main)