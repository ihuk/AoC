import sys

def main():
    g = []
    rs = 0
    cs = 0
    for l in sys.stdin:
        r = [int(s) for s in l.strip()]
        g += r
        rs += 0
        cs = len(r)
    print g

if '__main__' == __name__:
    main()
