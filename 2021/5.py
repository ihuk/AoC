import sys

def main():
    grid = {}
    for l in sys.stdin:
        start, end = l.replace(' ', '').split('->')
        xs, ys = [int(s.strip()) for s in start.split(',')]
        xe, ye = [int(s.strip()) for s in end.split(',')]
        dx = xe - xs if xe >= xs else xs - xe
        dy = ys - ye if ye >= ys else ye - ys
        sx = 1 if xs < xe else -1
        sy = 1 if ys < ye else -1
        err = dx + dy
        while True:
            p = (xs, ys)
            grid[p] = grid.get(p, 0) + 1
            if xs == xe and ys == ye:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                xs += sx
            if e2 <= dx:
                err += dx
                ys += sy
    print len([c for c in grid.values() if c >= 2])


if '__main__' == __name__:
    main()
