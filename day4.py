class BingoGame:

    def __init__(self, lines):
        self.boards = []
        self.numbers = lines[0].split(",")

        board_count = int((len(lines) - 1) / 6)

        for i in range(board_count):
            b = BingoBoard()

            for j in range(5):
                which = i * 6 + 2 + j

                b.spots_numbers.insert(j, lines[which].split())
                b.spots_marked.insert(j, [False] * len(b.spots_numbers[j]))

            self.boards.insert(i, b)

#        self.print_boards()

        self.round = 0

    def last_called_number(self):
        return int(self.numbers[self.round - 1])

    def play_round(self):
        number = self.numbers[self.round]
        print("Playing number {}".format(number))
        self.mark_boards(number)
        self.round += 1

    def print_boards(self):
        for board in self.boards:
            print("Board id {} of total {} boards".format(id(board), len(self.boards)))
            board.print()

    def mark_boards(self, number):
        for board in self.boards:
            board.mark_number(number)

    def check_win(self):
        for board in self.boards:
            if board.check_win():
                return board.sum_unmarked()

        return 0

class BingoBoard:
    spots_numbers = []
    spots_marked = []

    def __init__(self):
        self.spots_numbers = []
        self.spots_marked = []

    def mark_number(self, num):
        for i in range(len(self.spots_numbers)):
            for j in range(len(self.spots_numbers[i])):
                if self.spots_numbers[i][j] == num:
                    self.spots_marked[i][j] = True
                    return True

    def check_win(self):
        winner = False
        for i in range(len(self.spots_marked)):
            if False in self.spots_marked[i]:
                winner = winner | False
            else:
                print("Winner {}".format(self.spots_marked[i]))
                winner = True

        for j in range(len(self.spots_marked[0])):
            col_win = True
            for i in range(len(self.spots_marked)):
                col_win = col_win and self.spots_marked[i][j]

            winner = winner or col_win

        return winner

    def sum_unmarked(self):
        sum = 0
        for i in range(len(self.spots_numbers)):
            for j in range(len(self.spots_numbers[i])):
                if self.spots_marked[i][j] == False:
                    sum += int(self.spots_numbers[i][j])
        return sum

    def print(self):
        if len(self.spots_numbers) == 0:
            print("Bingo board is empty")
            return

        for i in range(len(self.spots_numbers)):
            print("line {}:".format(i), end = "")
            for j in range(len(self.spots_numbers[i])):
                if self.spots_marked[i][j] == True:
                    print("[{}]".format(self.spots_numbers[i][j]), end=" ")
                else:
                    print("{}".format(self.spots_numbers[i][j]), end=" ")
            print("")

def read_game(lines):
    game = BingoGame(lines)

    return game

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    game = read_game(input_lines)
    for i in range(len(game.numbers)):
        game.play_round()
        if game.check_win() > 0:
            score = game.check_win() * game.last_called_number()
            game.print_boards()
            print("Game won in {} rounds - score {}".format(i,score))
            break


    return str(score)
