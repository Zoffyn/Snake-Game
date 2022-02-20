import msvcrt
from random import randint
from time import sleep
from typing import Final

WIDTH: Final = 50
HEIGHT: Final = 20

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __eq__(self, other: 'Position') -> bool:
        if type(other) is not Position:
            raise TypeError(type(other))
        return self.x == other.x and self.y == other.y

    # for debug
    def __str__(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"

player: list[Position] = [Position(randint(1, WIDTH), randint(1, HEIGHT))]
food: Position

def put_food():
    global food
    food = Position(randint(1, WIDTH), randint(1, HEIGHT))
    while food == player[0]:
        food = Position(randint(1, WIDTH), randint(1, HEIGHT))

def shift_body(x:int, y: int):
    if len(player) > 1:
        for i in range(1, len(player)):
            px = player[i].x
            py = player[i].y
            player[i] = Position(x, y)
            x = px
            y = py

def move_up(move: bool = True) -> bool:
    if player[0].y > 1:
        if move:
            x = player[0].x
            y = player[0].y
            player[0].y -= 1
            shift_body(x, y)
        return True
    return False

def move_down(move: bool = True) -> bool:
    if player[0].y < HEIGHT:
        if move:
            x = player[0].x
            y = player[0].y
            player[0].y += 1
            shift_body(x, y)
        return True
    return False

def move_right(move: bool = True) -> bool:
    if player[0].x < WIDTH:
        if move:
            x = player[0].x
            y = player[0].y
            player[0].x += 1
            shift_body(x, y)
        return True
    return False

def move_left(move: bool = True) -> bool:
    if player[0].x > 1:
        if move:
            x = player[0].x
            y = player[0].y
            player[0].x -= 1
            shift_body(x, y)
        return True
    return False  

def extend_body():
    global current_movement
    tail = player[len(player) - 1]
    if len(player) == 1:
        if current_movement == move_up:
            player.append(Position(tail.x, tail.y + 1))
        elif current_movement == move_left:
            player.append(Position(tail.x + 1, tail.y))
        elif current_movement == move_down:
            player.append(Position(tail.x, tail.y - 1))
        else:
            player.append(Position(tail.x - 1, tail.y))
    else:
        dx = player[len(player) - 2].x - tail.x
        dy = player[len(player) - 2].y - tail.y
        if dy == -1:
            player.append(Position(tail.x, tail.y + 1))
        elif dx == -1:
            player.append(Position(tail.x + 1, tail.y))
        elif dy == 1:
            player.append(Position(tail.x, tail.y - 1))
        else:
            player.append(Position(tail.x - 1, tail.y))

def render() -> None:
    for y in range(HEIGHT + 2):
        for x in range(WIDTH + 2):
            if x == 0 or x == WIDTH+1 or y == 0 or y == HEIGHT+1:
                print('█', end='')
            else:
                if (pos := Position(x, y)) in player:
                    if pos == player[0]:
                        print('▣', end='')
                    else:
                        print('□', end='')
                elif Position(x, y) == food:
                    print('◉', end='')
                else:
                    print('░', end='')
        print()

def clear_screen() -> bool:
    print(f'\033[{WIDTH+2}D', end='')
    print(f'\033[{HEIGHT+2}A', end='')

current_movement = None

gameover: bool = False

put_food()

while not gameover:
    if food == player[0]:
        put_food()
        extend_body()
    render()
    clear_screen()
    if current_movement:
        current_movement()
    sleep(0.2)
    if msvcrt.kbhit():
        typed_character = msvcrt.getch()
        if typed_character == b'w':
            if current_movement != move_up and \
                current_movement != move_down and move_up(False):
                current_movement = move_up
        if typed_character == b'a':
            if current_movement != move_left and \
                current_movement != move_right and move_left(False):
                current_movement = move_left
        if typed_character == b's':
            if current_movement != move_down and \
                current_movement != move_up and move_down(False):
                current_movement = move_down
        if typed_character == b'd':
            if current_movement != move_right and \
                current_movement != move_left and move_right(False):
                current_movement = move_right