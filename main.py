WIDTH, HEIGHT = 50, 30

def render():
    for i in range(HEIGHT + 2):
        for j in range(WIDTH + 2):
            if i == 0 or i == HEIGHT+1 or j == 0 or j == WIDTH+1:
                print('█', end='')
            else:
                print('░', end='')
        print()

render()