import sys
from collections import defaultdict
from itertools import count

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
    translation_maps = defaultdict(list)
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
            translation_maps[m].append((ss, ds, rl))
    locations = []
    for s in seeds:
        location = s
        for m in translation_maps:
            for ss, ds, rl in translation_maps[m]:
                if ss <= location < (ss + rl):
                    location = ds + (location - ss)
                    break
        locations.append(location)
    print(min(locations))
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
    for i in count(): 
        location = i
        for m in reversed(translation_maps):
            for ss, ds, rl in translation_maps[m]:
                if ds <= location < (ds + rl):
                    location = ss + (location - ds)
                    break
        if any([srs <= location < sre for srs, sre in seed_ranges]):
            print(i)
            break


if '__main__' == __name__:
    main()


