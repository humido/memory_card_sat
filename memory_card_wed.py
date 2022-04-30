#Great!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

q1=Question("In what year was the grear fire of London?", "1666", "1999", "1062", "666")
q2=Question("In what year was Moscow founded?", "1047", "1666", "147", "2012")
q3=Question("What is the powerhouse of the cell?", "mytochondria", "heart", "nucleus", "oven")
q4=Question("What is Force divided by mass?", "acceleration", "distance", "power", "speed")
q5=Question("What is the integral of sin(x)?", "-cos(x)", "tan(x)", "cos(x)", "-sin(x)")

q_list = [q1,q2,q3,q4,q5]

def show_ans():
    check()
    gbox1.hide()
    gbox2.show()
    ans_b.setText("Next Question")

def show_qst():  
    gbox2.hide()
    gbox1.show()
    ans_b.setText("Answer")
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if ans_b.text() == "Finish":
        quit() 
    elif ans_b.text() == "Answer":
        show_ans()
    else:
        next_question()

def ask(q: Question):
    shuffle(but_list)
    label1.setText(q.question)
    label3.setText(q.right_answer)
    but_list[0].setText(q.right_answer)
    but_list[1].setText(q.wrong1)
    but_list[2].setText(q.wrong2)
    but_list[3].setText(q.wrong3)

def check():
    if but_list[0].isChecked():
        label2.setText("Correct. Well done.")
        main_win.correct += 1
    else:
        label2.setText("Incorrect. The answer is:")
        main_win.wrong +=1
    rating = main_win.correct/(main_win.correct+main_win.wrong)*100
    label4.setText("Correct answers: " + str(main_win.correct))
    label5.setText("User rating: " + str(rating//1) + "%")

#def next_question():
#    main_win.counter += 1
#    shuffle(q_list)
#    if main_win.counter >= len(q_list):
#        main_win.counter = 0    
#    ask(q_list[main_win.counter])
#    show_qst()

def next_question():
    if len(q_list):
        shuffle(q_list)
        q=q_list[0]
        ask(q)
        q_list.remove(q)
        show_qst()
    else:
        label1.setText("The test has ended")
        ans_b.setText("Finish")


app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card App")
main_win.move(2400,300)
main_win.resize(400,300)
main_win.counter = -1
main_win.correct = 0
main_win.wrong = 0

label1 = QLabel("--A very difficult question goes here.--")
gbox1 = QGroupBox("Answer options")
gbox2 = QGroupBox("Correct Answer")

label2=QLabel("--Correct/Incorrect--")
label3=QLabel("--correct answer written here--")
label4=QLabel("Correct answers: 0")
label5=QLabel("User Rating: 0%")

ans_b = QPushButton("Answer")

b1=QRadioButton("Option 1")
b2=QRadioButton("Option 2")
b3=QRadioButton("Option 3")
b4=QRadioButton("Option 4")

but_list=[b1,b2,b3,b4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

v1=QVBoxLayout()
v2=QVBoxLayout()
v3=QVBoxLayout()
v4=QVBoxLayout()
h1=QHBoxLayout()

v1.addWidget(label4, alignment = Qt.AlignRight)
v1.addWidget(label5, alignment = Qt.AlignRight)
v1.addWidget(label1)
v1.addWidget(gbox1)
v1.addWidget(gbox2)

v1.addWidget(ans_b, stretch=3)
v2.addWidget(b1)
v2.addWidget(b2)
v3.addWidget(b3)
v3.addWidget(b4)
h1.addLayout(v2)
h1.addLayout(v3)
v4.addWidget(label2)
v4.addWidget(label3)
gbox2.setLayout(v4)
gbox1.setLayout(h1)


main_win.setLayout(v1)
gbox2.hide()

next_question()

ans_b.clicked.connect(test)

main_win.show()
app.exec()
