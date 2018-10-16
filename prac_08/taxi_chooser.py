from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """
Let's drive!
q)uit, c)hoose taxi, d)rive
"""
current_taxi = None


def main():
    print(MENU)
    user_choice = None
    while user_choice != 'q':
        user_choice = input(">>> ").lower()
        if user_choice == 'c':
            choose_taxi()
        if user_choice == 'd':
            drive_taxi()
    if user_choice == 'q':
        print(total_cost)
        print("Taxis are now: {}".format('no u'))


def choose_taxi():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    n = 0
    for taxi in taxis:
        print("{} - {}".format(n, taxi))
    pass


def drive_taxi():
    print("Drive how far? ")

    pass


main()
