import sys


def main():
    ss = [(map(int, s0.split('-')), map(int, s1.split('-'))) for s0, s1 in [l.strip().split(',') for l in sys.stdin]]
    sss = map(lambda (s0, s1): (s0, s1) if s0[1] - s0[0] > s1[1] - s1[0] else (s1, s0), ss)
    os = filter(lambda (s0, s1): s0[0] <= s1[0] <= s0[1] or s0[0] <= s1[1] <= s0[1], sss)
    print len(os)


if '__main__' == __name__:
    main()

