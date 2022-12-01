input_file = r'S:\Dokument\Programmering\Github\alexandersb98\adventofcode2022\day1\input.txt'

def get_input_string(path: str):
    with open(path) as f:
        return f.read()

def parse_input_file(path: str):
    input_string: str = get_input_string(path)
    lines = input_string.splitlines()
    
    calories = list()
    index = 0
    for line in lines:
        if line.isdigit():
            value = int(line)
            if len(calories) == index:
                calories.append(value)
            else:
                calories[index] += value
        else: # if line is ''
            index += 1

    return calories

calories = parse_input_file(path=input_file)
print(f"Largest number of calories = {max(calories)}")
sorted_cals = sorted(calories, reverse=True)
top3_calories_count = sum(sorted_cals[:3])
print(f"Total calories carried by top 3 = {top3_calories_count}")