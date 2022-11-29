import tkinter as tk
import math

class CalcGui(object):
    def __init__(self, app=None):
        app.title('calculator') 
        app.geometry('300x500') 

def main():
    app = tk.Tk()
    CalcGui(app)
    app.mainloop()
    
    
if __name__ == "__main__":
    main()