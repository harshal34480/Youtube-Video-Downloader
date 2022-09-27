# import library gui and download youtube vidios
from tkinter import *
from pytube import YouTube

# create display windowv or interface
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Easy youtube vidio downloader")

Label(root,text = 'Youtube Vidio Downloader', font = "arial 20 bold").pack()

# create feild to enter the link
link = StringVar()

Label(root, text='Paste Link Here:', font = 'arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width = 70,textvariable = link).place(x=32, y=90)

# create the function to start downloading
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font ='arial 15').place(x=180, y=150)

Button(root,text = 'DOWNLOAD', font='arial 15 bold', bg='pale violet red',padx= 2,command = Downloader).place(x=180, y=150)
root.mainloop()