score = 0
name = input ("What's your name")
if name == "human":
    print("That's cool")
else:
    print("Ok idc")

print ("Welcome to the quiz")
print ("This quiz is about the stuff in the universe")

answer = input ("What galaxy are we in?")
if answer == "milky way":
    print("HaCKeR!")
    score -= 5
elif answer == "":
    print("Bruv?")
else:
    print ("Haha noob we're in milky way")

print ("Do not try again :)")

print("Your final score is", score)