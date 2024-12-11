from main import *
from board_helper import *

class Bitboard():

    # Board is a 2d array
    def __init__(self, board):
        self.n = len(board)
        self.num_spaces = self.n ** 2

        # Bit boards
        self.white_board = 0b0
        self.black_board = 0b0
      
        # OR the correct bits to see them
        for i, row in enumerate(board): 
            for j, place in  enumerate(row):
                self.white_board <<= 1
                self.black_board <<= 1
                if place == white:
                    self.white_board |= 0b1
                elif place == black:
                    self.black_board |= 0b1


               
        # Comment out, for debugging purposes
        self.print_board()


    # Print the boards, only for debugging
    def print_board(self):
        # Get the string version of the binary representation
        white_str = str(bin(self.white_board))[2:]
        black_str = str(bin(self.black_board))[2:]

        # Cuts off any preprending 0s because they don't affect the representation 
        # and take up more space, aka 0100 -> 100, so add them here
        while (len(white_str) != self.num_spaces):
            white_str = "0" + white_str

        while (len(black_str) != self.num_spaces):
            black_str = "0" + black_str

        # Print the white bit board 
        print("White Bitboard: ")
        for idx, bit in enumerate(white_str):  
            if idx != 0 and idx % (self.n) == 0:
                print()

            print(bit, " ", end="")
        print()

        print("Black Bitboard: ")
        # Print the black bit board
        for idx, bit in enumerate(black_str):
            if idx != 0 and idx % (self.n) == 0:
                print() 

            print(bit, " ", end="")
        print()


if __name__ == "__main__":
    board_as_arr = make_board(8)
    print(board_as_arr)
    board = Bitboard(board_as_arr)


