from string import ascii_uppercase
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from playsound import playsound

def music():
    while True:
        playsound('music.mp3')

Thread(target=music, daemon=True).start()



from PIL import  Image, ImageSequence, ImageTk

def keygen(block1: str):
    if len(block1)!= 5 or block1.isalpha() == False:
        return ''
    block1=block1.upper()
    text=ascii_uppercase*2
    block2=''
    block3=''
    for i in block1:
        block2+=text[text.find(i)+3]
        block3 += text[text.find(i) - 5]
    return f'{block1}-{block2}-{block3}'


def on_button():
    text = form.get()
    key = keygen(text)
    if key=='':
        messagebox.showerror(title='Input error', message='Incorrect format')
        return None
    key_label.configure(text=key)
    return None


window = tk.Tk()
window.title('UndertaleKeyGen')
window.configure(background='black')
window.geometry('500x500')
window.resizable(0,0)


head=tk.Label(window, text='UNDERTALE KeyGen', font='ComicSansMS 36', fg='white', bg='black')

key_comm = tk.Label(window, text='Here is your key:', font='ComicSansMS 12', fg='white', bg='black')
key_label = tk.Label(window, text='XXXXX-XXXXX-XXXXX', font='ComicSansMS 40', fg='white', bg='black')

form_comm = tk.Label(window, text='Enter fragment (5 letters):', font='ComicSansMS 12', fg='white', bg='black')
form = tk.Entry(window, width=5, font='ComicSansMS 24')

submit_btn = tk.Button(window, command=on_button, text='Generate', font='ComicSansMS 24')

head.place(relx=0.5, rely=0.1, anchor='center')
key_comm.place(relx=0.05, rely=0.3, anchor='sw')
key_label.place(relx=0.5, rely=0.37, anchor='center')
form_comm.place(relx=0.05, rely=0.5, anchor='sw')
form.place(relx=0.05, rely=0.6, anchor='sw')
submit_btn.place(relx=0.3, rely=0.6, anchor='sw')

#gif

gif_label = tk.Label(window, bd=0)
gif_label.place(relx=0.5, rely=0.8, anchor='center')
im = Image.open('sans.gif')


frames = []
durations = []
while True:

    for frame in ImageSequence.Iterator(im):
        frame_rgba = frame.convert('RGBA')
        orig_w, orig_h = im.size
        scale=0.5
        resized = frame_rgba.resize((int(orig_w*scale), int(orig_h*scale)))
        frames.append(ImageTk.PhotoImage(resized))

        durations.append(frame.info['duration'])
    break



def animation(current_frame=0):
    gif_label.configure(image=frames[current_frame])
    next_frame = (current_frame + 1) % len(frames)
    window.after(durations[current_frame], lambda: animation(next_frame))



animation()



window.mainloop()
