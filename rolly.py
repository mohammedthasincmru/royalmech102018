import random
a = True
while a:
	print("you rolled",random.randint(1,6))
	print("do you want to roll again? yes/no")
	a="yes" in input()
