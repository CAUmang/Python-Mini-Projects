print("Welcome to the finance quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does EBITDA stands for? ")
if answer.lower() == "earnings before interest tax depreciation and amortisation":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("What does NP stands for? ")
if answer.lower() == "net profit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    
answer = input("What does EBIT stands for? ")
if answer.lower() == "earnings before interest and tax":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("What does GP stands for? ")
if answer.lower() == "gross profit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/4)*100) + "%." )
