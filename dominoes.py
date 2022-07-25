import random

def add(set):
    number = 0
    new_set = []
    while number < 7:
        new_piece = random.choice(set)
        new_set.append(new_piece)
        set.remove(new_piece)
        number += 1
    return new_set

def snake(list):
    domino_snake = [-1, -1]
    for i in range(7):
        if list[i][0] == list[i][1] and list[i][0] > domino_snake[0]:
            domino_snake = list[i]
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

def main():
    domino_set = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
                 [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                 [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
                 [3, 3], [3, 4], [3, 5], [3, 6],
                 [4, 4], [4, 5], [4, 6],
                 [5, 5], [5, 6],
                 [6, 6]]
    status = '0'
    snake_domino = []
    while status == '0':
        set = domino_set.copy()
        player_pieces = add(set)
        computer_pieces = add(set)
        stock_pieces = set
        status = status_definition(player_pieces, computer_pieces)
    snake_domino.append(snake_definition(player_pieces, computer_pieces))

    print(stock_pieces)
    print(computer_pieces)
    print(player_pieces)
    print(snake_domino)
    print(status)

if __name__ == '__main__':
    main()