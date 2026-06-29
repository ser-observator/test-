#кординаты поля
MAX_X=10
MIN_X=-10
MAX_Y=10
MIN_Y=-10

snake = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
move= (0,-1)
food= (5,5)
game_running = True
while game_running:
    
    
    
    head_x, head_y = snake[0]
    new_head_x = head_x + move[0]
    new_head_y = head_y + move[1]
    new_head = (new_head_x, new_head_y)
    
    if new_head_x < MIN_X or new_head_x > MAX_X:
        game_running = False
    if new_head_y < MIN_Y or new_head_y > MAX_Y:
        game_running = False
    
    if new_head == food:
        pass
    else:
        snake.pop()
        
    snake.insert(0, new_head)
    