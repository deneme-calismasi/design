from tkinter import *

root = Tk()
root.title('Rectangle Test')
canvas = Canvas(root, width=300, height=300)

## top_left_x, top_left_y, bottom_right_x, bottom_right_y
points_list = [0, 0, 25, 25]
color = "red"

for row in range(3):
    for col in range(3):
        rectang = canvas.create_rectangle(points_list[0], points_list[1], \
                                          points_list[2], points_list[3], fill=color)
        ## increase along the x axis
        for point in [0, 2]:
            points_list[point] += 50

    ## move down one row
    if row % 2:  ## row is an odd number
        points_list = [0, points_list[1] + 25, 25, points_list[3] + 25]
    else:  ## row is an even number
        points_list = [25, points_list[1] + 25, 50, points_list[3] + 25]

canvas.pack()
root.mainloop()
