def get_input_lines(path: str):
    with open(path) as f:
        return f.readlines()

item_types = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_priority(item):
    return item_types.index(item) + 1

def get_priorities(items: str):
    return [get_priority(item) for item in items]

def get_duplicates(c1: str, c2: str):
    return {item for item in c1 if item in c2 and item != '\n'}

def get_string_halves(s: str):
    if s == '':
        return '', ''
    splitter = int(len(s) / 2)
    return s[:splitter], s[splitter:]

def get_compartments(rucksack: str):
    return get_string_halves(rucksack)
    
def get_groups(lines: list): 
    group_size = 3
    n_groups = int(len(lines) / group_size)
    
    groups = []
    for i in range(n_groups):
        a = group_size*i
        b = a+group_size
        group = lines[a:b]
        groups.append(group)
    return groups

def get_badge(group):
    a,b,c = group
    duplicates = get_duplicates(a, get_duplicates(b, c))
    badge = list(duplicates)[0]
    return badge

def get_badges(groups: list):
    return [get_badge(group) for group in groups]


#--------------------------------------------
# PART 1

test_input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day3\test_input.txt'
input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day3\input.txt'

rucksacks = get_input_lines(path=input_file)

prio_sum = 0
for r in rucksacks:
    c1, c2 = get_compartments(r)
    duplicates = get_duplicates(c1, c2)
    priorities = get_priorities(duplicates)
    prio_sum += sum(priorities)

print(f'Total sum = {prio_sum}')

#--------------------------------------------
# PART 2

test_input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day3\test_input2.txt'
input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day3\input2.txt'

lines = get_input_lines(path=input_file)
groups = get_groups(lines)

group1 = groups[1]
elf_a, elf_b, elf_c = group1
badge = get_badge(group1)
print(badge)

badges = get_badges(groups)

print(badges)

priorities = get_priorities(badges)
total_prio = sum(priorities)
print(f'Total priority of all badges = {total_prio}')
    