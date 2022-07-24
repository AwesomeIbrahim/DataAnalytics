#!/usr/bin/env python
# coding: utf-8

# In[187]:


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



def resultofvalidguess(user_guess, randomized):
    """This function takes a user input and validates it against a randomized integer"""
    result = user_guess == randomized
    if user_guess < 0 or user_guess > 10:
        print("You have entered an invalid number.")
    else:
        if result == True:
            print("You entered the correct number!!!")
        else:
            print("Incorrect!. Please try again")

    
def validateuserinput(user_guess):
    """This function takes a user input and validates if it is within range 0 and 10"""
    validity = user_guess < 0 or user_guess > 10
    if validity = True:
        print("You have entered an invalid number.")
    else validity = False
    return validity
    
    


def scoregrade(score):
    """This function accept a score between 0 and 100 and returns the student's grade"""
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

                
def palindrome(val_string):
    val_string = str(val_string)
    reversedstring = val_string[::-1]
    if reversedstring == val_string:
        print(val_string,"is a palindrome")
    else:
        print(val_string,"is not a palindrome")

def getuserdata():
    """This function collates student's comma-separated scoresscores from a user till 'no' is used to end"""
    student_dict = {}
    while True:
        student_id = input("Please Enter the student ID: ")
        student_scores = input("please enter student score separated by a ',':")
        student_scores_list = student_scores.split(",")
        scores_list = []
        for eachscore in student_scores_list:
            eachscore = float(eachscore)
            scores_list.append(eachscore)
        student_dict[student_id] = scores_list
        more_student = input("Enter 'no' if you do not want to terminate and press any other key to continue")
        if more_student.lower() == "no":
            break
        else:
            continue
    return student_dict

def sumandaverage(student_dicts):
    """This function computes the sum and average for each student for data collected from the getuserdata function"""
    summary={}
    for eachstd in student_dicts:
        _sum = 0
        sumlist = []
        for eachval in student_dicts[eachstd]:
            _sum = _sum + eachval
        averagescore = round(_sum/len(student_dicts[eachstd]),1)
        sumlist = [_sum,averagescore]
        summary[eachstd] = sumlist
    #print(summary)
    return summary
    
    
    


# In[189]:


mydata = {'A': [99.0, 76.0, 78.0], 'B': [56.0, 77.0, 45.0], 'C': [67.0, 33.0, 9.0]}
sumandaverage(mydata)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




