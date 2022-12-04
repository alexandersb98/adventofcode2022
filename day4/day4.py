with open(r'day4/input.txt',) as f:
    lines = f.read().rsplit()

pairs = [tuple(l.split(',')) for l in lines]

pairs = list(
    map(
        lambda p: tuple([tuple(x.split('-')) for x in p]), pairs
    )
)

pairs = list(
    map(
        lambda pair: tuple(
            map(
                lambda interval: (int(interval[0]), int(interval[1])), pair
            )
        ),
        pairs
    )
)

def any_covers(a, b):
    return covers(a, b) or covers(b, a)

def covers(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

def overlaps(a: tuple, b: tuple):
    left_is_contained = a[0] in range(b[0], b[1]+1)
    right_is_contained = a[1] in range(b[0], b[1]+1)
    return left_is_contained or right_is_contained or any_covers(a,b)

# Part 1
fully_covering_pairs = [pair for pair in pairs if any_covers(pair[0], pair[1])]
print(f'Number of pairs in which one range fully covers the other = {len(fully_covering_pairs)}')

# Part 2
overlapping_pairs = [p for p in pairs if overlaps(p[0], p[1])]
print(f'Number of pairs that overlap each other = {len(overlapping_pairs)}')