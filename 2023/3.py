import re
import sys

SYMBOLS = '@#%$&+*-/='

def main():
    gears = {}
    part_numbers = []
    schematic = [l.strip() for l in sys.stdin]
    for i, l in enumerate(schematic):
        for number in re.finditer(r'\b\d+\b', l):
            for y in [i + o for o in [-1, 0, 1] if i + o >= 0 and i + o < len(l)]:
                start = number.start() - 1 if number.start() > 0 else number.start()
                symbols = [(c, x + start) for x, c in enumerate(schematic[y][start:number.end() + 1]) if c in SYMBOLS]
                if symbols:
                    part_number = int(number.group())
                    part_numbers.append(part_number)
                    for x in [x for c, x in symbols if '*' == c]:
                        gears.setdefault((x,y), []).append(part_number)
    print(sum(part_numbers))
    print(sum([reduce(lambda g0, g1: g0 * g1, gears[adjecent]) for adjecent in gears.keys() if 2 == len(gears[adjecent])]))




if '__main__' == __name__:
    main()



