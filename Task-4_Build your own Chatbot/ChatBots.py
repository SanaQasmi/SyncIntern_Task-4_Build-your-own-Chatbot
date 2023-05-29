import random
import time


def greet():
    greetings = ["\033[1;36mChatBot: Hello! I'm your travel assistant.\033[0m"]
    greeting = random.choice(greetings)
    print(greeting)
    time.sleep(2)


def ask_name():
    print("\033[1;31mChatBot: What's your name?\033[0m")
    name = input("User: ")
    time.sleep(1)
    print("\033[1;36mChatBot: Welcome! Nice to meet you.\033[0m, " + name + "!")
    time.sleep(2)


def ask_destination():
    print("\033[1;31mChatBot: Where would you like to travel?\033[0m")
    destination = input("User: ")
    time.sleep(1)
    print("\033[1;36mChatBot: Wow! Great Choice! " + destination + " Is A Beautiful Place.\033[0m")
    time.sleep(2)


def ask_dates():
    print("\033[1;31mChatBot: What is Your Preferred Travel Dates?\033[0m")
    dates = input("User: ")
    time.sleep(1)
    print("\033[1;36mChatBot: Okay, Your Travel Dates Are\033[0m " + dates + ".")
    time.sleep(2)


def ask_help():
    print("\033[1;31mChatBot: Is There Anything Else I Can Help You With?\033[0m")
    help_needed = input("User: ").lower()
    if help_needed == "yes":
        return True
    else:
        return False


def main():
    greet()
    ask_name()
    ask_destination()
    ask_dates()
    while ask_help():
        ask_destination()
        ask_dates()
    print("\033[1;36mChatBot: Okay, Have A Great Trip!\033[0m")


if __name__ == "__main__":
    main()

#Python3 Building_ChatBot_Sana_Qasmi