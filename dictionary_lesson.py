programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "loop": "The action of doing something over and over",
                          }

#difference betweem a list and a dictionary
# dictionary call value by their keys
# list call value by their index
# dictionary is has key and value like prameter
# list has index and stored data

#important note we use {} to create the dictionary and store the value in
#imporatnt note we use [] to access the key to call the value

print(programming_dictionary["Bug"])

#add stuff to a exisiting dictionary
programming_dictionary["house"] = " a home people live in"
print(programming_dictionary)

# difference between creating empy list or empty dictionary
empty_list = []
empty_dictionary = {}

#wipe out a existing dictionary / reset it to empty
programming_dictionary1 ={}
print(programming_dictionary1)

#ediiting an item in the dictionary
programming_dictionary["Bug"] = "dragonfly"
print(programming_dictionary)


#looping through a dictionary
#for list / work dictionary for to loop through the key
for thing in programming_dictionary:
    print(thing)
    #print out the key value buy accessing the key
    print(programming_dictionary[thing])


#excerise

# Udemy
# 100 Days of Code: The Complete Python Pro Bootcamp
# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 



# Write a program that converts their scores to grades.



# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 



# The final version of the student_grades dictionary will be checked. 



# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 



# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# created a empty dictionary 
student_grades = {}

def getstudent_grades():
    # lopping throught the dictionary to get the key
    for name in student_scores:
        #access student score using the key to unlock it and storeing it into a variable grade_value 
        grade_value = student_scores[name]
        print(grade_value)

        #this will compare the key to the number and it correspoding grade outcome
        if grade_value >= 91:
            grade = "Outstanding"
        elif 81 <= grade_value <= 90:
            grade = "Exceeds Expectations"
        elif 71 <= grade_value <= 80:
            grade = "Acceptable" 
        else: 
            grade = "Fail"
       
        #store the name into the new dictionary and assigning the key with it value each time
        student_grades[name] = grade
    print(student_grades)
getstudent_grades()