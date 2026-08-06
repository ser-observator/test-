import random 
import time
import curses
#кординаты поля
MAX_X=10
MIN_X=-10
MAX_Y=10
MIN_Y=-10

snake = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
move= (0,-1)
food= (5,5)
moves_count=0
game_running = True
while game_running:
    def draw_flield(snake, food):
        for y in range(MAX_Y,  MIN_Y - 1, -1):
            row = ''
            for x in range(MIN_X, MAX_X + 1):
                if (x,y) == snake[0]:
                    row += 'H'
                elif (x,y) in snake:
                    row += 'o'
                elif (x,y) == food:
                    row += "*"
                
    head_x, head_y = snake[0]
    new_head_x = head_x + move[0]
    new_head_y = head_y + move[1]
    new_head = (new_head_x, new_head_y)
    
    if new_head_x < MIN_X or new_head_x > MAX_X:
        game_running = False
    if new_head_y < MIN_Y or new_head_y > MAX_Y:
        game_running = False
    
    if new_head == food:
        food = (random.randint(MIN_X, MIN_Y), random.randint(MIN_X, MIN_Y))
        pass
    else:
        snake.pop()
        
    snake.insert(0, new_head)
    time.sleep(0.5)
    
    moves_count += 1
    if moves_count > 100:
        game_running = False

print (f'\n Game Over!')
print (f'Финал длина: {len(snake)}')
print (f'Позиция: {snake}')