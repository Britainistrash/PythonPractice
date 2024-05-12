QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
score = 0
name = input ("What's your name")
if name == "human":
    print("That's cool")
else:
    print("Ok idc")

print ("Welcome to the quiz")
print ("This quiz is about the stuff in the universe")

question = "What galaxy are we in?"
a = "1"
b = "2"
c = "3"
d = "milky way"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
if answer == d or answer == "d".lower():
    print("HaCKeR!")
    score -= 5
elif answer == "":
    print("Bruv?")
else:
    print ("Haha noob we're in milky way")

print ("Do not try again :)")

print("Game bugged {}. You lost. Your score was {}".format(name, score))
