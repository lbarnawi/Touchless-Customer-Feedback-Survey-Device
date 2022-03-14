from tkinter import *
from PIL import ImageTk
import threading
from FingerCounter import *
import time
from PIL import Image

root = Tk()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.attributes('-fullscreen', True)

frame = Frame(root)

# Define the images
Img = ImageTk.PhotoImage(Image.open("Up.png"))
Img1 = ImageTk.PhotoImage(Image.open("Down.png"))
Img2 = ImageTk.PhotoImage(Image.open("Wave.png"))
Img3 = ImageTk.PhotoImage(Image.open("white.png"))
#
ImgLabel00 = Label(root, text="   \n \n \n \n  ")
ImgLabel00.grid(row=0, column=0, padx=5, pady=5)


def readingFun():
    while True:
        # This section is for Satisfied
        with open("okSat.txt", "r") as fSat:
            last_line = fSat.readlines()
            if "ok" in last_line:
                ImgLabel3 = Label(image=Img3)
                ImgLabel3.grid(row=1, column=2, padx=5, pady=5)
                time.sleep(0.4)
                ImgLabel = Label(image=Img)
                ImgLabel.grid(row=1, column=2, padx=5, pady=5)
                with open("okSat.txt", 'r+') as fSat:
                    fSat.truncate(0)
                    fSat.close()
            else:
                ImgLabel = Label(image=Img)
                ImgLabel.grid(row=1, column=2, padx=5, pady=5)
        # This section is for Neutral
        with open("okNeut.txt", "r") as fNeut:
            last_line = fNeut.readlines()
            if "ok" in last_line:
                ImgLabel3 = Label(image=Img3)
                ImgLabel3.grid(row=1, column=1, padx=5, pady=5)
                time.sleep(0.4)
                ImgLabel2 = Label(image=Img2)
                ImgLabel2.grid(row=1, column=1, padx=5, pady=5)
                with open("okNeut.txt", 'r+') as fNeut:
                    fNeut.truncate(0)
                    fNeut.close()
            else:
                ImgLabel2 = Label(image=Img2)
                ImgLabel2.grid(row=1, column=1, padx=5, pady=5)
        # This section is for Neutral
        with open("okUnsat.txt", "r") as fUnsat:
            last_line = fUnsat.readlines()
            if "ok" in last_line:
                ImgLabel3 = Label(image=Img3)
                ImgLabel3.grid(row=1, column=0, padx=5, pady=5)
                time.sleep(0.4)
                ImgLabel1 = Label(image=Img1)
                ImgLabel1.grid(row=1, column=0, padx=5, pady=5)
                with open("okUnsat.txt", 'r+') as fUnsat:
                    fUnsat.truncate(0)
                    fUnsat.close()
            else:
                ImgLabel1 = Label(image=Img1)
                ImgLabel1.grid(row=1, column=0, padx=5, pady=5)


# craeting a label widget
ImgLabel00 = Label(root, text="   \n \n \n \n \n \n \n \n \n \n  ")
ImgLabel00.grid(row=5, column=1, padx=5, pady=5)
myLabel = Label(root, text="ما مدى رضاك عن الخدمة المقدمة؟", font=("Arial", 45))
myLabel.grid(row=6, column=1)

myLabel = Label(root, text="غير راض", font=("Arial", 45))
myLabel.grid(row=3, column=0)
myLabel0 = Label(root, text="Unsatisfied", font=("Arial", 45))
myLabel0.grid(row=4, column=0)

myLabel2 = Label(root, text="محايد", font=("Arial", 45))
myLabel2.grid(row=3, column=1)
myLabel20 = Label(root, text="Neutral", font=("Arial", 45))
myLabel20.grid(row=4, column=1)

myLabel4 = Label(root, text="راض", font=("Arial", 45))
myLabel4.grid(row=3, column=2)
myLabel40 = Label(root, text="Satisfied", font=("Arial", 45))
myLabel40.grid(row=4, column=2)

# shoving it into the screen


threading.Thread(target=fcf).start()
threading.Thread(target=readingFun).start()

root.mainloop()
