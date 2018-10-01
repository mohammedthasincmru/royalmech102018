import random

a={1:'r',2:'p',3:'s'}

while True:
	p=input("your choice r/p/s: ")

	c=a[random.randint(1,3)]

	print("you chose:",p,"computer chose:",c)

	if(p==c):
		print("draw")
	elif(p=="r"):
		if(c=="p"):
			print("computer wins")
	elif(p=="p"):
		if(c=="s"):
			print("computer wins")
	elif(p=="s"):
		if(c=="r"):
			print("computer wins")
	elif(c=="r"):
		if(p=="p"):
			print("you win")
	elif(c=="p"):
		if(p=="s"):
			print("you win")
	elif(c=="s"):
		if(p=="r"):
			print("you win")

