import tkinter as tk
import winsound

main = tk.Tk()
main.iconbitmap("files\\skull2.ico")
main.title("💀")
img = tk.PhotoImage(file = "files\\dead.png")
label = tk.Label(main, image=img).pack()
winsound.PlaySound('files\\riff.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
main.mainloop()