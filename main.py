from tkinter import *
#from tkinter.ttk import *
from random import  randint
from time import sleep

def moving(item):
    global moved, x, y, v
    flag = True
    #print(box.coords(item)[0])
    for e in cars_l:

        if e != item:

            if cars[cars_l.index(item)][0] == 0:

                if  (0 < box.coords(item)[0] - box.coords(e)[0] <=90) and (box.coords(e)[1] == box.coords(item)[1]) and (0 <box.coords(item)[0]< screen[0]+ 3) and (0 < box.coords(e)[0]< screen[0]+ 3 ):
                    #pass
                    flag = False
            elif cars[cars_l.index(item)][0] == 1:
                if (0 < box.coords(item)[1] - box.coords(e)[1] <= 90) and (box.coords(e)[0] == box.coords(item)[0]) and (0 < box.coords(item)[1]<screen[1]+ 66) and (0 < box.coords(e)[1]<screen[1] + 65):
                    #pass
                    flag = False
            elif cars[cars_l.index(item)][0] == 2:
                if (0 < box.coords(e)[1] -box.coords(item)[1]  <= 90) and (box.coords(e)[0] == box.coords(item)[0]) and (-65 < box.coords(item)[1]<screen[1] ) and (-65 < box.coords(e)[1]<screen[1] ):
                   #pass
                    flag = False

    if cars[cars_l.index(item)][0] == 0:
        x[cars_l.index(item)]=-3
        y[cars_l.index(item)]=0

        if 0 <= box.coords(item)[0] - stop2 <= 5:
            if lights[0] == 0 or lights[0] == 1:
                flag = False
        elif 299 <=  box.coords(item)[0] <= 301:
            if cars[cars_l.index(item)][1] == 0:
                box.itemconfig(item, image=car_up)
                x[cars_l.index(item)]=0
                y[cars_l.index(item)]=-3
        elif  box.coords(item)[0] == 202:
            if cars[cars_l.index(item)][1] == 1:
                box.itemconfig(item, image=car_down)
                x[cars_l.index(item)] = 0
                y[cars_l.index(item)] = 3
    elif cars[cars_l.index(item)][0] == 1:
        x[cars_l.index(item)] = 0
        y[cars_l.index(item)] = -3
        if 0 <= box.coords(item)[1] - stop3 <= 5:
            if lights[0] == 2 or lights[0] == 1:
                flag = False
        elif 449 <= box.coords(item)[1] <= 450:
            if cars[cars_l.index(item)][1] == 1:
                box.itemconfig(item, image=car_right)
                x[cars_l.index(item)] = 3
                y[cars_l.index(item)] = 0

    elif cars[cars_l.index(item)][0] == 2:
        x[cars_l.index(item)] = 0
        y[cars_l.index(item)] = 3
        if 0 <= stop1 - box.coords(item)[1] <= 5:
            if lights[0] == 2 or lights[0] == 1:
                flag = False

    '''if flag:
        if cars[cars_l.index(item)] == 0:
            box.move(item, -randint(2,3), 0)
        elif cars[cars_l.index(item)] == 1:
            box.move(item, 0,-randint(2, 3))''' # старое движение


    if cars[cars_l.index(item)][0] == 0 and (box.coords(item)[1] > 65 + screen[1] or box.coords(item)[1] < -65):
        #box.delete(item)
        v = item

        #cars_l.pop(v)
        #cars.pop(v)
        #x.pop(v)
        #y.pop(v)
        cars[cars_l.index(item)][0] = randint(0, 2)
        cars[cars_l.index(item)][1] = randint(0, 1)

        #cars.append([randint(0, 2), randint(0, 1)])
        again(v)
        #win.after(0, gen)
    elif cars[cars_l.index(item)][0] == 1 and (box.coords(item)[1] < -65 or box.coords(item)[0] > 65 + screen[0]):
        #box.delete(item)

        v = item
        #cars_l.pop(v)
        #cars.pop(v)
        #x.pop(v)
        #y.pop(v)
        #cars.append([randint(0, 2), randint(0, 1)])
        cars[cars_l.index(item)][0] = randint(0, 2)
        cars[cars_l.index(item)][1] = randint(0, 1)
        again(v)
        #win.after(100, gen)
    elif cars[cars_l.index(item)][0] == 2 and (box.coords(item)[1] > 65 + screen[1]):
        #box.delete(item)
        v = item
        #cars_l.pop(v)
        #cars.pop(v)
        #x.pop(v)
        #y.pop(v)
        cars[cars_l.index(item)][0] = randint(0, 2)
        cars[cars_l.index(item)][1] = randint(0, 1)
        again(v)
        #ness += 1
        #win.after(100, gen)



    else: # появление новых машин

        win.after(10,lambda: moving(item))
    if flag:
        #print(x, y)
        box.move(item, x[cars_l.index(item)], y[cars_l.index(item)])

    '''if box.coords(item)[0] < -64 or box.coords(item)[0] > screen[0]+64 or box.coords(item)[1] > screen[1]+64 or box.coords(item)[1] < -64:
        box.delete(item)
        v = cars_l.index(item)
        cars_l.pop(v)
        cars.pop(v)
        cars.append( [randint(0, 2), randint(0,1)])
        print(cars)


        win.after(1,gen)''' # старое обновление


def again(n_car):

    if cars[cars_l.index(n_car)][0] == 0:
        box.coords(n_car, screen[0], 340)
        box.itemconfig(n_car, image=car_left)
    elif cars[cars_l.index(n_car)][0] == 1:
        box.coords(n_car, 300, screen[1])
        box.itemconfig(n_car, image=car_up)
    elif cars[cars_l.index(n_car)][0] == 2:
        box.coords(n_car, 202, -65)
        box.itemconfig(n_car, image=car_down)
    moving(n_car)


def gen():
    global j
    #cars.append(randint(0, 1))
    try:
        if cars[j][0] == 0:
            cars_l.append(box.create_image(screen[0], 340, anchor='nw', image=car_left))
        elif cars[j][0] == 1:
            cars_l.append(box.create_image(300, screen[1], anchor='nw', image=car_up))
        elif cars[j][0] == 2:
            cars_l.append(box.create_image(202, -65, anchor='nw', image=car_down))
        # win.after(100,  moving(cars_l[j]))
        #print(cars, cars_l)
        moving(cars_l[j])
        if j < len(cars) - 1:
            j += 1  # старое
            win.after(1000, gen)
    except IndexError:

        pass
        #gen()
        #if j < len(cars) - 1:
        #    j += 1  # старое
        #    win.after(1000, gen)
           # print('error')
           # moving(cars_l[j-1])
           # if j < len(cars) - 1:
           #     j += 1  # старое
           #     win.after(1000, gen)
        #j+=1



def light_updating():
    global color_now
    '''if lights[0] == 0:
        box.itemconfig(trl, fill='red')
        lights[0] = colors[1]
        win.after(3000, light_updating)
    elif lights[0] == 1:
        box.itemconfig(trl, fill='yellow')
        win.after(500, light_updating)
        lights[0]
    elif lights[0] == 1:
        box.itemconfig(trl, fill='green')
        lights[0] = 0
        win.after(3000, light_updating)
    #win.after(3000, light_updating)''' #старые светофоры
    next_color()
    box.itemconfig(trl, image=color[lights[0]])
    box.itemconfig(trl3, image=color[lights[0]])
    box.itemconfig(trl2, image=color[lights[1]])
    box.itemconfig(trl4, image=color[lights[1]])
    if lights[0] == 0 or lights[0] == 2:

        win.after(2000, light_updating)
    elif lights[0] == 1:

        win.after(800, light_updating)

def next_color():
    global color_prev, lights
    for i in range(len(lights)):
        if lights[i] == 0:
            lights[i] = 1
            color_prev[i] = 0
        elif lights[i] == 1:
            if color_prev[i] == 0:
                lights[i] = 2
            if color_prev[i] == 2:
                lights[i] = 0
        elif lights[i] == 2:
            color_prev[i] = 2
            lights[i] = 1

'''def new_car():
    global ness
    cars.pop(delete[len(delete)-1-ness])
    cars_l.pop(delete[len(delete)-1-ness])
    x.pop(delete[len(delete)-1-ness])
    y.pop(delete[len(delete)-1-ness])
    cars.append([randint(0, 2), randint(0,1)])
    x.append(0)
    y.append(0)
    gen()
    if ness > 0:
        ness -=1
        win.after(500,new_car)
    #win.after(2000, new_car)'''

def init():
    light_updating()
    am = int(scale.get())
    for i in range(am):
        cars.append([randint(0, 2), randint(0, 1)])
        x.append(0)
        y.append(0)
    win.after(500, gen)
    but.config(state=DISABLED)
    scale.config(state=DISABLED)
    win.focus()

moved = 300
lights = [0,2]
cars = []
cars_l = []
x = []
y = []
car_amount = 3
j=0
color_num = [0, 1, 2]
#color = ['red', 'yellow', 'green']
color_prev = [0,2]
screen = (1000, 750)

ness = 0
delete = []

stop1 = 200
stop2 = 440
stop3 = 530


win = Tk()
win.geometry('1000x850+0+0')
win.title('Crossroads by Leontev Aleksey 2022')
win.resizable(False, False)
car_left = PhotoImage(file='cont/car_left.png')
car_right = PhotoImage(file='cont/car_right.png')
car_up = PhotoImage(file='cont/car_up.png')
car_down = PhotoImage(file='cont/car_down.png')
background = PhotoImage(file='cont/background.png')
tl0 = PhotoImage(file='cont/trl_red.png')
tl1 = PhotoImage(file='cont/trl_yellow.png')
tl2 = PhotoImage(file='cont/trl_green.png')
color = [tl0, tl1, tl2]

box = Canvas(win, width=screen[0], height=screen[1])
but = Button(win, text='Start', command=init)
scale = Scale(win, orient='horizontal',  from_=6, to=20)
scale.set(10)
box.create_image(0,0,anchor='nw', image=background)


#trl = box.create_rectangle(300, 350, 350, 390)
trl = box.create_image(420, 200, anchor='nw', image=tl0)
trl2 = box.create_image(420, 500, anchor='nw', image=tl0)
trl3 = box.create_image(130, 350, anchor='nw', image=tl0)
trl4 = box.create_image(130, 200, anchor='nw', image=tl0)

#cars.append(box.create_image(200, 200, anchor='nw', image=car))




#win.after(2000, new_car)
box.grid(row=0, column=0, columnspan=2)
Label(text='Количество машин').grid(row=1, column=0, sticky=E, padx=10)
scale.grid(row=1, column=1, sticky=W)

but.grid(row=2, column=0, columnspan=2, pady = 15, stick='wens', padx=400)
#win.after(100, moving)

mainloop()