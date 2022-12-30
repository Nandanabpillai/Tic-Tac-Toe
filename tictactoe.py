import mysql.connector,sys,pygame,time
from clrprint import *

def create():
    mydb=mysql.connector.connect(host="localhost",user="root",password="abc",database='xii')
    mycursor=mydb.cursor()
    mycursor.execute('create table tictactoe_scores(player1 varchar(25),player2 varchar(25),rounds_played int,score1 int,score2 int,winner char(25))')

def add():
    mydb=mysql.connector.connect(host="localhost",user="root",password="abc",database='xii')
    mycursor=mydb.cursor()
    l=[t1,t2,r,x,y,s]
    mycursor.execute("insert into tictactoe_scores values(%s,%s,%s,%s,%s,%s)",l)
    mydb.commit()
    sys.exit()
    
def reply():                    
    global board,ch,a,c,r,s
    clrprint('Do you want to replay?',clr='g')
    ch=clrinput('Type yes or no : \n',clr='g')
    if ch.lower() == 'yes':
        r=r+1
        a,c=0,0
        clrprint('Round : ',r)
        board =[
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
    ]
        
        main()
                            
    elif ch.lower() == 'no':
        pygame.mixer.init()
        soundobj=pygame.mixer.Sound('seeya.wav')
        soundobj.play()
        time.sleep(3) #time.sleep is used to ensure that the next line is executed only after the audio has played
        if x > y:
            s = t1
        elif x < y:
            s = t2
        else:
            s = 'Draw'
        add()
    else:
        clrprint('Invalid Input!\nPlease enter yes or no',clr='r')
        reply()


def checking():                 #to check the winning condition
    global x,y
    for i in range(9):
        if board[0][0]!='1' and board[0][1]!='2' and board[0][2]!='3':
            if board[0][0]==board[0][1]==board[0][2]:
                if board[0][0]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                       
        
        if board[1][0]!='4' and board[1][1]!='5' and board[1][2]!='6':
            if board[1][0]==board[1][1] and board[1][1]==board[1][2]:
                if board[1][0]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                        
                
        if board[2][0]!='7' and board[2][1]!='8' and board[2][2]!='9':
            if board[2][0]==board[2][1] and board[2][1]==board[2][2]:
                if board[2][0]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()    
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                        
                
        if board[0][1]!='2' and board[2][1]!='8' and board[1][1]!='5':
            if board[2][1]==board[1][1] and board[2][1]==board[0][1]:
                if board[1][1]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()
                        
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                        
                
        if board[2][2]!='9' and board[1][2]!='6' and board[0][2]!='3':
            if board[2][2]==board[0][2] and board[1][2]==board[2][2]:
                if board[1][2]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()
                        
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                        
                
        if board[2][0]!='7' and board[1][0]!='4' and board[0][0]!='0':
            if board[2][0]==board[1][0] and board[2][0]==board[0][0]:
                if board[1][0]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()
                        
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                        
                
        if board[0][0]!='0' and board[1][1]!='5' and board[2][2]!='9':
            if board[0][0]==board[1][1] and board[0][0]==board[2][2]:
                if board[0][0]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    x=x+1
                    reply()
                        
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()
                        
            
        if board[2][0]!='7' and board[1][1]!='5' and board[0][2]!='3':
            if board[2][0]==board[1][1] and board[1][1]==board[0][2]:
                if board[2][0]==p1.upper():
                    print_board(board)
                    clrprint('Player 1 has won',clr='p')
                    x=x+1
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player1.wav')
                    soundobj.play()
                    time.sleep(2)
                                       
                    reply()
                        
                else:
                    print_board(board)
                    clrprint('Player 2 has won',clr='y')
                    pygame.mixer.init()
                    soundobj=pygame.mixer.Sound('player2.wav')
                    soundobj.play()
                    time.sleep(2)
                    
                    y=y+1
                    reply()

def place_piece(selection, board):
    global c,a
    if board[selection[0]][selection[1]]!='X' and board[selection[0]][selection[1]]!='O' :
        if r%2!=0:
            if c==0:
                board[selection[0]][selection[1]] = "X"
                c=c+1
                a=a+1
            elif c==1:
                board[selection[0]][selection[1]] = 'O'
                c=c-1
                a=a-1
        else:
            if c==1:
                board[selection[0]][selection[1]] = "X"
                c=c-1
                a=a-1
            elif c==0:
                board[selection[0]][selection[1]] = 'O'
                c=c+1
                a=a+1

    else:
        clrprint('Oops! That box is already taken, please select an unoccupied box', clr = 'r') # to prevent overwriting without missing a turn
                        
def convert_selection(selection): # to get the row and coloumn of the selected box
    selection -= 1
    return (selection // 3, selection % 3)
            #row no     #coloumn no

def select_square():
    if a==9:                    #condition for the game to be tied
        clrprint('Out of moves, it is a draw!',clr='r')
        pygame.mixer.init()
        soundobj=pygame.mixer.Sound('draw.wav')
        soundobj.play()
        import time
        time.sleep(4)
        
        reply()
    if r%2!=0:
        if c==0:
            selection = int(clrinput("It's your turn player 1. Move to which place? ",clr='p'))
        elif c==1:
            selection = int(clrinput("It's your turn player 2. Move to which place? ",clr='y'))
    else:
        if c==0:
            selection = int(clrinput("It's your turn player 2. Move to which place? ",clr='y'))
        elif c==1:
            selection = int(clrinput("It's your turn player 1. Move to which place? ",clr='p'))
        
    if not 1 <= selection <= 9:
        raise ValueError
    return selection

def print_board(board):
    for row in board:
        clrprint(row)
    print('\n')


def main():
    while True:
  
        try:
            print_board(board)
            selection = convert_selection(select_square())
            place_piece(selection, board)
            checking()
        except ValueError:
            print('Invalid Input')
            pygame.mixer.init()
            soundobj=pygame.mixer.Sound('number.wav')
            soundobj.play()
            time.sleep(2)

def initialise():
    global p1
    p1=clrinput('\nHey Player 1! Choose X or O : ', clr='p')
    if p1.lower()=='x':
        clrprint("Player 2 : O\n", clr='y')
        main()
    elif p1.lower()=='o':
        clrprint('Player 2 : X\n', clr='y')
        main()
    else:
        clrprint('\nEnter X or O!\n', clr='r')
        initialise()

board =[
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
    ]

x,y,r,a,c=0,0,1,0,0

t1=clrinput('Player 1 : Input your name - ',clr='p')
t2=clrinput('Player 2 : Input your name - ',clr='y')
initialise()