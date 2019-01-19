import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="CLICK ME",fg="red",command= lambda: print("u gay"))
button.pack(side=tk.LEFT)
root.mainloop()