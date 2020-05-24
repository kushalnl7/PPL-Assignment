
from tkinter import *
from tkinter import ttk, colorchooser, filedialog, messagebox
import tkinter.messagebox
import PIL.ImageGrab as ImageGrab

class main:

    def __init__(self, master):
        self.master = master
        self.penwidth = 5
        self.color_bg = 'white'
        self.color_fg = 'black'
        self.drawwidgets()
        self.setup()
        self.c.bind('<B1-Motion>', self.paint)  # drwaing the line
        self.c.bind('<ButtonRelease-1>', self.reset)

    def changeW(self, e):
        self.penwidth = e

    def clear(self):
        self.c.delete(ALL)

    def paint(self, e):
        paint_color = self.color_bg if self.eraser_on else self.color_fg
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y,
                               width=self.penwidth, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = e.x
        self.old_y = e.y

    def erase(self):
        self.activate_button(self.eraser, eraser_mode=True)

    def penf(self):
        self.activate_button(self.pen)

    def reset(self, e):  # reseting or cleaning the canvas
        self.old_x = None
        self.old_y = None

    def change_fg(self):  # changing the pen color
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  # changing the background color canvas
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
        self.clear()

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def msg(self):
        tkinter.messagebox.showinfo(
            'About Paint Application', 'This is a paint aplication which provides you with features such as changing background and brush colors. It also provides you with a slider to change pen width.')

    def about(self):
        tkinter.messagebox.showinfo(
            "Paint Application Developer", "Kushal Nitin Lahoti                                                                         MIS :- 111803179")

    def save_it(self):

        try:
            filename = filedialog.asksaveasfilename(defaultextension='.jpg')
            ImageGrab.grab().save(filename)
            messagebox.showinfo('Paint says', 'image is saved as ' + str(filename))

        except:
            messagebox.showerror('Paint says', 'unable to save image, \n something went wrong')

    def save_it_destroy(self):

        try:
            filename = filedialog.asksaveasfilename(defaultextension='.jpg')
            ImageGrab.grab().save(filename)
            messagebox.showinfo('Paint says', 'image is saved as ' + str(filename))
            self.root.destroy()

        except:
            messagebox.showerror('Paint says', 'unable to save image, \n something went wrong')

    def drawwidgets(self):
        self.controls = Frame(self.master, height=1000, width=140)
        self.label = Label(self.controls, text='Width',font=('Times 15'), fg='red')
        self.label.place(x=10, y=280)
        self.slider = ttk.Scale(self.controls, from_=5,to=100, command=self.changeW, orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.place(x=80, y=250)
        self.controls.pack(side=LEFT)
        self.pen = Button(self.controls, text='Pen',font=('Times 12'), command=self.penf)
        self.pen.place(x=15, y=200)
        self.eraser = Button(self.controls, text='Eraser',font=('Times 12'), command=self.erase)
        self.eraser.place(x=75, y=200)
        self.c = Canvas(self.master, width=500, height=400, bg=self.color_bg)
        self.c.pack(fill=BOTH, expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        filemenu = Menu(menu, tearoff = 0)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Save', command=self.save_it)
        filemenu.add_command(label='Save and Exit', command=self.save_it_destroy)

        color = Menu(menu, tearoff=0)
        menu.add_cascade(label='Colors', menu=color)
        color.add_command(label='Brush Color', command=self.change_fg)
        color.add_command(label='Background Color', command=self.change_bg)

        option = Menu(menu, tearoff=0)
        menu.add_cascade(label='Options', menu=option)
        option.add_command(label='Clear Canvas', command=self.clear)
        option.add_command(label='Exit', command=self.master.destroy)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        #help_option.add_command(label="Features", command=self.features_msg)
        help_option.add_command(label="About Paint Application", command=self.msg)
        help_option.add_command(label="Develpoers", command=self.about)

    def setup(self):

        self.old_x = None
        self.old_y = None
        self.eraser_on = False
        self.active_button = self.pen


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.geometry('900x600')
    root.title('Paint Application')
    root.mainloop()


