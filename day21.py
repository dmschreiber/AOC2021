import re


def part1(input):
    player_start = load_input(input)

    player_score = [0,0]
    player_pos = [player_start[0],player_start[1]]

    turn = 0
    roll_number = 0
    total_roll_number = 0
    while max(player_score) < 1000:
        combo_roll = (roll_number % 100) + 1 + (roll_number+1) % 100 + 1 + (roll_number+2) % 100 + 1
        player_pos[turn] = (player_pos[turn] + combo_roll) % 10
        player_score[turn] += player_pos[turn]+1

        # print("Player {} rolls {}+{}+{} and moves to space {} for a total score of {}".format(turn+1,(roll_number % 100) + 1, (roll_number+1) % 100 + 1, (roll_number+2) % 100 + 1,player_pos[turn]+1,player_score[turn]))
        turn = (turn + 1) % 2
        roll_number = (roll_number + 3) % 100
        total_roll_number += 3

    loser = min(player_score)
    return str(loser*total_roll_number)


def load_input(input):
    with open(input) as f:
        input_lines = f.read().splitlines()
    pattern_text = r'^Player (?P<player>\d) starting position: (?P<position>\d+)$'
    pattern = re.compile(pattern_text)
    match = pattern.match(input_lines[0])
    player_start = []
    for i in input_lines:
        match = pattern.match(i)
        if match:
            player = int(match.group('player')) - 1
            position = int(match.group('position')) - 1
            player_start.append(position)
        else:
            print("error {} doesnt' match".format(i))
    return player_start


r_tally = {}

def all_rolls():
    global r_tally
    if len(r_tally) == 0:
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,4):
                    if i+j+k in r_tally:
                        r_tally[i+j+k] += 1
                    else:
                        r_tally[i+j+k] = 1
        return r_tally.items()

    else:
        return r_tally.items()


def play(player_score, player_pos, turn):

    if player_score[0] >= 21:
        return [1, 0]
    elif player_score[1] >= 21:
        return [0, 1]

    wins = [0,0]
    for r, r_count in all_rolls():
        child_score = player_score.copy()
        child_pos = player_pos.copy()
        child_pos[turn] = (child_pos[turn] + r) % 10
        child_score[turn] += child_pos[turn] + 1

        result = play(child_score, child_pos, (turn + 1) % 2)
        wins = [wins[0] + result[0] * r_count, wins[1] + result[1] * r_count]

    return wins

def part2(input):
    player_start = load_input(input)

    player_score = [0,0]
    player_pos = [player_start[0],player_start[1]]
    turn = 0

    won = play(player_score, player_pos, turn)
    i = 0
    print(won)

    return str(max(won))


