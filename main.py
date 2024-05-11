import time
import random

def clamp(a, min, max):
    if a < min:
        return min
    if a > max:
        return max
    return a
def move (y, x):
    print("\033[%d;%dH" % (y, x))
w, h = 80, 40
chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
def RGB(red=None, green=None, blue=None,bg=False):
    if(bg==False and red!=None and green!=None and blue!=None):
        return f'\u001b[38;2;{red};{green};{blue}m'
    elif(bg==True and red!=None and green!=None and blue!=None):
        return f'\u001b[48;2;{red};{green};{blue}m'
    elif(red==None and green==None and blue==None):
        return '\u001b[0m'

matrix = []
drops = []
for i in range(w * h):
    matrix.append(0)

def frame():
    for i, (x, y) in enumerate(drops):
        if y > h - 1:
            drops.pop(i)
        else:
            drops[i] = (x, y + 1)

    for i in range(w * h):
        a = matrix[i]
        a -= 20
        if a < 0:
            a = 0
        matrix[i] = a

    for i, (x, y) in enumerate(drops):
        matrix[get_index(x, y)] = 255.0

def get_index(x, y):
    return x * h + y

def render():
    move(0, 0)
    for y in range(h):
        print(RGB(0, 0, 0, True), end="")
        for x in range(w):
            luminance = int(matrix[get_index(x, y)])
            char = chars[clamp(int(float(luminance) / 255 * len(chars)), 0, len(chars) - 1)]
            print(RGB(0, luminance, 0) + char if luminance > 10 else " ", end="")
        print(RGB())

def create_drop():
    drops.append((int(random.uniform(1, w - 1)), 0))

while True:
    time.sleep(0.1)
    create_drop()
    render()
    frame()
