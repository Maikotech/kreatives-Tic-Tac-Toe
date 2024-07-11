#!/usr/bin/python3
import time
import board
import neopixel
pixel_pin = board.D18
num_pixels = 256
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

COLOR_X = (255, 0, 0)
COLOR_O = (0, 0, 255)
COLOR_EMPTY = (0, 0, 0)

board_state = [' '] * 9

mapping = [
    33, 34, 35,
    30, 29, 28,
    1, 2, 3
    ]
def display_board():
    pixels.fill(COLOR_EMPTY)
    for i in range(9):
        if board_state[i] == 'X':
            pixels[mapping[i]] = COLOR_X
        elif board_state[i] == 'O':
            pixels[mapping[i]] = COLOR_O
    pixels.show()
    
def check_winner(board, player):
    win_condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_condition:
        if all(board[i] == player for i in condition):
            return true
        return False
def is_draw(board):
    return all(cell != ' ' for cell in board)

def main():
    current_player = 'X'
    while True:
        display_board()
        try :
            move = int(input(f"PLayer {current_player}, enter your move (0-8): "))
            if board_state[move] == ' ':
                board_state[move] = current_player
                if check_winner(board_state, current_player):
                    display_board()
                    print(f"PLayer {current_player} wins!")
                    break
                elif is_draw(board_state):
                    display_board()
                    print("It's a draw!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("INvalid move, blabla")
        except (ValueError, IndexError):
            print("Invalid move, blabla")
                
    time.sleep(5)
    pixels.fill(COLOR_EMPTY)
    pixels.show()
    
if __name__ == "__main__":
    main()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    
    
    