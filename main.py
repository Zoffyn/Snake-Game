import msvcrt
from random import randint
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

def move_up() -> None:
    if player[0].y > 1:
        player[0].y -= 1

def move_down() -> None:
    if player[0].y < HEIGHT:
        player[0].y += 1

def move_right() -> None:
    if player[0].x < WIDTH:
        player[0].x += 1

def move_left() -> None:
    if player[0].x > 1:
        player[0].x -= 1  

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
                else:
                    print('░', end='')
        print()

def clear_screen() -> bool:
    print(f'\033[{WIDTH+2}D', end='')
    print(f'\033[{HEIGHT+2}A', end='')

gameover: bool = False

while not gameover:
    render()
    clear_screen()
    if msvcrt.kbhit():
        typed_character = msvcrt.getch()
        if typed_character == b'w':
            move_up()
        if typed_character == b'a':
            move_left()
        if typed_character == b's':
            move_down()
        if typed_character == b'd':
            move_right()