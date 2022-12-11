import sys


def main():
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
    print(sum([xs[c] * c for c in [20, 60,  100, 140, 180, 220]]))
    for c, x in list(enumerate(xs))[1:]:
        sprite = [x - 1, x, x + 1]
        sys.stdout.write("#" if (c - 1) % 40 in sprite else ".")
        if 0 == c % 40:
            print()


if '__main__' == __name__:
    main()
    
