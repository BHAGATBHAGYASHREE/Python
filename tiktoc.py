
print("----------------------------------------Tic-Tac-Toe---------------------------------------------------")
board = [['1', '2','3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
b = [[' ', ' ',' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]        
def print_b():
    for row in b:
        print(" | ".join(row))
        print("-" * 9)       
print_b()

# Example usage:
print_board()
print("-------------------------------------------------------------------------------------------------------")
