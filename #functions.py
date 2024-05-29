#functions
def intro():
    #name
    name = input("What's your name?")

    print("Welcome to this quiz,", name)
    print("This quiz is about the ten largest countries in the world. Can you name them?")

#main code
def getLives():
    while True:
        lives = input("How many chances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please chose a positive number")
        except:
            print("That wasn't a number")