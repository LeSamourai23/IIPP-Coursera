import os

os.system('cls')

### Practice Question Paper (AN INTRODUCTION TO INTERACTIVE PROGRAMMING IN PYTHON [CRA 4013])

## Q1A. How do you define a function in Python? Write a function to calculate the sum of thedigits in an integer. 
# if a function contains no return statement, what value does the function return?

# Ans.
# A function is a block of code which only runs when you call it.
def add(a, b):
    print(a+b)

a= int(input("a: "))
b= int(input("b: "))

add(a,b)
# If no return is there the function will return "none"   

## Q1B. What is the use of range() method? Explain with an example

# Ans.
# A range method is used to generate a range of numbers. It takes two arguments start and stop and an optional third argument step.
for i in range(1, 6):
    print (i) 
#1, 2, 3, 4, 5

## Q2A. What do you mean by a class? How do you create instances of a class? Explain the
# purpose of the _ _ init _ _ method in a class. Illustrate with an example.

# Ans.
# A class is a blueprint for creating objects (instances) that have a set of
# attributes and methods. It provides a way to define the behavior and 
# characteristics of objects of a particular type.

# __init__ method is used to initialize the object's attributes and perform any other setup that may by required.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        doy = 2023 - int(self.age)
        print(f"Hello {self.name}. You were born in the year {doy}") 

name= input("Enter your name: ")
age= input("Enter your age: ")

person1 = Person(name, age)

person1.introduce()

## Q2B. Differentiate between local variables and global variables in Python. Illustrate with an example

#Local Variable- They are declared within a function and are only accessible within the scope of the function
def lv_function():
    y = 10
    print(y)

lv_function()
#Global Variable- The are declared ouside the function and are accessible everywhere in the code
x=10

def gv_function():
    print("Inside the function:", x)

gv_function()

print("Outside the function:", x)

## Q2C. How do you load an image using simplegui? Give an example.

#Ans. 
#simplegui.load_image(URL)

import simplegui

def draw_handler(canvas):
    canvas.draw_image(image, (1500//2, 1800//2), (1500, 1800), (1280/2, 720/2), (1280, 720))
          #           image,  center_source, width_height_source, center_dist, width_height_dist            

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')

frame = simplegui.create_frame("Testing", 1280, 720)
frame.set_draw_handler(draw_handler)
frame.start()

## Q3A.  What is a dictionary? Explain the method of iterating over the elements of a dictionary. Give an example.

# Ans. 
# It is an unordered pair of keys and values. It is also known as associative pair or hash table. 
# Each key in a dictionary has a value and vice-versa

student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

# Iterating over key-value pairs using a for loop
for name, score in student_scores.items():
    print(f"{name} scored {score} marks")

# Iterating over keys using a for loop
for name in student_scores.keys():
    print(name)

# Iterating over values using a for loop
for score in student_scores.values():
    print(score)

# Q3B. What is the difference between list and tuple? Illustrate with an example.

# Ans.
# Lists-> 1. They are mutable (can be modified after creation)
#         2. They are defined using []
# Tuples-> 1. Tuples are immutable (cannot be modified after creation)
#          2. They are defined using ()

fruits = ['apple', 'banana', 'orange', 'pineapple']
juices = ('apple juice', 'orange juice', 'pineapple juice')

print(fruits) #['apple', 'banana', 'orange', 'pineapple']
fruits.append('grape')
print(fruits)    # ['apple', 'banana', 'orange', 'pineapple', 'grape'] 

#juices.append('watermelon juice') #Attribute Error
#print(juices)
 
## Q3C. How do you define and use a label in python?

# Ans.
# label1 = frame.add_label('My first label')

## Q4A. Write a program in Python to input the marks scored by a student in three subjects,
##      calculate the total and average marks and grade the student based on the following criteria
marks1 = int(input("Enter Subject 1 Markes: "))
marks2 = int(input("Enter Subject 2 Markes: "))
marks3 = int(input("Enter Subject 3 Markes: "))

def result(a, b, c):
    print(f'Your total marks are {a+b+c}')
    print(f'Your average marks are {(a+b+c)/3}')

result(marks1, marks2, marks3)

## Q4B. What are the three parts of a frame? Explain.

# Ans.
# In the context of the SimpleGUI library, which is a graphical user interface (GUI) framework for Python, a frame consists of three main parts:

# Canvas: The canvas is the primary area within the frame where graphical elements, such as shapes, images, and text, can be displayed. 
#        It provides a drawing surface for creating visual content.

# Controls: Controls are interactive elements, such as buttons, input fields, checkboxes, sliders, and dropdown menus, that allow users to interact with the program. 
#          These controls provide functionality to respond to user input and trigger actions or events.

# Timers: Timers are used to schedule and control the timing of events in the frame. They allow you to set up recurring or delayed actions, such as updating the canvas, moving objects, or executing specific functions at regular intervals.

# Together, these three parts work in harmony to create a functional and interactive GUI application using the SimpleGUI library. 
# The canvas provides the visual representation of the program, controls enable user interaction, and timers facilitate time-based actions and animations.

## Q5A. What do you mean by event-driven programming? Explain the method of implementing it in Python

# Ans.
# Event-driven programming is a programming paradigm where the flow and execution of a program are determined by events. An event can be any occurrence or action, such as user interactions (mouse clicks, keyboard input), system notifications, or messages from other parts of the program. 
# In event-driven programming, the program waits for events to occur and then responds to them by executing specific event handlers or callbacks.

import simplegui

def button_clicked():
    print("Button clicked!")

# Create a frame
frame = simplegui.create_frame("Event Handling Example", 200, 200)

# Register the button_clicked() function as the event handler for a button click event
frame.add_button("Click Me", button_clicked)

# Start the frame
frame.start()

## Q5B. Write the syntax of the while looping structure and explain it’s working. Write Python code segment to print the numbers from 1 to 10 using a while loop.

# Ans.

# while(condition):
#   Some Code

# Basically, till the condition is met in the while loop, it will continue to run the code block indented inside it

a = 1
while a <= 10:
    print(a)
    a += 1

## Q5C. Given the strings s1 = “Python” and s2 = “Programming”, write the outputs of the
##      following statements:
##      a) print s1[-1]
##      b) print s2[:5]
##      c) print s1[3:]
##      d) print s1[2:3] + s2[0] (2)

# Ans.
# a) n
# b) Progr
# c) hon
# d) tP

