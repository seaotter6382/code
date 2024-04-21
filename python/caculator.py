import time
import random

while True:
    print('welcome to the real python caculator!')
    time.sleep(0.5)
    print('select a option below!')
    time.sleep(0.5)
    print('add (1)')
    time.sleep(0.1)
    print('subtract (2)')
    time.sleep(0.1)
    print('multiply (3)')
    time.sleep(0.1)
    print('divide (4)')
    time.sleep(0.1)
    word = input()
	if word == "1":
		print('enter your first number')
		word1 = input()
		print('enter your second number')
		word2 = input()
		result = int(word1) + int(word2)
		print('the sum of ' + str(word1) + ' and ' + str(word2) + ' is ' + str(result))
		break
	if word == "2":
		print('enter your first number')
		word1 = input()
		print('enter your second number')
		word2 = input()
		result = int(word1) - int(word2)
		print('the diffrence of ' + str(word1) + ' and ' + str(word2) + ' is ' +  str(result))
        break
	if word == "3":
		print('enter your first number')
		word1 = input()
		print('enter your second number')
		word2 = input()
        result = int(word1) * int(word2)
        print('the product of ' + str(word1) + ' and ' + str(word2) + ' is ' + str(result))
        break
    if word == "4":
        print('enter your first number')
        word1 = input()
        print('enter your second number')
        word2 = input()
        result = int(word1) / int(word2)
        print('the quotient of ' str(word1) + ' and ' str(word2) + ' is ' + str(result))
        break
    
        
