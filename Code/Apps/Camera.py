from tkinter import *
from cv2 import VideoCapture, imshow, waitKey, destroyWindow, imwrite

class Camera:
    def __init__(self, WIN, AppListCanvas):
        self.WIN = WIN
        self.AppListCanvas = AppListCanvas

    def GoBack(self):
        self.CameraCanvas.pack_forget()
        self.AppListCanvas.pack(side=LEFT, fill=BOTH, expand=True)

    def TurnOnCamera(self):
        cam = VideoCapture(0)
        result, image = cam.read()

        if result:
            imshow("Camera Window", image)

            k = waitKey(0)
            if k == ord('q'):
                destroyWindow("Camera Window")
            
            imwrite("newImg.png", image)

    def MakeWidget(self):
        self.CameraCanvas = Canvas(self.WIN)

        self.Title = Label(self.CameraCanvas, text="Camera", font="Aerial 35")

        self.BackButton = Button(self.CameraCanvas, text="Back", font="Aerial 20", command=self.GoBack)

        self.TurnOnB = Button(self.CameraCanvas, text="Turn On", font="Aerial 20", command=self.TurnOnCamera)

    def PlaceWidget(self):
        self.CameraCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.Title.place(x=100, y=0)
        self.BackButton.place(x=5, y=340)

        self.TurnOnB.place(x=120, y=90)

    def Update(self):
        self.MakeWidget()
        self.PlaceWidget()