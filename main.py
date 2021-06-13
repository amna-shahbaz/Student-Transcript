_author_ = "Amna Shahbaz"
_date_ = "Thursday, June 9th, 2021"
_version_ = "1.0"
_filename_ = "Shahbaz_Amna_Assignment-4.py"
_description_ = "Student transcript for school using lists."


def get_int (prompt):
  """This function requests an input given a prompt, then outputs the integer after conversion."""
  while True:
    try:
      i = int(input(prompt))
    except:
      print("Invalid Entry")
    else:
      break
  return i

def get_mark (prompt):
  """This function requests an input given a prompt, then validates if mark is between 0-100."""
  while True:
    try:
      n = int(input(prompt))
    except ValueError:
      pass
    else:
      if n in range(0, 101):
        return n

def sum_list(l):
  """This function takes the sum of all the integers in the list."""
  sum = 0
  for x in l:
    sum += x
  return sum

def check_silver_medal (prompt):
  """This function requests an input given a prompt, then checks if student average is for silver medal or scholar."""
  if average >= SILVER_MEDALIST:
    print("You are a silver medal student and Ontartio scholar.")
  elif average >= HONOUR_ROLL:
    print ("You are an Ontario scholar.")
  else:
    print ("Good job!")
  return average

SILVER_MEDALIST = 90
HONOUR_ROLL = 80
#Take user inputs
name = input("Please enter your name: ")
grade_year = get_int ("Please enter your grade (year): ")
date_student = input("Please enter the date: ")
num = get_int ("Enter your number of courses: ")

user_list_courses = []
user_list_marks = []

#For loop to ask for course codes and marks
for i in range(num):
  a = input ("\nEnter your course code (first 6 characters): ")
  #Validates first 6 characters
  first_six_characters = a[0:6]
  user_list_courses.append(first_six_characters)
  b = get_mark ("Enter your mark for this course: ")
  user_list_marks.append(b)

#Takes the average of all marks
average = round((sum_list(user_list_marks)/num),2)

print ("-------------------------------------")
print ("Transcript: \n")

print("Name:", name)
print ("Grade year:", grade_year)
print ("Date:", date_student, "\n")
print ("Courses: ")
for courses in user_list_courses:
  print (courses)
print ("\nMarks: ")
for marks in user_list_marks:
  print (marks,"%")
print ("\nAverage:", average,"%")
check_silver_medal(average)