import random


def add(set_):
    number = 0
    new_set = []
    while number < 7:
        new_piece = random.choice(set_)
        new_set.append(new_piece)
        set_.remove(new_piece)
        number += 1
    return new_set


def snake(array):
    domino_snake = [-1, -1]
    for i in range(7):
        if array[i][0] == array[i][1] and array[i][0] > domino_snake[0]:
            domino_snake = array[i]
    return domino_snake


def status_definition(player_pieces, computer_pieces):
    player_domino = snake(player_pieces)
    computer_domino = snake(computer_pieces)
    if player_domino == [-1, -1] and computer_domino == [-1, -1]:
        return '0'
    else:
        if player_domino[0] > computer_domino[0]:
            return 'computer'
        else:
            return 'player'


def snake_definition(player_pieces, computer_pieces):
    player_domino = snake(player_pieces)
    computer_domino = snake(computer_pieces)
    if player_domino[0] > computer_domino[0]:
        player_pieces.remove(player_domino)
        return player_domino
    else:
        computer_pieces.remove(computer_domino)
        return computer_domino


def printing(stock_pieces, player_pieces, computer_pieces, snake_domino, status):
    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()
    if len(snake_domino) > 6:
        print(snake_domino[0], snake_domino[1], snake_domino[2], "...",
              snake_domino[-3], snake_domino[-2], snake_domino[-1])
    else:
        print(''.join([str(m) for m in snake_domino]))
    print()
    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(str(i + 1) + ":" + str(player_pieces[i]))
    print()
    if status == 'computer':
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")


def the_end(stock_pieces, player_pieces, computer_pieces, snake_domino, status):
    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()
    if len(snake_domino) > 6:
        print(snake_domino[0], snake_domino[1], snake_domino[2], "...",
              snake_domino[-3], snake_domino[-2], snake_domino[-1])
    else:
        print(''.join([str(m) for m in snake_domino]))
    print()
    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(str(i + 1) + ":" + str(player_pieces[i]))
    print()
    print(status)


def check_flag(flag):
    if flag == 1:
        return "Status: The game is over. You won!"
    if flag == -1:
        return "Status: The game is over. The computer won!"
    if flag == 0:
        return "Status: The game is over. It's a draw!"


def make_right(user, snake_domino, domino):
    if user[domino - 1][0] == snake_domino[len(snake_domino) - 1][1]:
        snake_domino.append(user[domino - 1])
        user.pop(domino - 1)
    elif user[domino - 1][1] == snake_domino[len(snake_domino) - 1][1]:
        a = user[domino - 1][0]
        user[domino - 1][0] = user[domino - 1][1]
        user[domino - 1][1] = a
        snake_domino.append(user[domino - 1])
        user.pop(domino - 1)


def check_left(user, snake_domino, domino):
    if user[abs(domino) - 1][1] == snake_domino[0][0]:
        return True
    elif user[abs(domino) - 1][0] == snake_domino[0][0]:
        return True
    else:
        return False


def check_right(user, snake_domino, domino):
    if user[domino - 1][0] == snake_domino[len(snake_domino) - 1][1]:
        return True
    elif user[domino - 1][1] == snake_domino[len(snake_domino) - 1][1]:
        return True
    else:
        return False


def make_left(user, snake_domino, domino):
    if user[abs(domino) - 1][1] == snake_domino[0][0]:
        snake_domino.insert(0, user[abs(domino) - 1])
        user.pop(abs(domino) - 1)
    elif user[abs(domino) - 1][0] == snake_domino[0][0]:
        a = user[abs(domino) - 1][0]
        user[abs(domino) - 1][0] = user[abs(domino) - 1][1]
        user[abs(domino) - 1][1] = a
        snake_domino.insert(0, user[abs(domino) - 1])
        user.pop(abs(domino) - 1)


def new_count(array, elem):
    num = 0
    for i in range(len(array)):
        for j in range(2):
            if array[i][j] == elem:
                num += 1
    return num


def numbers_count(numbers, computer):
    for i in range(len(computer)):
        for j in range(2):
            numbers[computer[i][j]] += 1
    return numbers


def zero_condition(user, stock):
    new_piece = random.choice(stock)
    user.append(new_piece)
    stock.remove(new_piece)


def player_move(stock_pieces, player_pieces, snake_domino):
    domino = 0
    while True:
        try:
            domino = int(input())
            if domino not in range(-len(player_pieces), len(player_pieces) + 1):
                print("Invalid input. Please try again.")
                continue
            elif domino < 0 and check_left(player_pieces, snake_domino, domino) is False:
                print("Illegal move. Please try again.")
                continue
            elif domino > 0 and check_right(player_pieces, snake_domino, domino) is False:
                print("Illegal move. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    if domino < 0:
        make_left(player_pieces, snake_domino, domino)
    elif domino > 0:
        make_right(player_pieces, snake_domino, domino)
    elif domino == 0 and len(stock_pieces) != 0:
        zero_condition(player_pieces, stock_pieces)


def computer_move(stock_pieces, computer_pieces, snake_domino, flag):
    snake_domino_2 = []
    for r in snake_domino:
        for j in r:
            snake_domino_2.append(j)
    computer_pieces_2 = []
    for h in computer_pieces:
        for g in h:
            computer_pieces_2.append(g)
    num_score = {0: snake_domino_2.count(0) + computer_pieces_2.count(0),
                 1: snake_domino_2.count(1) + computer_pieces_2.count(1),
                 2: snake_domino_2.count(2) + computer_pieces_2.count(2),
                 3: snake_domino_2.count(3) + computer_pieces_2.count(3),
                 4: snake_domino_2.count(4) + computer_pieces_2.count(4),
                 5: snake_domino_2.count(5) + computer_pieces_2.count(5),
                 6: snake_domino_2.count(6) + computer_pieces_2.count(6)}
    pieces_score_list = []
    for q in range(0, len(computer_pieces_2), 2):
        pieces_score = num_score[computer_pieces_2[q]] + num_score[computer_pieces_2[q + 1]]
        pieces_score_list.append(pieces_score)
    while True:
        if max(pieces_score_list) == 0:
            flag = 3
            break
        checked_piece_score_index = pieces_score_list.index(max(pieces_score_list)) + 1
        pieces_score_list[checked_piece_score_index - 1] = 0
        if check_left(computer_pieces, snake_domino, checked_piece_score_index) is True:
            make_left(computer_pieces, snake_domino, checked_piece_score_index)
            break
        elif check_right(computer_pieces, snake_domino, checked_piece_score_index) is True:
            make_right(computer_pieces, snake_domino, checked_piece_score_index)
            break
    if flag == 3:
        zero_condition(computer_pieces, stock_pieces)
        flag = -2


def main():
    domino_set = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
                  [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                  [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
                  [3, 3], [3, 4], [3, 5], [3, 6],
                  [4, 4], [4, 5], [4, 6],
                  [5, 5], [5, 6],
                  [6, 6]]
    status = '0'
    flag = -2
    stock_pieces = []
    player_pieces = []
    computer_pieces = []
    snake_domino = []

    while status == '0':
        set_ = domino_set.copy()
        player_pieces = add(set_)
        computer_pieces = add(set_)
        stock_pieces = set_
        status = status_definition(player_pieces, computer_pieces)
    snake_domino.append(snake_definition(player_pieces, computer_pieces))

    while flag == -2:
        if len(computer_pieces) == 0:
            flag = -1
            break
        elif len(player_pieces) == 0:
            flag = 1
            break
        elif snake_domino[0][0] == snake_domino[len(snake_domino) - 1][0]:
            piece = snake_domino[0][0]
            if new_count(snake_domino, piece) == 8:
                flag = 0
                break
        elif len(stock_pieces) == 0:
            flag = 0
            break
        else:
            flag = -2

        if status == 'player':
            printing(stock_pieces, player_pieces, computer_pieces, snake_domino, status)
            player_move(stock_pieces, player_pieces, snake_domino)
            status = 'computer'

        elif status == 'computer':
            printing(stock_pieces, player_pieces, computer_pieces, snake_domino, status)
            input()
            computer_move(stock_pieces, computer_pieces, snake_domino, flag)
            status = 'player'

    status = check_flag(flag)
    the_end(stock_pieces, player_pieces, computer_pieces, snake_domino, status)


if __name__ == '__main__':
    main()
