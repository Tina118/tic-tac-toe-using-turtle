import turtle
turtle.title("Tic Tac Toe")
turtle.bgcolor("black")

def draw_board():
	turtle.pen(fillcolor="red", pencolor="white", pensize=5)
	turtle.forward(-300)
	turtle.backward(-300)
	turtle.forward(300)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(600)
	turtle.left(90)
	turtle.forward(400)
	turtle.left(90)
	turtle.forward(600)
	turtle.left(90)
	turtle.forward(600)
	turtle.left(90)
	turtle.forward(600)
	turtle.left(90)
	turtle.forward(200)
	turtle.backward(200)
	turtle.left(90)
	turtle.forward(200)
	turtle.right(90)
	turtle.forward(600)
	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(600)
	
def draw_x(x,y):
	turtle.pen(fillcolor="red", pencolor="white", pensize=10)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.left(0)
	turtle.right(45)
	turtle.forward(100)
	turtle.backward(200)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.backward(200)
	turtle.right(45)

def draw_circle(x,y):
	turtle.pen(fillcolor="red", pencolor="white", pensize=10)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.circle(50)
	#turtle.penup()
	
def horizontal_line(x,y):
	turtle.pen(fillcolor="red", pencolor="red", pensize=10)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.left(0)
	turtle.right(90)
	turtle.forward(550)
	turtle.backward(550)
	turtle.right(100)
	
def vertical_line(x,y):
	turtle.pen(fillcolor="red", pencolor="red", pensize=10)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.left(0)
	turtle.right(180)
	turtle.forward(550)
	turtle.left(0)
	
def left_line(x,y):
	turtle.pen(fillcolor="red", pencolor="red", pensize=10)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.left(0)
	turtle.right(135)
	turtle.forward(750)

def right_line(x,y):
	turtle.pen(fillcolor="red", pencolor="red", pensize=10)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.left(0)
	turtle.left(135)
	turtle.forward(750)


draw_board()


def drawing(position,shape):
	if position==1 and shape=="x": draw_x(-200,300)
	elif position==2 and shape=="x": draw_x(0,300)
	elif position==3 and shape=="x": draw_x(200,300)
	elif position==4 and shape=="x": draw_x(-200,100)
	elif position==5 and shape=="x": draw_x(0,100)
	elif position==6 and shape=="x": draw_x(200,100)
	elif position==7 and shape=="x": draw_x(-200,-100)
	elif position==8 and shape=="x": draw_x(0,-100)
	elif position==9 and shape=="x": draw_x(200,-100)

	elif position==1 and shape=="o":draw_circle(-150,300)
	elif position==2 and shape=="o":draw_circle(50,300)
	elif position==3 and shape=="o":draw_circle(250,300)
	elif position==4 and shape=="o":draw_circle(-150,100)
	elif position==5 and shape=="o":draw_circle(50,100)
	elif position==6 and shape=="o":draw_circle(250,100)
	elif position==7 and shape=="o":draw_circle(-150,-100)
	elif position==8 and shape=="o":draw_circle(50,-100)
	elif position==9 and shape=="o":draw_circle(250,-100)



player1=0
player2=0
shape1=""
shape2=""
p1=[]
board=[2]*9
while(True):
	shape1=input("Enter the option for player1: X or O:").lower()
	if shape1=="x" or shape1=="o":
		if shape1=="o":
			shape2="x"
		else:
			shape2="o"
		break
		
	else:
		print("Please enter valid value")
print("Player 1 will be ",shape1)
print("Player 2 will be ",shape2)
count=0
flag=0
while(True):
	def counting(count):
		if count>=5 and count<=9:
			if (board[0]==0 and board[1]==0 and board[2]==0):
				horizontal_line(-270,300)
				return(True)
			elif (board[3]==0 and board[4]==0 and board[5]==0):
				horizontal_line(-270,100)
				return(True)
			elif(board[6]==0 and board[7]==0 and board[8]==0):
				horizontal_line(-270,-100)
				return(True)
			elif (board[0]==1 and board[1]==1 and board[2]==1): 
				horizontal_line(-270,300)
				return(True)
			elif (board[3]==1 and board[4]==1 and board[5]==1) :
				horizontal_line(-270,100)
				return(True)
			elif (board[6]==1 and board[7]==1 and board[8]==1):
				horizontal_line(-270,-100)
				return(True)
			elif (board[0]==0 and board[4]==0 and board[8]==0) : 
				left_line(-270,370)
				return(True)
			elif (board[2]==0 and board[4]==0 and board[6]==0):
				right_line(270,370)
				return(True)
			elif (board[0]==1 and board[4]==1 and board[8]==1):  
				left_line(-270,370)
				return(True)
			elif (board[2]==1 and board[4]==1 and board[6]==1):
				right_line(270,370)
				return(True)
			elif (board[0]==0 and board[3]==0 and board[6]==0):
				vertical_line(-200,370) 
				return(True)
			elif  (board[1]==0 and board[4]==0 and board[7]==0):
				vertical_line(0,370) 
				return(True)
			elif (board[2]==0 and board[5]==0 and board[8]==0):
				vertical_line(200,370) 
				return(True)
			elif (board[0]==1 and board[3]==1 and board[6]==1):
				vertical_line(-200,370)    
				return(True)
			elif (board[1]==1 and board[4]==1 and board[7]==1):
				vertical_line(0,370) 
				return(True)
			elif (board[2]==1 and board[5]==1 and board[8]==1):
				vertical_line(-200,370) 
				return(True)
		return(False)
	while(True):
		player1=int(input("Enter the position player 1:"))
		if player1 in range(1,10) and player1 not in p1:
			p1.append(player1)
			board[player1-1]=0
			count+=1
			drawing(player1,shape1)
			if counting(count):
				print("Player 1 wins")
				turtle.pen(fillcolor="red", pencolor="yellow", pensize=10)
				turtle.penup()
				turtle.goto(0,-300)
				turtle.pendown()
				turtle.write("Player 1 wins", move=False, align="center", font=("Arial", 40, "normal"))
				flag=1
			break
		else:
			print("Enter a value number or The number you entered is already taken")
	
	
	
	if flag==1:
		break
			
	while(True):
		player2=int(input("Enter the position player 2:"))
		if player2 in range(1,10) and player2 not in p1:
			p1.append(player2)
			board[player2-1]=1
			count+=1
			drawing(player2,shape2)
			if counting(count):
				flag=1
				print("Player 2 wins")
				turtle.pen(fillcolor="red", pencolor="yellow", pensize=10)
				turtle.penup()
				turtle.goto(0,-300)
				turtle.pendown()
				turtle.write("Player 2 wins", move=False, align="center", font=("Arial", 40, "normal"))
			break
		else:
			print("Enter a value number or The number you entered is already taken")
			
	if flag==1:
		break
	
	if count==9:
		print("It's a tie")
		break
	
	print(p1)
	print(board)	
	
turtle.mainloop()
