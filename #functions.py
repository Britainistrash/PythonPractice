guesses = []
BIGGEST_COUNTRIES_ANSWERS =["russia", "canada", "china", "us", "brazil", "australlia", "india", "argentina"]

#functions

def intro():
    #name
    name = input("What's your name?")

    print("Welcome to the quiz,", name)
    print("The quiz is about the ten largest countries in the world")

#ask lives
def getLives():
    while True:
        lives = input("How many chances do you want?")
        try:
            #if the number is okay
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("chose a number")
        except:
            print("That wasn't a nummber")

#if already exists
def inList(answer, list):
    if answer in list:
        return True
    else:
        return False
    
#main code
intro()
lives = getLives()
score = 0

#quiz starts
while lives > 0:
    answer = input("Name one of the top 10 biggest countries in the world:\n").lower()

    #wrong or correct answer
    if inList(answer, BIGGEST_COUNTRIES_ANSWERS):
        #if gueesed or not aready
        if inList(answer, guesses):
            print("You have already guessed that already")
        else:
            print("Correct")
            score += 5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses), score, lives))
    else:
        print("Wrong")
        lives -= 1
        print("You have guessed {}. Your score is {}. You have {} chances reamaing".format(len(guesses),score, lives))

#quiz end
print("GG. Your final score was {}".format(score))