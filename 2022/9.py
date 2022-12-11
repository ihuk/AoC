import sys


def main():
    ks = [(0, 0)] * 10
    ts = set(ks)
    ms = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    for direction, steps in [(d, int(s)) for d, s in [l.strip().split() for l in sys.stdin]]:
        print(f"{direction} {steps}")
        for _ in range(steps):
            dx, dy = ms[direction]
            ks[0] = (ks[0][0] + dx, ks[0][1] + dy)
            for i in range(1, len(ks)):
                h = ks[i - 1]
                t = ks[i]
                match (h[0] - t[0], h[1] - t[1]):
                    case (-2, 0):
                        t = (t[0] - 1, t[1])
                    case (-2, 1):
                        t = (t[0] - 1, t[1] + 1)
                    case (-1, 2):
                        t = (t[0] - 1, t[1] + 1)
                    case (0, 2):
                        t = (t[0], t[1] + 1)
                    case (1, 2):
                        t = (t[0] + 1, t[1] + 1)
                    case (2, 1):
                        t = (t[0] + 1, t[1] + 1)
                    case (2, 0):
                        #print(f"R {h}, {t}")
                        t = (t[0] + 1, t[1])
                    case (2, -1):
                        t = (t[0] + 1, t[1] - 1)
                    case (1, -2):
                        t = (t[0] + 1, t[1] - 1)
                    case (0, -2):
                        t = (t[0], t[1] - 1)
                    case (-1, -2):
                        t = (t[0] - 1, t[1] - 1)
                    case (-2, -1):
                        t = (t[0] - 1, t[1] - 1)
                    case _:
                        print("wtf: ", h[0] - t[0], h[1] - t[1])
                #print(f"head: {h}, tail {ks[i]} -> {t}")
                ks[i] = t
            #print(ks[-1])
            ts.add(ks[-1])
    print(ks)
    print(f"len: {len(ts)}") 


if '__main__' == __name__:
    main()

