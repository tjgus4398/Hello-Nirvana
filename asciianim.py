import os, time
import io
import pyautogui

filenames = os.listdir("/Users/hwangseohyeon/Desktop/WEB/python/asciiart")
filenames = [v for v in filenames if v.split(".")[-1]=="txt"]
filenames.sort()

def asciianim(filenames, delay = 1, repeat = 10):
    frames = []
    for name in filenames:
        with io.open("/Users/hwangseohyeon/Desktop/WEB/python/asciiart/"+name, "r", encoding="utf-8") as f: #No such file or directory:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system("clear")

os.system("clear")
asciianim(filenames, delay= 0.1, repeat= 50) # 반복 횟수