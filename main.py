import tkinter as tk

def main():
    page = tk.Tk()
    
    frame1 = tk.Frame(master=page, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    frame2 = tk.Frame(master=page, width=100, bg="yellow")
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    frame3 = tk.Frame(master=page, width=50, bg="blue")
    frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    page.mainloop()
    
