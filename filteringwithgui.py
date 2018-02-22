from PIL import ImageTk
import PIL.Image, PIL.ImageOps
from Tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Image Inversion")
        self.pack(fill=BOTH, expand=2)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file=Menu(menu)
        file.add_command(label='exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit=Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        # edit.add_cascade(label='Show Text', command=self.showText)
        menu.add_cascade(label='Edit', menu=edit)

    def showImg(self):
        # load = PIL.Image.open('image1.jpg')
        # render1 = ImageTk.PhotoImage(load)
        # invimg = PIL.ImageOps(load)
        invimg = PIL.ImageOps.invert('image1.jpg')
        # invimg.save('new-image.jpg')
        # invimg.show('new-image.jpg')
        render = ImageTk.PhotoImage(invimg)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=10)

    # def showInvImg(self):
    #
    #     invimg = PIL.ImageOps()
    #     invimg.save('new-img.jpg')
    def client_exit(self):
        exit()

root = Tk()
root.geometry("640x480")
app = Window(root)
root.mainloop()





# img = Image.open('image1.jpg')
# inverted_image = PIL.ImageOps.invert(img)
# inverted_image.save('new-img.jpg')