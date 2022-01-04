# Rock paper scissors: Make a two-player Rock-Paper-Scissors game. 

print("Please choose your answer: rock, paper, scissors")
while True:
    item1 = input("Player 1: ")
    item2 = input("Player 2: ")
    points_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player1_points = points_dict.get(item1)
    player2_points = points_dict.get(item2)
    difference = player1_points - player2_points
    if difference == 0:
        print('Game is tied. Please continue.')
        print('')
    elif difference in [-1, 2]:
        print('Player 1 wins!')
        if input("Play another round? Answer yes/no: ") == 'yes':
            continue
        else:
            break
    elif difference in [-2, 1]:
        print('Player 2 wins!')
        if input('Play another round? Answer yes/no: ') == 'yes':
            continue
        else:
            break