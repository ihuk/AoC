import sys
from collections import defaultdict


MAPS = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]


def main():
    seeds = []
    translation_maps = defaultdict(dict)
    almanac = [l.strip() for l in sys.stdin]
    _, ss = almanac.pop(0).split(':')
    seeds = [int(s) for s in ss.split()]
    almanac.pop(0)
    for m in MAPS:
        almanac.pop(0)
        while True:
            if not almanac:
                break
            l = almanac.pop(0)
            if not l:
                break
            ds, ss, rl = map(int, l.split())
            for s, d in zip(range(ss, ss + rl), range(ds, ds + rl)):
                translation_maps[m][s] = d
    print("computed translation tables")
    locations = []
    for s in seeds:
        location = s
        for m in translation_maps:
            location = translation_maps[m].get(location, location)
        locations.append(location)
    print(min(locations))

if '__main__' == __name__:
    main()

