import numpy as np
from random import randint
import datetime
import time
        
with open('file.txt', 'a') as f:
    now = datetime.datetime.now()    
    f.write(now.strftime("Session Date: %m-%d-%y "))
    f.write("\n")
    

    
    class givenator:
        def __init__(self, start1, end1, start2, end2):
            given1 = 10
            given2 = 10
            while (given1 % 10 == 0) or (given2 % 10 ==0):
                given1 = randint(start1, end1)
                given2 = randint(start2, end2)
            if start2 == 1:
                given2 = given1
            self.given1 = given1
            self.given2 = given2
        def make_givens(self):
                g1 = str(self.given1)
                g2 = str(self.given2)
                return g1 + " x " + g2
        def multiply(self):
            return self.given1 * self.given2
        def square():
             return self.given1**2
               
    class tabulate():
        session = 0
        ses_accuracy = 0.0
        speed = 0.0
        items = 0
        allscore = 0
        categSpeed = [], [], [], []
        categAccu = [], [], [], []
        def __init__(self, correct, answers, category, laptime):
            self.correct = correct
            self.answers = answers
            self.score = 0
            self.accuracy = 0.0
            self.category = category
            self.laptime = laptime
            self.speed = 0
            tabulate.session+=1
        def tab(self):
            for i in range(10):
                if self.answers[i] == self.correct[i]:
                    print(f"{i+1}.) Correct  {self.answers[i]} == {self.correct[i]}")
                    self.score +=1
                else: 
                    print(f"{i+1}.) Incorrect  {self.answers[i]} != {self.correct[i]}")
            tabulate.allscore+=self.score
            tabulate.items +=10
            print(f"Score: {self.score}/10")                
        def record(self):
            self.accuracy = self.score/10
            self.speed = sum(self.laptime)/10
            tabulate.categAccu[self.category].append(self.accuracy)
            tabulate.categSpeed[self.category].append(self.speed)
            tabulate.ses_accuracy = tabulate.allscore/tabulate.items
            print(f"Speed: {self.speed}")
            print(f"Category Avg Accuracy: {sum(tabulate.categAccu[self.category])/len(tabulate.categAccu[self.category])}")
            print(f"Category Avg Speed: {sum(tabulate.categSpeed[self.category])/len(tabulate.categSpeed[self.category])}")
            time = datetime.datetime.now()    
            f.write(time.strftime("Time: %H: %M"))
            f.write("\n")
            f.write(f"Set No.:  {tabulate.session}")
            categoutput = {1: "TWObyTWO", 2:"THREEbyONE", 3:"SQUARE2"}
            f.write("Category: ")
            f.write(str(categoutput[self.category]))
            f.write("\n")
            f.write("Accuracy:" ) 
            f.write(str(self.score/10))
            f.write("\n")
            f.write("Speed: ")
            f.write(str(self.speed))
            f.write("\n\n")
            
            
                    
              
       
    
    category = 0
    instance = [], [], [], []
    
    while category != 5:
        print("------Mental Math------\n1-Two-digits by two-digits\n2-Three-digits by one-digit\n3-Squaring two-digits\4-Mixed Problems\n5-Exit")
        category = int(input("Category: "))
        if(category == 5):
            break
        if(category == 1):
            categories = [10, 100, 10, 100]
        if(category == 2):
            categories = [100, 1000, 2, 10]
        if(category == 3):
            categories = [10, 100, 1, 1]
        questions = []
        correct = []
        s = len(instance[category])
        answers = []
        laptime = np.ones(10)
        start = time.time()
        lap = start
        
        for i in range(10):
            questions.append(givenator(categories[0], categories[1], categories[2], categories[3]))
            print(i+1, "). ", questions[i].make_givens())
            try:      
                answers.append(int(input("Answer:")))
            except:
                print("Invalid input! Try again")
                answers.append(int(input("Answer:")))
            laptime[i] = round((time.time() - lap), 2)
            lap = time.time()
            correct.append(questions[i].multiply())
        instance[category].append(tabulate(correct, answers, category, laptime))
        print(instance[category][0])
        instance[category][s].tab()
        instance[category][s].record()
        s +=1 
    f.write("Frequency: TWObyTWO: ")
    f.write(str(len(tabulate.categAccu[1])))
    f.write("| THREEbyONE: ")
    f.write(str(len(tabulate.categAccu[2])))
    f.write("| SQUARE: ")
    f.write(str(len(tabulate.categAccu[3])))
    f.write("\n")
    f.write("Session Accuracy: TWObyTWO: ")
    try:    
        f.write(str(sum(tabulate.categAccu[1])/len(tabulate.categAccu[1])))
    except: 
        f.write(str(0.0))
    f.write(" | THREEbyONE: ")
    try:    
        f.write(str(sum(tabulate.categAccu[2])/len(tabulate.categAccu[2])))
    except:
        f.write(str(0.0 ))
    f.write(" | SQUARE: ")
    try:
        f.write(str(sum(tabulate.categAccu[3])/len(tabulate.categAccu[3])))
    except:
        f.write(str(0.0 ))
    f.write("\n")
    f.write("Session Speed: TWObyTWO: ")
    try:    
        f.write(str(sum(tabulate.categSpeed[1])/len(tabulate.categSpeed[1])))
    except:
        f.write(str(None ))
    f.write("| THREEbyONE: ")
    try:
        f.write(str(sum(tabulate.categSpeed[2])/len(tabulate.categSpeed[2])))
    except:
        f.write(str(None ))
    f.write(" | SQUARE: ")
    try:
        f.write(str(sum(tabulate.categSpeed[3])/len(tabulate.categSpeed[3])))
    except:
        f.write(str(None ))
    f.write("\n\n") 
    
    