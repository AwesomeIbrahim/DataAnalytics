#!/usr/bin/env python
# coding: utf-8

# In[11]:


def stats(*variables):
    """This function cleans an input and sort the numbers in an ascending order.
    It also computes the mean as well as the median"""
    mytemplist = []
    for eachvariable in variables:
        if isinstance(eachvariable,(int,float)):
            mytemplist.append(eachvariable)
        else:
            pass
    mytemplist.sort()
    lengthofarray = len(mytemplist)
    isum = 0
    for eachvar in mytemplist:
        isum = isum + eachvar
    mean = isum/lengthofarray
    if lengthofarray%2 != 0:
        indexnum = int(((lengthofarray + 1)*0.5)-1)
        median = mytemplist[indexnum]
    else:
        indexnum1 = int(lengthofarray/2)
        indexnum2 = int((lengthofarray/2) - 1)
        median = (mytemplist[indexnum1] + mytemplist[indexnum2])/2
    print("The sorted array is: ", mytemplist)
    print("The sum of the numbers in the array is: ", isum)
    print("The mean is: ", mean)
    print("The median is: ", median)
    return mytemplist, isum, mean, median


#number guessing games
#import random
#randomized = int(random.randint(1,10))
#print(randomized)

def resultofguess(user_guess, randomized):
    """This function takes a user input and validates it against a randomized integer"""
    result = user_guess == randomized
    if user_guess < 0 or user_guess > 10:
        print("You have entered an invalid number.")
    else:
        if result == True:
            print("You entered the correct number!!!")
        else:
            print("Incorrect!. Please try again")

    
    


def scoregrade(score):
    if score < 0 or score > 100:
        print("You have entered an invalid score")
    else:
           if score >= 0 and score < 40:
                print("Grade: F")
           elif score >= 40 and score < 45:
                print("Grade: E")
           elif score >= 45 and score < 50:
                print("Grade: D")
           elif score >= 50 and score < 60:
                print("Grade: C")
           elif score > 60 and score < 70:
                print("Grade: B")
           else:
                print("You got an A, Champ!")






