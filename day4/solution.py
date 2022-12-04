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

fully_covering_pairs = [pair for pair in pairs if any_covers(pair[0], pair[1])]
print(f'Number of pairs in which one range fully covers the other = {len(fully_covering_pairs)}')
