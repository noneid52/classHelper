import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

#ImportFoodDataCSV
foodDataCsvFile = "foodData.csv"

def loadFoodDataCsv():
    try:
        foodData = pd.read_csv(foodDataCsvFile)
        return foodData
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {foodDataCsvFile} not found.")
        return None

# Pick Food Main
def pickRandomFoodMain():
    app = tk.Tk()
    app.title("랜덤 음식 뽑기")
    app.geometry("400x300")

    label = tk.Label(app, text="랜덤 음식 뽑기!", font=("맑은 고딕", 30, "bold"))
    label.pack(pady=10)

    pick_button = tk.Button(app, text="뽑기!", command=pickRandomFoodRun, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
    pick_button.pack(pady=50)

# Pick Food Function
def pickRandomFoodRun():
    if foodData is None:
        return
    max_number = foodData["number"].max()
    random_number = random.randint(1, max_number)
    matched_row = foodData[foodData["number"] == random_number]

    if not matched_row.empty:
        name = matched_row.iloc[0]["name"]
        messagebox.showinfo("결과창", f"뽑아진 음식: {name}")
    else:
        messagebox.showinfo("결과창", f"Number: {random_number} (No matching name found)")

########################################################

# Run Timer Main
def runTimerMain():
    global timerRunning, timeLeft, resetFlag, setFlag
    timerRunning = False
    timeLeft = 0  # Left Time(sec)
    resetFlag = 0
    setFlag = 0

    def setTimer():
        global timeLeft, setFlag
        try:
            hours = int(enterHour.get())
            minutes = int(enterMinute.get())
            seconds = int(enterSecond.get())
            timeLeft = hours * 3600 + minutes * 60 + seconds
            updateTimerLabel()
            setFlag = 1
        except ValueError:
            timerLabel.config(text="잘못된 입력!")

    def updateTimerLabel():
        hours = timeLeft // 3600
        minutes = (timeLeft % 3600) // 60
        seconds = timeLeft % 60
        timerLabel.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    def startTimer(): # Start Timer
        if setFlag == 1 :
            global timerRunning
            if not timerRunning:
                timerRunning = True
                countdown()

    def pauseTimer(): # Pause Timer
        global timerRunning
        timerRunning = False

    def resetTimer(): # Reset Timer
        global timerRunning, timeLeft, resetFlag
        timerRunning = False
        timeLeft = 0
        timerLabel.config(text="00 : 00 : 00")
        resetFlag = 1

    def countdown():
        global timeLeft, timerRunning, resetFlag
        if timerRunning and timeLeft > 0:
            timeLeft -= 1
            updateTimerLabel()
            app.after(1000, countdown)
        elif timeLeft == 0:
            if resetFlag == 0:
                timer_running = False
                timerLabel.config(text="시간 종료!")
                messagebox.showinfo("시간 종료", f"시간 종료!")
                setFlag = 0
            elif resetFlag == 1: # reset?
                resetFlag = 0
                setFlag = 0

    # GUI Part
    app = tk.Tk()
    app.title("타이머")
    app.geometry("400x300")

    label = tk.Label(app, text="타이머!", font=("맑은 고딕", 30, "bold"))
    label.pack(pady=10)

    timerLabel = tk.Label(app, text="00:00:00", font=("맑은 고딕", 25), fg="blue")
    timerLabel.pack(pady=20)

    enterFrame = tk.Frame(app)
    enterFrame.pack(pady=5)

    enterHour = tk.Entry(enterFrame, width=5)
    enterHour.insert(0, "0")
    enterHour.pack(side="left")

    enterMinute = tk.Entry(enterFrame, width=5)
    enterMinute.insert(0, "0")
    enterMinute.pack(side="left")

    enterSecond = tk.Entry(enterFrame, width=5)
    enterSecond.insert(0, "0")
    enterSecond.pack(side="left")

    setButton= tk.Button(enterFrame, text="설정", command=setTimer, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
    setButton.pack(side="left", padx=5)

    buttonFrame = tk.Frame(app)
    buttonFrame.pack(pady=10)
    startButton = tk.Button(buttonFrame, text="시작 / 재개", command=startTimer, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
    startButton.pack(side="left", padx=5)
    pauseButton = tk.Button(buttonFrame, text="정지", command=pauseTimer, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
    pauseButton.pack(side="left", padx=5)
    #resetButton = tk.Button(buttonFrame, text="초기화", command=resetTimer, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
    #resetButton.pack(side="left", padx=5)

    copyrightLabel = tk.Label(app, text="타이머를 한번 실행을 하였으면 종료 후 다시 실행 바랍니다.", font=("맑은 고딕", 9))
    copyrightLabel.pack(side="bottom", pady=0)

########################################################

#ImportNameDataCSV
nameDataCsvFile = "nameData.csv"

def loadNameDataCsv():
    try:
        nameData = pd.read_csv(nameDataCsvFile)
        return nameData
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {nameDataCsvFile} not found.")
        return None

# Pick Name Main
def pickRandomNameMain():
    app = tk.Tk()
    app.title("랜덤 이름 뽑기")
    app.geometry("400x300")

    label = tk.Label(app, text="랜덤 이름 뽑기!", font=("맑은 고딕", 30, "bold"))
    label.pack(pady=10)

    pick_button = tk.Button(app, text="뽑기!", command=pickRandomNameRun, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
    pick_button.pack(pady=50)

# Pick Name Function
def pickRandomNameRun():
    if nameData is None:
        return
    max_number = nameData["number"].max()
    random_number = random.randint(1, max_number)
    matched_row = nameData[nameData["number"] == random_number]

    if not matched_row.empty:
        name = matched_row.iloc[0]["name"]
        messagebox.showinfo("결과창", f"뽑아진 이름: {name}")
    else:
        messagebox.showinfo("결과창", f"Number: {random_number} (No matching name found)")

########################################################

# CSV Load
foodData = loadFoodDataCsv()
nameData = loadNameDataCsv()

# Main GUI
app = tk.Tk()
app.title("수업 도우미")
app.geometry("500x400")

# Header Title
mainLabel = tk.Label(app, text="수업 도우미!", font=("맑은 고딕", 30, "bold"))
mainLabel.pack(pady=30)

# Pick Food Button
foodStartButton = tk.Button(app, text="랜덤 음식 뽑기", command=pickRandomFoodMain, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
foodStartButton.pack(pady=10)

# Timer Button
timerStartButton = tk.Button(app, text="타이머", command=runTimerMain, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
timerStartButton.pack(pady=10)

# Pick Name Button
numberStartButton = tk.Button(app, text="랜덤 이름 뽑기", command=pickRandomNameMain, font=("맑은 고딕", 12), activeforeground="red", relief="raised")
numberStartButton.pack(pady=10)


# Run GUI
app.mainloop()
