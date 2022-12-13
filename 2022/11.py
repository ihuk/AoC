import sys
from tqdm import tqdm

d = {
    0: {
           'items': [64],
           'operation': lambda old: old * 7,
           'test': lambda x: 1 if 0 == x % 13 else 3,
       },

    1: {
           'items': [60, 84, 84, 65],
           'operation': lambda old: old + 7,
           'test': lambda x: 2 if 0 == x % 19 else 7,
       },

    2: {
           'items': [52, 67, 74, 88, 51, 61],
           'operation': lambda old: old * 3,
           'test': lambda x: 5 if 0 == x % 5 else 7,
       },

    3: {
           'items': [67, 72],
           'operation': lambda old: old + 3,
           'test': lambda x: 1 if 0 == x % 2 else 2,
       },

    4: {
           'items': [80, 79, 58, 77, 68, 74, 98, 64],
           'operation': lambda old: old * old,
           'test': lambda x: 6 if 0 == x % 17 else 0,
       },

    5: {
           'items': [62, 53, 61, 89, 86],
           'operation': lambda old: old + 8,
           'test': lambda x: 4 if 0 == x % 11 else 6,
       },

    6: {
           'items': [86, 89, 82],
           'operation': lambda old: old + 2,
           'test': lambda x: 3 if 0 == x % 7 else 0,
       },

    7: {
           'items': [92, 81, 70, 96, 69, 84, 83],
           'operation': lambda old: old + 4,
           'test': lambda x: 4 if 0 == x % 3 else 5,
       }
}


def main():
    r = {}
    for _ in tqdm(range(10000)):
        for m in d.keys():
            for i in d[m]['items']:
                r[m] = r.get(m, 0) + 1
                nwl = d[m]['operation'](i)
                nwl %= 9699690
                n = d[m]['test'](nwl)
                d[n]['items'].append(nwl)
            d[m]['items'] = []
    print(r)
    ma = sorted(r.values())[-2:]
    print(ma[0] * ma[1])


if "__main__" ==  __name__:
    main()


