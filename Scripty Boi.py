# YO IS BETER HEllo
def reset():
    global board_spaces, whose_turn_is_it,  game_is_still_playing
    board_spaces = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
    whose_turn_is_it = 1
    game_is_still_playing = True


def draw_board():
    """
    draws the board
    :return:
    """
    #Note: in a few of the lines ahead, we are using the notation {0:2d} instead of just {0}. The additional stuff is
    #      formatting info - it says that we want an integer (the "d" - don't ask me why) that is at least two characters
    #      wide. If it is a single digit number, put a space in front of it. This will ensure that our boxes will look
    #      right, whether they hold single or double digit numbers!
    print("") # blank line
    print(" P2  13  12  11  10   9   8  ")
    print("+---+---+---+---+---+---+---+---+")
    print("|   |{0:2d} |{1:2d} |{2:2d} |{3:2d} |{4:2d} |{5:2d} |   |".format(board_spaces[13],board_spaces[12],\
                                                                             board_spaces[11],board_spaces[10],\
                                                                             board_spaces[9],board_spaces[8]))
    print("|{0:2d} +---+---+---+---+---+---+{1:2d} |".format(board_spaces[0],board_spaces[7]))
    print("|   |{0:2d} |{1:2d} |{2:2d} |{3:2d} |{4:2d} |{5:2d} |   |".format(board_spaces[1],board_spaces[2],\
                                                                             board_spaces[3],board_spaces[4],\
                                                                             board_spaces[5],board_spaces[6]))
    print("+---+---+---+---+---+---+---+---+")
    print("      1   2   3   4   5   6  P1")

def p1_ply():
    """
    handles one move for player 1
    :return: whether the player gets to go again.
    """
    good_answer = False
    while not good_answer:
        try:
            which_bin = int(input("Player 1, which bin do you want, 1-6? "))
            if which_bin > 0 and which_bin < 7:
                good_answer = True
            else:
                print("That is not a legal move.")
        except ValueError:
            print("That was not a number. Please try again.")

    # by the time we get here, the variable "which_bin" holds a legal move - which bin the player wants.



    global board_spaces
    #    The player has chosen a legal move - a number stored in the variable "which_bin." Put the number of
    #       chips in this space on the board into a new variable, "num_chips_to_distribute," and then empty this space on
    #       the board.
    num_chips_to_distribute = board_spaces[which_bin]
    board_spaces[which_bin] = 0

    # REPLACE THIS TEMPORARY LINE! If you leave this here, the program won't work.

    drop_location = which_bin  # this is the variable that we will use to drop 1 chip each in several spaces.
    final_bin = num_chips_to_distribute + which_bin
    if final_bin > 13:
        final_bin = final_bin - 14
    while num_chips_to_distribute > 0:
        drop_location = drop_location + 1
        # Increment the drop_location; if we get to 14, reset it to zero.
        # (Hint: you can do the "14 check" with an "if" statement or use a "%" trick.)
        if drop_location >= 14:
            drop_location = 0
        #   If drop_location is not on the opponent's scoring space, add one chip to this board space, and
        #   reduce num_chips_to_distribute by 1.

        if drop_location != 0 :
            board_spaces[drop_location] = board_spaces[drop_location] + 1
            num_chips_to_distribute = num_chips_to_distribute - 1



    # ----- after the while loop....
        # Check whether the drop_location wound up on Player 1's side of the board.
            if drop_location > 0 and drop_location < 7:
                if board_spaces[drop_location] == 1:
                    board_spaces[7] = board_spaces[7] + 1
                    board_spaces[drop_location] = 0
                    opposite_bin = 14-drop_location
                    opposite_bin_amount = board_spaces[opposite_bin]
                    board_spaces[7] = board_spaces[7] + opposite_bin_amount
                    board_spaces[opposite_bin] = 0
    if final_bin == 7:
        return True
    return False

def p2_ply():
    good_answer = False
    while not good_answer:
        try:
            which_bin = int(input("Player 2, which which_bin do you want, 8-13? "))
            if which_bin > 7 and which_bin < 14:
                good_answer = True
            else:
                print("That is not a legal move.")
        except ValueError:
            print("That was not a number. Please try again.")

    global board_spaces

    num_chips_to_distribute = board_spaces[which_bin]
    board_spaces[which_bin] = 0


    drop_location = which_bin
    final_bin = num_chips_to_distribute + which_bin
    if final_bin > 13:
        final_bin = final_bin - 14
    while num_chips_to_distribute > 0:

        drop_location = drop_location + 1

        if drop_location >= 14:
           drop_location = 0

        if drop_location != 7:
            board_spaces[drop_location] = board_spaces[drop_location] + 1
            num_chips_to_distribute = num_chips_to_distribute - 1
            if drop_location > 7 and drop_location < 14:
                if board_spaces[drop_location] == 1:
                    board_spaces[7] = board_spaces[7] + 1
                    board_spaces[drop_location] = 0
                    opposite_bin = 14-drop_location
                    opposite_bin_amount = board_spaces[opposite_bin]
                    board_spaces[7] = board_spaces[7] + opposite_bin_amount
                    board_spaces[opposite_bin] = 0

    if final_bin == 0:
        return True

    return False
def p1_space_counter_machine():
    global board_spaces
    l = 0
    for p in range (1,7):

        l = l + board_spaces[p]
    return l


def p2_space_counter_machine():
    global board_spaces
    o = 0
    for k in range(8, 14):
        o = o + board_spaces[k]
    return o
def check_for_game_over():
    global board_spaces
    """
    checks to see whether all the squares are empty on either side of the board.
    :return: whether the game should end.
    """
    sum_of_p1_spaces = 0
    sum_of_p2_spaces = 0



    sum_of_p1_spaces = p1_space_counter_machine()
    sum_of_p2_spaces = p2_space_counter_machine()



    if sum_of_p1_spaces == 0:
        return True
    if sum_of_p2_spaces == 0:
        return True

    return False # if we got this far, then the game isn't over.

def give_players_pieces_on_their_side_of_the_board():
    global board_spaces
    """
    gives player 1 all the pieces in squares 1-6 and gives player 2 all the pieces in squares 8-13.
    :return: None
    """

    #Note: this is very similar to check_for_game_over() - you can probably steal some code from that and modify.
    sum_of_p1_spaces = 0
    sum_of_p2_spaces = 0


    for b in range(1,6):
        board_spaces[7] = board_spaces[7] + board_spaces[b]

    for k in range(8, 13):
        board_spaces[7] = board_spaces[7] + board_spaces[k]

    for woah in range(1, 13):
        if woah != 7:
            board_spaces[woah] = 0


def loop():
    """
    perform a single ply and check whether the game is over.
    :return: None
    """
    global whose_turn_is_it, game_is_still_playing
    draw_board()
    if whose_turn_is_it == 1:
        go_again = p1_ply()
        if not go_again:
            whose_turn_is_it = 2
    else:
        go_again = p2_ply()
        if not go_again:
            whose_turn_is_it = 1
    game_is_still_playing = not check_for_game_over()


def main():
    """
    Reset the board, run the primary game loop, and handle the post-game summary.
    :return: None
    """
    reset()
    while game_is_still_playing:
        loop()
    draw_board()
    print ("Reallocating pieces.")
    give_players_pieces_on_their_side_of_the_board()
    draw_board()
    print ("Game over.")



# =============================  Game Starts here. =====================================
main()
