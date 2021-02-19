import random
from webscraper import action_trivias

# this program will throw a random bollywood trivia , depending on the user's genre choice


# the user is welcomed to the app


# the user is given a menu to choose the genre from


# depending on the choice , display a random trivia and ask the movie's name
def Action_Movies():
    user_answer = 'Y'
    score = 0
    while user_answer == 'Y':
        # getting a random trivia by converting dictionary into a list, then picking at random
        trivia, movie = random.choice(list(action_trivias.items()))
        print(trivia)


        # asking user to guess the movie n displaying their result
        guess = input("What's your guess? : ")
        guess = guess.upper()
        if guess == movie:
            print("Your guess is correct")
            score += 1
            print("Your current score is: " + str(score) + " points.")

        elif guess != movie:
            score -= 1
            print("Wrong guess. You lost a point")
            print("The movie is: "+ movie)
            print("Your current score is "+ str(score) + " points")

        user_answer = input("Ready for the next one? : ").upper()

    if user_answer == 'N':
        print("Well played. See you next time!!")
        print("Your final score is: "+ str(score) + " points")



# ask the user if they want to keep going in the existing genre, switch, or stop altogether

# display the final score and say goodbye

