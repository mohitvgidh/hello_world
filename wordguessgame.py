import random
import time
import logging
import re
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s -%(levelname)s -%(message)s')
print("welcome to hangman game")
print("the life of michael lies in your hand")
print("guess the correct word and save him")
print("you get 10 guesses")
attempt=10
i=0
j=0
fopen=open("mohit.txt",'r')
words=(fopen.read())
mo1=[]

corword=[]
choice='y'
disword=['*','*','*','*','*','*']

while choice=='y':
	rex=re.compile(r'[a-z]{3,6}')
	mo=rex.findall(str(words))
	random.shuffle(mo)
	selword=random.sample(mo,1)
	selectword=str(selword[0])
	
	print("the game begins play carefully")	
	while j<10:
		print("the word is:",end='')
		for h in disword:
			print(h,end='')
		print("\n")
		print(f"no of attempt remaining:{attempt}")
		print("make a guess")
		
		x=input()
		if x in selectword:
			
			print("great guess")
			for i in range(len(selectword)):
				if x==selectword[i]:
					disword[i]=x
				
							
		
		else:
		
			print("wrong guess")
			attempt=attempt-1
			j=j+1
   
		if "*" not in disword:
			j=11
			flag=1
	if flag==1:
		print("success")
		print(f"correct word is:{selectword}")
	else:
		print("failure")
	
	choice=input("do you want to play again")




	


			