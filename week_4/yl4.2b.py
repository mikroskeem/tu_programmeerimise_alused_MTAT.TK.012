from tkinter import Canvas, Tk

root = Tk()
root.title("Liiklusmärk")

canvas = Canvas(root, width = 500, height = 500, background = "White")
canvas.pack()

box = canvas.create_rectangle(10, 10, 490, 490, fill = "Blue")
arrow = canvas.create_polygon(200, 450, 300, 450, 300, 250, 400, 250, 250, 50, 100, 250, 200, 250, 200, 450, fill = "White")

root.mainloop()
