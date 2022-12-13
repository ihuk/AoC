import sys


def main():
    moves = {'L': (-1, ), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    offsets = {
    knots = [(0, 0)] * 10
    trail = set(knots)
    print trail
    for direction, steps in [(d, int(s)) for d, s in [l.strip().split() for l in sys.stdin]]:
        for _ in range(steps):
            dx, dy = moves[direction]
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(1, len(knots)):
                h = knots[i - 1]
                t = knots[i]
                if abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2:
                    continue
                if h[0] == t[0] or h[1] == t[1]:
                    t = (t[0] + dx, t[1] + dy)
                else:
                    t = (t[0] + dx if dx else h[0], t[1] + dy if dy else h[1])
                knots[i] = t
            trail.add(knots[-1])
    print len(trail)


if '__main__' == __name__:
    main()

