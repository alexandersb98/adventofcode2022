test_input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day3\test_input.txt'
input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day3\input.txt'

def get_input_lines(path: str):
    with open(path) as f:
        return f.readlines()

item_types = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_priority(item):
    return item_types.index(item) + 1

def get_priorities(items: str):
    return [get_priority(item) for item in items]

def get_duplicates(c1: str, c2: str):
    #return c1 and c2 [l for a in A if a in b]
    duplicates = []
    for item in c1:
        if (item in c2) and (item not in duplicates):
            duplicates.append(item)
    return duplicates

def get_string_halves(s: str):
    if s is '':
        return '', ''
    splitter = int(len(s) / 2)
    return s[:splitter], s[splitter:]

def get_compartments(rucksack: str):
    return get_string_halves(rucksack)
    

#--------------------------------------------




# PART 1

rucksacks = get_input_lines(path=test_input_file)
print(len(rucksacks))


priorities = get_priorities('pLPvts')
print(sum(priorities))

duplicates = get_duplicates('asdFF', 'dFghfF')
print(duplicates)

c1, c2 = get_compartments('asdf')
print(f'c1 = "{c1}"')
print(f'c2 = "{c2}"')

prio_sum = 0
for r in rucksacks:
    c1, c2 = get_compartments(r)
    duplicates = get_duplicates(c1, c2)
    priorities = get_priorities(duplicates)
    prio_sum += sum(priorities)

print(f'Total sum = {prio_sum}')