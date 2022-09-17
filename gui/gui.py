import tkinter as tk
from Jarvis.utils.BaseFunctionality import listen, get_location


def create_gui():
    root = tk.Tk()
    root.title('Jarvis')
    canvas = tk.Canvas(root, height=600, width=900, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)  # adding a frame on the outside
    get_location()
    listening_button = tk.Button(root, text='Im here', padx=10, pady=5, fg='white', bg='#263D42', command=listen)
    listening_button.pack()
    root.mainloop()
