import os

file = open('Start.txt', 'r')
text = file.read()

if text[0] == "1":
    text = text.split("\n")
    for index, module in enumerate(text):
        if index  == 0:
            pass
        else:
            os.system(f"pip install {module}")
    file = open("Start.txt", 'w')
    file.write("0")

os.system("Python Main.py")