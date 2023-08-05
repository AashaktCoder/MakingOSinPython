# This would be a single user single task operating system made using tkinter module of python and would have a gui interface and features such as file handling, image manipulation, video recording, camera etc.

from tkinter import *

class MainWindow:
    def __init__(self):
        self.WIN = Tk()

        self.LoginNameVal = StringVar()
        self.LoginPassVal = StringVar()

    def Booting(self):
        self.WIN.title("Panda OS")
        icon = PhotoImage(file="Images\\Icons\\PandaIcon.png")
        self.WIN.iconphoto(False, icon)
        self.WIN.geometry("400x400")
        self.WIN.maxsize(400, 400)
        self.WIN.minsize(400, 400)

    def Login(self):
        with open("Other\\LoginInfo.txt", 'r') as f:
            for i in f.readlines():
                InfoList = eval(i)

                if InfoList[0] == self.LoginNameVal.get():
                    if InfoList[1] == self.LoginPassVal.get():
                        print("YOU LOGGED IN!!!!!!!!!!")

    def MakeWidgets(self):
        self.LoginScreen = Canvas(self.WIN)
        self.LoginTitle = Label(self.LoginScreen, text="Welcome to Panda OS", font="Aerial 40", wraplength=400)

        self.LoginTitleName = Label(self.LoginScreen, text="Name: ", font="Aerial 30")
        self.LoginNameInput = Entry(self.LoginScreen, font="Aerial 25", width=14, textvariable=self.LoginNameVal)

        self.LoginTitlePass = Label(self.LoginScreen, text="Password:", font="Aerial 25")
        self.LoginPassInput = Entry(self.LoginScreen, font="Aerial 25", width=12, textvariable=self.LoginPassVal)

        self.LoginButton = Button(self.LoginScreen, text="Login", font="Aerial 24", command=self.Login)
    
    def PlaceWidgets(self):
        self.LoginScreen.pack(side=LEFT, fill=BOTH, expand=True)
        self.LoginTitle.place(x=50,y=0)

        self.LoginTitleName.place(x=5, y=170)
        self.LoginNameInput.place(x=135, y=175)

        self.LoginTitlePass.place(x=5, y=235)
        self.LoginPassInput.place(x=170, y=235)
        self.LoginButton.place(x=145, y=300)

    def Update(self):
        self.Booting()
        self.MakeWidgets()
        self.PlaceWidgets()
        self.WIN.mainloop()

newWindow = MainWindow()
newWindow.Update()