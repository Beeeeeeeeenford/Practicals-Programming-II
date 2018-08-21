import random

numbers_line = 6
min_number = 1
max_number = 45


def main():
    picks = int(input("How many quick picks?"))
    while picks < 0:
        print("You need to enter some quick picks!")
        picks = int(input("How many quick picks?"))
    for n in range(picks):
        quick_pick = []
        for i in range(numbers_line):
            number = random.randint(min_number, max_number)
            while number in quick_pick:
                number = random.randint(min_number, max_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
