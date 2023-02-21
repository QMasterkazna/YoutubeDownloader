import tkinter.filedialog as fd
from tkinter import *
from tkinter import ttk

from pytube import YouTube

import os

import json

def clear():
    errmg2.set("Очищено")
    entry.delete(0, END)


def Download():
    video = entry.get()
    with open('path.json', 'r', encoding='utf-8') as file:
        Pathfile = json.load(file)
    if video:
        try:
            yt = YouTube(video)
            file = yt.streams.get_lowest_resolution()
            oputh = (f"{Pathfile}")
            file.download(oputh)
            print("успешно")
            errmg.set("Entry link pls:>")
            errmg2.set(f"Successfully {yt.title}")
            clear()
        except:
            print(Pathfile)
            errmg2.set("Не указан путь. "+"Или файл уже есть в этой папке")
    else:
        errmg2.set("Поле ввода ссылки пустое")
        print("Empty")

def DownloadMP3():
    video = entry.get()
    with open('path.json', 'r', encoding='utf-8') as file:
        Pathfile = json.load(file)
    if video:
        try:
            yt = YouTube(video)
            file = yt.streams.filter(only_audio=True).first()
            oputh = (f"{Pathfile}")
            out_file = file.download(output_path=oputh)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            errmg2.set(f"Successfully {yt.title}")
        except:
            print(Pathfile)
            errmg2.set("Не указан путь. "+"Или файл уже есть в этой папке")
    else:
        errmg2.set("Поле ввода ссылки пустое")
        print("Empty")

def choose():
    global directory
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    with open("path.json", 'w',encoding='utf-8' ) as file:
        json.dump(directory, file, ensure_ascii=False)
    with open('path.json', 'r', encoding='utf-8') as rfile:
        Pathfile = json.load(rfile)
    directory_choose.set(Pathfile)

with open('path.json','r', encoding='utf-8') as PathtoReadFile:
    pathToSave = json.load(PathtoReadFile)


root = Tk()
root.title("Youtube Downloader :>")
root.geometry("1400x400")

root.resizable(width=False, height=False)

bg = PhotoImage(file="897-989.png")
my_label = Label(root, image=bg)
my_label.place(x=0,y=0, relwidth=1, relheight=1)

errmg2 = StringVar()
errmg2.set("First job")
successfully_label = ttk.Label(foreground="red", textvariable=errmg2, wraplength=250)
successfully_label.pack(padx=5, pady=5, anchor=NW)

errmg = StringVar()
errmg.set("Hello entry link pls:>")
successfully_label = ttk.Label(foreground="green", textvariable=errmg, wraplength=250)
successfully_label.pack(padx=5, pady=5, anchor=NW)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
btn = ttk.Button(text="Download", command=Download)
btn.pack(anchor=NW, padx=6, pady=6)

btn_mp3= ttk.Button(text="Download MP3", command=DownloadMP3)
btn_mp3.pack(anchor=NW, padx=6, pady=6)

directory_choose = StringVar()
directory_choose.set(pathToSave)
directory_choose_label = ttk.Label(foreground="green", textvariable=directory_choose, wraplength=250)
directory_choose_label.pack(padx=3, pady=3, anchor=NW)

btn_dir = ttk.Button(text="Choose directory", command=choose)
btn_dir.pack(anchor=NW, padx=6, pady=6)

clear_btn = ttk.Button(text="Clear", command=clear)
clear_btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
