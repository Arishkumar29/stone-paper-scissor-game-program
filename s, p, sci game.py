print('\t\t°°°°°Stone Paper Scissor°°°°°')
print('\t1.stone \n\t2.paper \n\t3.scissor \n\tTotal ten chances, you play the game, who are take high sorce.They are win the match.....')
import random
list = [ 'stone','paper','scissor']
chancepoint=10
CP=0
HP=0
s=0
chance=0
while chance<chancepoint:
	a=random.choice(list)
	b=input('\nchoose(stone/paper/scissor) : ')
	import time
	import sys
	print("Loading:")
	animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
	for i in range(len(animation)):
	   time.sleep(.2)
	   sys.stdout.write("\r" + animation[i % len(animation)])
	   sys.stdout.flush()
	print("\n")
	if a==b:
		print('\n\t\tBoth are same')
		print('\nYour point is :',HP,'\t\tComputer point is :',CP)
		print('\n\t\tTie point')
	elif a=='stone' and b=='paper':
		print('\nopponent Answer is : ',a,'\n\nyour answer is : ',b)
		CP=CP+1
		print('\nYour point is : ',HP, '\t\tComputer point is : ',CP)
		print('\n\t\tyou win')	
		
	elif a=='scissor' and b=='paper':
		print('\nopponent Answer is : ',a,'\n\nyour answer is : ',b)
		CP=CP+1
		print('\nYour point is : ',HP, '\t\tComputer point is : ',CP)
		print('\n\t\tcomputer win')
		
	elif a=='paper' and b=='scissor':
		print('\nopponent Answer is : ',a,'\n\nyour answer is : ',b)
		HP=HP+1
		print('\nYour point is : ',HP, '\t\tComputer point is : ',CP)
		print('\b\t\tyou win')	
		
	elif a=='scissor' and b=='paper':
		print('\nopponent Answer is : ',a,'\n\nyour answer is : ',b)
		CP=CP+1
		print('\nYour point is : ',HP, '\t\tComputer point is : ',CP)
		print('\n\t\tcomputer win')	
		
	elif a=='stone' and b=='scissor':
		print('\nopponent Answer is : ',a,'\n\nyour answer is : ',b)
		CP=CP+1
		print('\nYour point is : ',HP, '\t\tComputer point is : ',CP)
		print('\n\t\tcomputer win')	
			
	elif a=='scissor' and b=='stone':
		print('\nopponent Answer is : ',a,'\n\nyour answer is : ',b)
		HP=HP+1
		print('\nYour point is : ',HP, '\t\tComputer point is : ',CP)
		print('\n\t\tyou win')
	else:
		print('Wrong Value')
		
	chance=chance+1
	s=chancepoint-chance
	print('\nRemaining Chance Is :',s)
print('\t\t\tGame Over')	
if HP==CP:
		print('\n\tMatch is Tie')
elif HP>CP:
		print('\n\tYou is win the Game')
else:
		print('\n\tComputer win the Match')	

