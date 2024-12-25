import pyttsx3
import speech_recognition
import webbrowser
import pyaudio
import playsound
from gtts import gTTS
import os
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

i=0
while i<3:
    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi đang nghe, bạn nói đi.")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio,language="vi-VI")
        print("You: {}".format(you))
    except:
        i=i+1
        print("Robot: Xin lỗi! tôi không nhận được voice!")
        robot_brain = "Mình không nghe được bạn nói, bạn nói lại nhé"
        output = gTTS(robot_brain,lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        continue

    if "chào" in you:
        robot_brain = "Hello Hòa"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "now" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "Google" in you:
        webbrowser.open("C:\Program Files\Google\Chrome\Application\chrome.exe")
        robot_brain = "Đã mở Google"
    elif "Hòa" in you:
        robot_brain = "Hòa là một học sinh gương mẫu, có trách nhiệm trong công việc và là một người rất đẹp trai"
    elif "bye" or "tạm biệt" in you:
        robot_brain = "Tạm biệt, Hòa"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        output = gTTS(robot_brain,lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        break
    else:
        robot_brain = "Xin lỗi, phần này tôi chưa được học."

    print("Robot: " + robot_brain)
    #robot_mouth.say(robot_brain)
    #robot_mouth.runAndWait()

    output = gTTS(robot_brain,lang="vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3')
    os.remove('output.mp3')
