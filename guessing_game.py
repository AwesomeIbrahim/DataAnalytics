import random
randomized_number = random.randint(1,100)
print(randomized_number)
while (randomized_number != guess):
    guess2 = input("Enter a number between 1 and 100")
    guess = int(guess2)
    print ("Wrong guess dearie")
    break
    #elif:
    #print ("Guess was correct. You are an hero")
    #break

