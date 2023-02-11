import tkinter.filedialog as fd
from tkinter import *
from tkinter import ttk

from pytube import YouTube


def clear():
    entry.delete(0, END)


def Download():
    video = entry.get()
    if video:
        yt = YouTube(video)
        file = yt.streams.get_lowest_resolution()
        oputh = (f"{directory}")
        file.download(oputh)
        print("успешно")
        errmg.set("Entry link pls:>")
        errmg2.set("Successfully")
    else:
        print("Empty")


def choose():
    global directory
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    directory_choose.set(directory)


root = Tk()
root.title("Youtube Downloader :>")
root.geometry("1400x400")

bg = PhotoImage(file="897-989.png")
my_label = Label(root, image=bg)
my_label.place(x=0,y=0, relwidth=1, relheight=1)

errmg2 = StringVar()
errmg2.set("First job")
successfully_label = ttk.Label(foreground="green", textvariable=errmg2, wraplength=250)
successfully_label.pack(padx=5, pady=5, anchor=NW)

errmg = StringVar()
errmg.set("Hello entry link pls:>")
successfully_label = ttk.Label(foreground="green", textvariable=errmg, wraplength=250)
successfully_label.pack(padx=5, pady=5, anchor=NW)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
btn = ttk.Button(text="Click", command=Download)
btn.pack(anchor=NW, padx=6, pady=6)

directory_choose = StringVar()
directory_choose.set("Nothing")
directory_choose_label = ttk.Label(foreground="green", textvariable=directory_choose, wraplength=250)
directory_choose_label.pack(padx=3, pady=3, anchor=NW)

btn_dir = ttk.Button(text="Choose directory", command=choose)
btn_dir.pack(anchor=NW, padx=6, pady=6)

clear_btn = ttk.Button(text="Clear", command=clear)
clear_btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
