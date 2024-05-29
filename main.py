import random

QUESTION_FORMAT = "{}/nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["good", "nice", "great"]
BAD_COMMENTS = ["Nah", "Next one", "Nop"]
QUESTIONS = ["What si the capital of NZ?",
            "What is the most common pet in NZ?"
                "What is the highest mountain in NZ?"]
OPTIONS = [["Auckland", "Wellington", "chirstchurch", "Dunedin"],
           ["mouse", "dog", "bird", "cat"],
           ["Mt. Taranaki", "Mt. Eden", "Mt. Aoraki", "Mt. Ruapehu"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWER = [1,3,2]

play = "yes"

#ask name
name = input("What's your name")
input("What's your name?")
print("Welcome to the quiz,", name)
print("This quiz is about capital cities of the world.")

#number of attempets
while True:
    try:
        tries = input("How many attempts do you want for each question? 1-4")
        tries = int(tries)
        break
    except:
        print("That's not a number")

#quiz starts
while play == "yes":
    score = 0
    #loop
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            #ask question
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                  OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            #check answer
            if answer == OPTIONS[i][ANSWER[i]] or answer == SHORT_OPTIONS[ANSWER[i]]:
                print("Correct")
                score += 5
                print(random.choice(GOOD_COMMENTS))
                break
            elif answer == "":
                print("Not sure?")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong!")
                print(random.choice(BAD_COMMENTS))
            else:
                print("That wasn't an option")

            question_attempts -= 1
            print("The answer is Wellington")
    #quiz end
    print("Welldone {}. You finished the quiz . Your final score was {}".format(name, score))

    #replay
    play = input("Do you want to play again?").lower()
