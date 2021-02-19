from bollywood_trivia import Action_Movies
import random
def main_menu():

    print("\n Action(A) \n Drama(B) \n Comedy(C) \n Romance(D)\n ")
    user_choice = input("Please choose one of the above: ")
    user_choice = user_choice.upper()
    if user_choice == 'A':
        print("You chose: Action")
        Action_Movies()

    elif user_choice == 'B':
        print("You chose: Drama")
    elif user_choice == 'C':
        print("You chose: Comedy")
    elif user_choice == 'D':
        print("You chose: Romance")
    else:
        print("Invalid choice.")

main_menu()


