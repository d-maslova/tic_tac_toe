def place_mark(player):
    grid = f"\n_{matrix[0]}_|_{matrix[1]}_|_{matrix[2]}_\n" \
           f"_{matrix[3]}_|_{matrix[4]}_|_{matrix[5]}_\n" \
           f"_{matrix[6]}_|_{matrix[7]}_|_{matrix[8]}_\n"
    return print(grid)


def check_result(player):
    wins = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [7, 5, 3]
    ]
    for win in wins:
        result = all(turn in player for turn in win)
        if result:
            return True


game_on = False
field = "_1_|_2_|_3_\n_4_|_5_|_6_\n_7_|_8_|_9_\n"
start = input("Would you like to play tic tac toe? type y/n\n").lower()
p1 = []
p2 = []

if start == "y":
    game_on = True
    matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Welcome to tic tac toe. Player 1 will start.\n")
    print(field)
    while game_on:
        p1_turn = int(input(f"Player 1, choose a number between 1 and 9\n"))
        matrix[p1_turn - 1] = "X"
        p1.append(p1_turn)
        place_mark(matrix)

        if check_result(p1):
            print("Player 1 wins")
            game_on = False

        p2_turn = int(input(f"Player 2, choose a number between 1 and 9\n"))
        matrix[p2_turn - 1] = "0"
        p2.append(p2_turn)
        place_mark(matrix)

        if check_result(p2):
            print("Player 2 wins")
            game_on = False
    else:
        print("Game over")

