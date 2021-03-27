from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *


file_size = 0

def Download():
    global file_size
    try:
        #Getting the url
        url = url_textfield.get()
        #Changing the button text and disabling it
        button.config(text="Please Wait...")
        button.config(state=DISABLED)
        #Ask the directory to store the video
        save_video = askdirectory()
        if save_video is None:
            return
        #Creating a object for YouTube
        ob = YouTube(url)
        #Assigning the highest resolution eg: "720p"
        stream = ob.streams.get_highest_resolution()
        #Getting the filesize
        file_size = stream.filesize
        #Setting the title of the video
        title.config(text=stream.title)
        title.pack(side = TOP)
        #Downloading the video
        stream.download(save_video)
        print("Done...")
        #Making the button normal and adjusting the text
        button.config(state=NORMAL)
        button.config(text="Start Download")
        showinfo("Downloaded","Downloaded Successfully")
        #Making the TextField disappear
        url_textfield.delete(0,END)
        title.pack_forget()

    except Exception as e:
        print(e)
        print("Error !!!")


#Starting GUI
m = Tk()
#Setting the title of the window
m.title("Youtube Downloader")
#Setting the geometry of the window
m.geometry("500x600")
#Setting the icon
m.iconbitmap('youtube_downloader_icon.ico')
#Heading icon
file = PhotoImage(file="youtube_downloader_icon(1).png")
image = Label(m,image=file)
image.pack(side=TOP,pady=10)
#URL TextField
url_textfield = Entry(m,font=('verdana',16),justify=CENTER)
url_textfield.pack(side=TOP,fill=X,padx=20)
#Button
button = Button(m,text="Start Download",font=("verdana",12),relief="ridge",command=Download)
button.pack(side=TOP,pady=20)
#Video Title
title = Label(m,font=("verdana",8),text="Video Title",justify=CENTER)
#Background color
m.configure(bg='gainsboro')
#Running the window
m.mainloop()

