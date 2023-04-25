#This is the source that I used for Tkinter. https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

#The following are the libraries that I will be using.
import random
import itertools
from tkinter import *
from time import time 

window=Tk() #Creates an object called "window" that is made using Tk.

print('Running...')

#These variables will contain the value displayed as the question, as well as the answer values, designed to match the question.
question=StringVar()
chosen_answer=StringVar()

#These next four values hold the values of their respective answer buttons.
answer_a=StringVar()
answer_a.set("Answer A")

answer_b=StringVar()
answer_b.set("Answer B")

answer_c=StringVar()
answer_c.set("Answer C")

answer_d=StringVar()
answer_d.set("Answer D")

#These two values will respectively hold the value of the right answer and the button clicked for use within later methods.
correct_answer_button = None
answer_button_pressed = None


#This sets the value of the time, which is recorded in seconds.
second=IntVar()

#This sets the value of the score, which raises by 1, with each correct answer
score=IntVar()

#This is the timer. It holds a value called "time" that starts at 60 and goes down in intervals of one second when the game starts.
def timer(time):
    TimeSpace["text"] = time
    if time > 0:
        window.after(1000, timer, time-1)
    else:
        stop()


#The following four dictionaries contain all values necessary for each question to work. That is the question and a set of answers.
questiondicta = {
    "question": "How would you finish a line containing a function definition?",
    "answers": ["():","();", "()-", "()"]
}
questiondictb = {
    "question": "What kind of brackets are used for lists?",
    "answers": ["Square Brackets", "Round Brackets", "Curly Brackets", "No Brackets"]
}
questiondictc = {
    "question": "Which of the following Python libraries would be best suited for designing interfaces and forms?",
    "answers": ["Tkinter", "Numpy", "Mesa", "Matplotlib"]
}
questiondictd = {
    "question": "Which symbol would you start a comment with in Python?",
    "answers": ["#", "//", "-", "()"]
}

#This set contains all of the dictionaries and one of them will be chosen at random.
questions = [questiondicta, questiondictb, questiondictc, questiondictd]


#The "start" method (or command) starts the game by outputting the first question and setting the second value to 60 and score value to 0.
def start(): 
    global answer_button_pressed 
    global correct_answer_button
    score.set("0")
    timer(60)

    #This choses a random value from the set of questions.
    #"q" represents the chosen dictionary
    q = questions[random.randint(0,3)]

    #These lines make use of the chosen dictionary and
    #from it, they asssign the question and answer values.
    chosen_question = q["question"]
    question.set(chosen_question)
    chosen_answers = q["answers"]
    
    #This sets up the answer permutations. 
    #There are four different combinations of answer choices and one of the four is chosen at random
    answer_mappings = list(itertools.permutations([0, 1, 2, 3]))
    mapping = list(answer_mappings[random.randint(0,len(answer_mappings))])
    
    #New values are given to the answer buttons based off of the permutations
    answer_a.set(chosen_answers[mapping[0]])
    answer_b.set(chosen_answers[mapping[1]])
    answer_c.set(chosen_answers[mapping[2]])
    answer_d.set(chosen_answers[mapping[3]])

#This method assigns the value of the correct answer. It is always the first value in the set.
    for i in range(0,3):
        if mapping[i] == 0:
            correct_answer_button = i

#This method, which triggers when an answer is given is identical to the "start" method, except that it doesn't reset the timer or score.
def next_question():
    global answer_button_pressed 
    global correct_answer_button

#These two lines ask the code to get the current score and select another question randomly.
    current_score = score.get()
    q = questions[random.randint(0,3)]

    #The values of the newly chosen question dictionary replace the previous questions and answers.
    chosen_question = q["question"]
    question.set(chosen_question)
    chosen_answers = q["answers"]
    
    #New permutations are set up as well.
    answer_mappings = list(itertools.permutations([0, 1, 2, 3]))
    mapping = list(answer_mappings[random.randint(0,len(answer_mappings))])
    
    #The mapping method is also reused.
    for i in range(0,3):
        if mapping[i] == 0:
            correct_answer_button = i

#This method verifies if the button chosen matches the one for the correct answer.
#If so, it will raise the value of the score by 1, otherwise it will load the next question without doing anything.
    global answer_button_pressed 
    if answer_button_pressed == correct_answer_button:
        current_score = current_score + 1
    else:
        current_score = current_score
    score.set(current_score)

    #These new answer button values are set based on the permutations as well.
    answer_a.set(chosen_answers[mapping[0]])
    answer_b.set(chosen_answers[mapping[1]])
    answer_c.set(chosen_answers[mapping[2]])
    answer_d.set(chosen_answers[mapping[3]])

#In the event that each button is pressed, that button becomes the value of answer_button_pressed.    
def button_press_A():
    global answer_button_pressed 
    answer_button_pressed = 0
    next_question()

def button_press_B():
    global answer_button_pressed 
    answer_button_pressed = 0
    next_question()

def button_press_C():
    global answer_button_pressed 
    answer_button_pressed = 0
    next_question()

def button_press_D():
    global answer_button_pressed 
    answer_button_pressed = 0
    next_question()

#The stop method stops the game by resetting the questions and stopping the timer.
def stop():
    question.set("")
    timer.time = None
    answer_a.set("Answer A")
    answer_b.set("Answer B")
    answer_c.set("Answer C")
    answer_d.set("Answer D")

#These are the various widgets of my Python game. They determine how the game is presented.
TitleLabel=Label(window, text="Python Trivia Game", fg='black', font=("Cambria, 56"))
TitleLabel.place(x=120, y=30)

#These are the details for the space where the questions are displayed.
QuestionSpace = Entry(window, width=80, font=("Arial", 12), textvariable= question)
QuestionSpace.place(x=50, y=180)

#The following four widgets detail information about the answer buttons.
ButtonA=Button(window, fg='blue', font=("Cambria, 18"), textvariable=answer_a, command = button_press_A)
ButtonA.place(x=80, y=250)

ButtonB=Button(window, text="Answer B", fg='red', font=("Cambria, 18"), textvariable=answer_b, command = button_press_B)
ButtonB.place(x=280, y=250)

ButtonC=Button(window, text="Answer C", fg='orange', font=("Cambria, 18"), textvariable=answer_c, command = button_press_C)
ButtonC.place(x=480, y=250)

ButtonD=Button(window, text="Answer D", fg='green', font=("Cambria, 18"), textvariable=answer_d, command = button_press_D)
ButtonD.place(x=680, y=250)

#This details where the "Start" button goes. When clicked, it triggers the "start" command.
StartButton=Button(window, text="Start", fg='black', font=("Cambria, 26"), command = start)
StartButton.place(x=300, y=400)

#The "Stop" button and the "stop" command are assigned in a similar way.
StopButton=Button(window, text="Stop", fg='black', font=("Cambria, 26"), command = stop)
StopButton.place(x=500, y=400)


#This entry section is called "TimeSpace" and will keep track of the time that the player has left.
TimeSpace = Label(window, text="60", width=3, font=("Arial", 24))
TimeSpace.place(x=500, y=500)

#This section is called "ScoreSpace and will keep track of the player's score.
ScoreSpace = Label(window, width=3, font=("Arial", 24), textvariable=score)
ScoreSpace.place(x=300, y=500)

#This label tells the player where the time space is.
TimeLabel=Label(window, text="Time", fg='black', font=("Cambria, 16"))
TimeLabel.place(x=500, y=550)

#While this label tells the player where the score space is.
ScoreLabel=Label(window, text="Score", fg='black', font=("Cambria, 16"))
ScoreLabel.place(x=300, y=550)

#This three lines are the most important as they allow the form itself to appear, without it, the widgets wouldn't display.
window.title('Python Trivia Game - Designed by Joshua Hore') #This details what will be displayed in the window
window.geometry("900x600+10+20") #This specifies the dimensions of the window. (widthxheight+x+y)
window.mainloop() #The new window is now an application constantly awaiting new events to also be specified in the program.