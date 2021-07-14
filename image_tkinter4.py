import tkinter as tk
from PIL import Image, ImageTk

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new('RGB', (500, 500), "white")  # create a new white image

window = tk.Tk()
canvas = tk.Canvas(window, width=img.size[0], height=img.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(img)
canvas.create_image(img.size[0] // 2, img.size[1] // 2, image=image_tk)


def mouseClick(event):
    x, y = event.x, event.y
    print("x: {}, y: {}".format(x, y))
    # Update image
    img.putpixel((x, y), (255, 0, 0))
    # Update screen
    canvas.create_oval(x, y, x, y, width=0, fill='red')


canvas.bind("<Button-1>", mouseClick)

window.mainloop()
