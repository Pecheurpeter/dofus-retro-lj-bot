import tkinter as tk 
from tkinter import filedialog, Text
import os
import pyautogui
import threading
import functools as ft

root = tk.Tk()            # kind like main framework
apps = []                 # apps is a list to store app paths in
count_ss_naming = 0

if os.path.isfile('save.txt'):                  # if there is a file called save.txt    
    with open('save.txt', 'r') as f:                #open save txt file as read
        tempApps = f.read()                             #tempsApps is the content the save.txt file
        tempApps = tempApps.split(',')                  #we split the content(paths of the apps) by comma
        apps = [x for x in tempApps if x.strip()]       #we create a list called apps with the paths of apps if path is not an empty string

def takeSS(): 
    ss = pyautogui.screenshot()
    
    ss.save(f"SS {count_ss_naming}.png")

    global count_ss_naming
    count_ss_naming += 1

   



# def runApps():
#     for app in apps:
#         os.startfile(app)

canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42")  #creating a canvas and attaching it to root
canvas.pack()

frame = tk.Frame(root, bg = "white")                                 #creating a frame on canvas
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)   #adjusting the placement of the frame

openFile = tk.Button(root, text = "take SS", padx = 10, pady = 5, fg ="white", bg = "#263D42", command = takeSS)   #creating a "Open File" Button
openFile.pack()

# runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg ="white", bg = "#263D42", command = runApps)    #creating a "Run Apps" Button
# runApps.pack()



for app in apps:                # for each element of apps
    label = tk.Label(frame , text=app)     # create a label 
    label.pack()
    
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')