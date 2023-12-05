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
    print(translation_maps)
    locations = []
    for s in seeds:
        location = s
        for m in translation_maps:
            for ss, ds, rl in translation_maps[m]:
                if ss <= location < (ss + rl):
                    #print(f'{m}: {ss} <= {location} < {ss + rl}: {location} -> {ds + (location - ss)}')
                    location = ds + (location - ss)
                    break
        locations.append(location)
    print(min(locations))
    locations = []
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
    for srs, sre in seed_ranges:
        for s in range(srs, sre):
            location = s
            for m in translation_maps:
                for ss, ds, rl in translation_maps[m]:
                    if location < ss:
                        continue
                    if ss <= location < (ss + rl):
                        location = ds + (location - ss)
                        break
            locations.append(location)
    print(min(locations))


if '__main__' == __name__:
    main()


