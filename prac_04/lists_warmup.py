numbers = [3, 1, 4, 1, 5, 9, 2]

'''
numbers[0] is 3
numbers[-1] is 2
numbers[3] is 1
numbers[:-1] is [3, 1, 4, 1, 5, 9]
numbers[3:4] is [1]
5 in numbers is [4]
7 in numbers is [0]
"3" in numbers is [0]
numbers + [6, 5, 3] is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''

#Question 1
numbers[0] = 10
#Question 2
numbers[-1] = 1
#Question 3
numbers[2:]
#Question 4
if 9 in numbers:
    print('9 is in the list')
else:
    print('9 is not in the list')

print(numbers)
