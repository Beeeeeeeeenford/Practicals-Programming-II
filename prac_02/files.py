
name = input("Enter your name")
file = open('name.txt', 'w')
file.write(name)

file = open('name.txt', 'r')
print("Your name is {}".format(name))

new_file = open('numbers.txt', 'r')
print(new_file)
