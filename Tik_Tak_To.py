
one, two, three, four, five, six, seven, eight, nine= ('', '', '', '', '', '', '', '', '')

print('\n')

print("Welcome to Tik Tak To game!")
print("Are you ready to play? If yes type \'Y\' to play else type \'Q\' to quit.")

agreement = input('>> ')


while True:

    if agreement.lower()=='y':
        break

    elif agreement.lower()=='q':
        print("Game over!")
        break

    else:
        print('Please input a correct key!')
        agreement = input(">> ")


print('\n')


if agreement.lower()=='y':

    print("Player 1: What do you want to chose \'X\' or \'O\'?")
    first_player = input('>> ')
    first_player = first_player.upper()


    while True:

        if first_player.lower()=='x':
            second_player = 'O'
            break

        elif first_player.lower()=='o':
            second_player = 'X'
            break

        else:
            print('Please input a correct value \'X\' or \'O\'!')
            first_playert = input(">> ")
            first_player = first_player.upper()


    print('\n')

    print("{0:^3}|{1:^3}|{2:^3}".format(seven, eight, nine))
    print('------------')
    print("{0:^3}|{1:^3}|{2:^3}".format(four, five, six))
    print('------------')
    print("{0:^3}|{1:^3}|{2:^3}".format(one, two, three))

    print('\n')

    print("Start the game.")

    print('\n')

    print("1st Player key: " + first_player)
    print("2nd Player key: " + second_player)

    print('\n')

    score_set = []
    value_list = [[one, two, three], [four, five, six], [seven, eight, nine], [one, four, seven], [two, five, eight], [three, six, nine], [one, five, nine], [three, five, seven]]
    count = 1
    gameover = True
    move = 0

    while gameover:

        if count == 1:
            player_value = first_player.upper()
            print('Player' + str(count) + ': In which box you want to place \"' + player_value + "\" (1-9)?")
            turn = input('>> ')
            turn = int(turn)
            count += 1
            move += 1

        else:
            player_value = second_player.upper()
            print('Player' + str(count) + ': In which box you want to place \"' + player_value + "\" (1-9)?")
            turn = input('>> ')
            turn = int(turn)
            count -= 1
            move += 1

        loop = True

        while loop:

            if turn not in score_set and turn in range(1, 10):

                score_set.append(turn)
                if turn == 1:
                    one = player_value
                elif turn == 2:
                    two = player_value
                elif turn == 3:
                    three = player_value
                elif turn == 4:
                    four = player_value
                elif turn == 5:
                    five = player_value
                elif turn == 6:
                    six = player_value
                elif turn == 7:
                    seven = player_value
                elif turn == 8:
                    eight = player_value
                elif turn == 9:
                    nine = player_value
                else:
                    pass

                print('\n')

                print("{0:^3}|{1:^3}|{2:^3}".format(seven, eight, nine))
                print('------------')
                print("{0:^3}|{1:^3}|{2:^3}".format(four, five, six))
                print('------------')
                print("{0:^3}|{1:^3}|{2:^3}".format(one, two, three))

                print('\n')

                value_list = [[one, two, three], [four, five, six], [seven, eight, nine], [one, four, seven], [two, five, eight], [three, six, nine], [one, five, nine], [three, five, seven]]
                loop = False

            else:

                print('Please input a correct box value (1-9) and that hasn\'t been used before!')
                turn = input(">> ")
                turn = int(turn)


        for i in value_list:

            if i[0]=='X' and i[1]=='X' and i[2]=='X':

                if first_player.upper() == 'X':

                    print('\n')
                    print("Player 1: Won the game!")
                    gameover = False

                elif second_player.upper() == 'X':

                    print('\n')
                    print("Player 2: Won the game!")
                    gameover = False

                else:

                    pass

            if i[0]=='O' and i[1]=='O' and i[2]=='O':

                if first_player.upper() == 'O':

                    print('\n')
                    print("Player 1: Won the game!")
                    gameover = False

                elif second_player.upper() == 'O':

                    print('\n')
                    print("Player 2: Won the game!")
                    gameover = False

                else:

                    pass

            else:

                pass

        if move == 9 and gameover == True:

            print("No one has won! Match Draw!")
            break

        else:

            pass
