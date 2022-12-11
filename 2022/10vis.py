import sys
import curses
from time import sleep

def main(screen):
    screen.clear()
    curses.curs_set(False)
    x = 1
    xs = [1]
    for instruction in [l.split() for l in [l.strip() for l in sys.stdin]]:
        match instruction:
            case ['noop']:
                xs.append(x) 
            case ['addx', v]:
                xs.append(x)
                xs.append(x)
                x += int(v)
    for c, x in list(enumerate(xs))[1:]:
        sprite = [x - 1, x, x + 1]
        screen.addstr(0, 44, f"C: {c}")
        screen.addstr(1, 44, f"X: {x}")
        #screen.addstr(1, 45, f"S: {'▐' if c - 1 in sprite else '・'}")
        screen.addstr((c - 1) // 40, (c - 1) % 40, "▐" if (c - 1) % 40 in sprite else " ")
        screen.refresh()
        sleep(.015)
    sleep(60)

if '__main__' == __name__:
    curses.wrapper(main)

    
