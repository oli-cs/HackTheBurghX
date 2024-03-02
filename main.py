import tkinter as tk

def main():
    page = tk.Tk()
    
    frame1 = tk.Frame(master=page, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
    
    page.mainloop()
    
main()
