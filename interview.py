# my simple interview


# personal questions

print("hey! hello hellooo! just answer these feww questions!")

name = input("What is your name? ")

favourite_game = input("What is your favourite game? ")

favourite_food = input("What is your favourite food? ")

favourite_music = input("What is your favourite type of music? ")

superpower = input("If you could have any superpower, what would it be? ")


# summarize

print()
print("---- Iresults.......loser ----")
print("Your name is", name)
print("Your favourite game is", favourite_game)
print("Your favourite food is", favourite_food)
print("Your favourite music is", favourite_music)
print("Your superpower would be", superpower)


# yes or no questions

score = 0

print()
print("---- quiz time, nerd! ----")

answer1 = input("1. Do you like computer science? ")

if answer1 == "yes":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer2 = input("2. Do you like music? ")

if answer2 == "yes":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer3 = input("3. Is Python a programming language? ")

if answer3 == "yes":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer4 = input("4. Is the Earth a planet? ")

if answer4 == "yes":
    print("Incorrect")
else:
    print("Incorrect!")

answer5 = input("5. Is this test impossible to ace? ")

if answer5 == "yes":
    print("Correct! I dictate reality!")
    score = score + 1
else:
    print("Incorrect! I dictate reailty!")


# final score

print()
print("Your score is", score, "out of 5.")
