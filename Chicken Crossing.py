import random

'''
The goal of this game is to help the chicken cross the road :D 
There are seven lanes on the road with passing cars on each except for
the first and seventh lane. The number of cars on each lane varies per
move and the chicken must avoid them in order to reach the other side.

Not only does the chicken have to avoid the cars but it also has to follow
a pattern to be granted entry to the gates. The pattern (not in particular
order) is to move at least three steps to the right, three steps to left,
two steps upward, and no more nine steps downward.

The chicken must also be careful not to step outside the road or else it dies.
'''

#GLOBAL VAR
size = 7
x = size//2
y = 0
character = "&"
end_game = 0
counter = 0
won = False
moves = []
main_board = []

#FUNCTIONS
def GetBoard(x, y):

    board = []

    for i in range(size):
        
        row = []
        for j in range(size):

            if i == y and j == x:
                row.append(character)
            elif i == 0:
                row.append("=")
            elif i == size-1:
                row.append("#")
            else:
                row.append("_")

        board.append(row)

    return board

def AddCars(road):

    global counter
    
    for lane in road[1:-1]:

        for c in range(counter):

            lane[random.randint(0, size - 1)] = "@"

    return road

def IsValid():

    global x, y, size

    if x < size and x >= 0 and y < size and y >= 0:
        return True
    

def MoveChar(direction):

    global x, y, end_game

    if direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    elif direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    elif direction == "exit":
        end_game = 1
        print("Thanks for playing! :)")
    else:
        print("Invalid move")

def IsAlive(board):
    for b in board:
        for c in b:
            if c == "&":
                return True
            
def ReachedEnd(board):
    for d in board[size-1]:
        if d == "&":
            return True
        
def CompletedMoves(moves):
    if moves.count("right") >= 3 and moves.count("left") >= 3 and moves.count("up") >= 2 and moves.count("down") <= size + 2:
            return True
    
def WelcomeHome():

    global won
    won = True

    welcome = []

    for s in range(size):
        welcome.append("&")

    print(welcome)

#MAIN
while end_game == 0:

    main_board = GetBoard(x, y)

    with_traffic = AddCars(main_board)

    [print(b) for b in with_traffic]

    if ReachedEnd(with_traffic) and CompletedMoves(moves):
        WelcomeHome()
        print("You've crossed the street! :D")
        end_game = 1

    elif ReachedEnd(with_traffic) and not CompletedMoves(moves):
        print("We don't recognize you... :/")

    if IsValid() and IsAlive(with_traffic) and not won:
        move = input("Where to go? ")
        MoveChar(move)
        moves.append(move)

        counter = random.randint(1, 2)

    elif won:
        MoveChar("exit")

    else:
        end_game = 1
        print("You died. :(")