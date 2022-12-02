#opponent_moves = {'A':0, 'B':1, 'C':2}
#player_moves = {'X':0, 'Y':1, 'Z':2}

opponent_moves = ['A', 'B', 'C']
player_moves = ['X', 'Y', 'Z']

test_input_file = r'C:\repos\personal\adventofcode2022\day2\test_input.txt'
input_file = r'C:\repos\personal\adventofcode2022\day2\input.txt'

def parse_input(path: str):
    with open(input_file) as f:
        lines = f.readlines()
    rounds = []
    for line in lines:
        try:
            opponent_move = line[0]
            player_move = line[2]
        except:
            continue
        
        if opponent_move not in opponent_moves:
            continue
        if player_move not in player_moves:
            continue

        rounds += [(opponent_move, player_move)]
    return rounds

def _get_score(opponent_move, player_move):
    index_o = opponent_moves.index(opponent_move)
    index_p = player_moves.index(player_move)

    score = 1 + index_p

    if index_p == (index_o + 1) % 3: # player wins
        score += 6
    elif index_p == index_o: # draw
        score += 3
    
    return score

def get_score(round):
    return _get_score(round[0], round[1])

def compute_total_score(rounds: list):
    return sum([get_score(round) for round in rounds])

# ---------------------------------------------

def get_player_move(opponent_move, player_outcome):
    index_o = opponent_moves.index(opponent_move)

    match player_outcome:
        case 'X': # lose
            index_p = (index_o - 1) % 3
        case 'Y': # draw
            index_p = index_o
        case 'Z': # win
            index_p = (index_o + 1) % 3
    
    return player_moves[index_p]

def _get_score2(opponent_move, player_outcome):
    player_move = get_player_move(opponent_move, player_outcome)
    return _get_score(opponent_move, player_move)

def get_score2(round: tuple):
    return _get_score2(round[0], round[1]) 

def compute_total_score2(rounds: list):
    return sum([get_score2(round) for round in rounds])

# ---------------------------------------------

rounds = parse_input(path=input_file)

# Part 1
score = compute_total_score(rounds)
print(score)

# Part 2
score = compute_total_score2(rounds)
print(score)

