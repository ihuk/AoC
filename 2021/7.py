def main():
    ils = [int(s.strip()) for s in raw_input().split(',')]
    nls = max(ils) + 1
    ls = [0] * nls
    for l in ils:
        ls[l] += 1
    rs = [0] * nls
    for i in range(nls):
        for j in range(i + 1, nls):
            d = j - i
            fc = d * (d + 1) / 2
            rs[i] += (fc * ls[j])
            rs[j] += (fc * ls[i])
    print min([c for c in rs if c > 0])

if '__main__' == __name__:
    main()
