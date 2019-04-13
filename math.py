number1 = int(input("Enter the first factor: "))
number2 = int(input ("Enter the second factor: "))
addFunction = 0
answer = 0

if addFunction < number2:
	while True:
		answer = answer + number1
		addFunction = addFunction + 1
		if addFunction == number2:
			break
print ("The product is", answer)