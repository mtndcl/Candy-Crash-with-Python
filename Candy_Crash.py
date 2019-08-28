
import sys


matrix = []


target=""
user1=0
user2=0

def readfile(file):
	r=0
	for line in file.readlines():
		line = line.split(" ")
		
		line[-1] = line[-1].strip()
		c=len(line)
		r=r+1
		matrix.append(line)
	
	return 	r,c

def printmatrix():
	for i in range(len(matrix)):
		for a in range(len(matrix[i])):
			
			if(matrix[i][a]=="n"):
				print(" ",end=" ")
			else:
				print(matrix[i][a],end=" ")
		print()
	

	


	
		
def settarget(input):
	target=matrix[input[0]][input[1]]
	print(target)
def findsamesugar(r,c,target,row,colon):
	
	
	global gameover
	matrix[r][c]="n"
	count=0
	if(r+1<row):
		if(target==matrix[r+1][c]):
			
		
			
			findsamesugar(r+1,c,target,row,colon)
		
	if( c+1<colon):		
		if(target==matrix[r][c+1]):
			
			
			findsamesugar(r,c+1,target,row,colon)
	if(r>=0):
		if(target==matrix[r-1][c]  ):
			
			
			findsamesugar(r-1,c,target,row,colon)
	if(c>=0):		
		if(target==matrix[r][c-1]  ):
			
			
			findsamesugar(r,c-1,target,row,colon)
	
def clear(row,colon):
	
	for a in range(colon):
		for i in range(row):
			
			if(matrix[i][a]=="n"):
				for t in range(i,-1,-1):
					
					matrix[t][a]=matrix[t-1][a]
					if(t==0):
						matrix[0][a]="n"
					
def fibbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)
		

def deletefullgap(row,colon):
	for a in range(colon):
	
		empty=True
		for i in range(row):
			
			if(matrix[i][a]!="n"):
				empty=False
		if(empty):
			for x in range(row):
				for t in range(a,colon,1):
					if(t==colon-1):
						matrix[x][t]="n"
					else:			
						matrix[x][t]=matrix[x][t+1]
def destroyed():
	total=0
	for line in matrix:
		for i in line:
			if(i=="n"):
				total=total+1
	
	return total
	
def checkgame(row ,colon):

	over=True
	for i in range(row):
		for a in range(colon):
			if(matrix[i][a]!="n"):
				if(a+1<colon):
					if(matrix[i][a]==matrix[i][a+1] ):
						over=False
				if(i+1<row):
					if(matrix[i][a]==matrix[i+1][a] ):
						over=False
					
				if(a>0):
					if(matrix[i][a]==matrix[i][a-1] ):
						over=False
				if(i>0):
					if(matrix[i][a]==matrix[i-1][a] ):
						over=False
	
	return over		
				
sizes=readfile(file=open(sys.argv[1],"r"))
row=sizes[0]
colon=sizes[1]


print()
printmatrix()

print("\n Your Score is: 0\n")
score=0
have=0	

while(True):

	user_input = input ("Please enter a colon and column number: ")
	print()
	try:
		user_input = user_input.split(" ")
		user_input[-1] = user_input[-1].strip()
		#print("\n Ydewe: {}   {}\n".format(colon,column))
		user1= int(user_input[0])-1
		user2=int(user_input[1])-1
		error=False
		try:
			selectednumber=int(matrix[user1][user2])
		
		except:
			error=True
			print("Please enter a correct size!")
			print()
		
		
		if(error==False):
		
			
			findsamesugar(user1,user2,matrix[user1][user2],row,colon)
			
			
			
			
			total=destroyed()
			
			current=total-have
			score+=fibbo(current)*selectednumber
		
			have=total;
			
			clear(row,colon)
			
			deletefullgap(row,colon)
			printmatrix()
			
			
			print("\n Your Score is: {}\n".format(score))
			
			if(checkgame(row,colon)):
				print("Game Over")
				break
				
	except ValueError:
		print("No.. input string is not an Integer. It's a string")

	



#printmatrix()