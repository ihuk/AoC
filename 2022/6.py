import sys


def main():
    b = sys.stdin.readline()
    psb = filter(lambda s: len(s[1]) == 4, [(i, set(b[i:i + 4])) for i, _ in enumerate(b)])
    msb = filter(lambda s: len(s[1]) == 14, [(i, set(b[i:i + 14])) for i, _ in enumerate(b)])
    print psb[0][0] + 4 
    print msb[0][0] + 14 



if '__main__' == __name__:
    main()



