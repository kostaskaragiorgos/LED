""" Led Control Panel"""
from socket import timeout
from tkinter import Menu, Button, messagebox as msg, Tk, Label, END
from tkinter import Text
import time
import serial

def helpmenu():
    """help menu function"""
    msg.showinfo("HELP", "")

def aboutmenu():
    """about menu function"""
    msg.showinfo("About", "LED CONTROL PANEL\nVersion 1.0")

class LedControlPannel():
    def __init__(self, master):
        self.master = master
        self.master.title("LED CONTROL PANEL")
        self.master.geometry("250x250")
        self.master.resizable(False, False)
        self.ser = serial.Serial('COM3', 9600, timeout=1)


       

        self.findbutton = Button(self.master, text="LED ON", command=self.turnon)
        self.findbutton.pack()

        self.clearbutton = Button(self.master, text="LED OFF", command=self.turnoff)
        self.clearbutton.pack()

        self.menu = Menu(self.master)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)

       

        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)

        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())


    def turnon(self):
        pac = self.ser.readline()
        if (pac.decode('utf').rstrip('\n') == "1"):
            msg.showerror("ERROR","The led is already on!!!")
        self.ser.write(b'H')

    def turnoff(self):
        pac = self.ser.readline()
        if (pac.decode('utf').rstrip('\n') == "0"):
            msg.showerror("ERROR","The led is already off!!!")
        self.ser.write(b'L')

    
    def exitmenu(self):
        """exit menu function"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    



def main():
    """main functionn"""
    root = Tk()
    LedControlPannel(root)
    root.mainloop()

if __name__ == '__main__':
    main()