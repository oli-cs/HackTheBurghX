import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from suggestionAlgorithm import HouseTinder

def createGUI(data):
    page = tk.Tk()

    # window with border are created as frames
    border = tk.Frame(master=page, width=210, height=110, bg="saddle brown")
    window = tk.Frame(master=border, width=200, height=100, bg="bisque")

    # the frame that holds the image is created
    imageFrame = tk.Frame(master=window)

    # border and windows are packed to fit the page
    border.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
    window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # image is resized into 500px by 500px aspect ratio
    oldImg1 = Image.open(data[6])
    img1 = ImageTk.PhotoImage(oldImg1.resize((700,500)))
    
    # image is set to take the top left 4 grid boxes of the grid
    imageFrame.grid(column=0, columnspan=4, row=0, rowspan=6, sticky='nw', padx=10, pady=10)
    label1 = tk.Label(imageFrame, image = img1)
    label1.pack(fill=tk.BOTH, expand=True)

    # price
    price = "£" + str(data[4])
    text = tk.Label(window, text=price, bg="bisque", font=Font(weight="bold", size=50))
    text.grid(column=4, columnspan=4, row=0, sticky='n')

    # address
    address = data[5]
    text2 = tk.Label(window, text=address, bg="bisque", font=Font(size=35))
    text2.grid(column=4, columnspan=4, row=1, sticky='n')

    # description
    description = data[7]
    text3 = tk.Label(window, text=description, bg="bisque", wraplength=(94*7))
    text3.grid(column=4, columnspan=4, row=2, rowspan=6, sticky='n')

    # agency
    agency = data[1]
    text4 = tk.Label(window, text=agency, bg="bisque", font=Font(size=20), padx=10)
    text4.grid(column=0, columnspan=4, row=6, sticky='n')

    # padding
    padding = tk.Label(window, text=" ", bg="bisque", font=Font(size=80))
    padding.grid(column=0, row=7)
    
    # bedroom icon
    oldImg2 = Image.open("icons/bedroom.png")
    img2 = ImageTk.PhotoImage(oldImg2.resize((100,100)))
    bedroom = tk.Frame(master=window)
    bedroom.grid(column=0, row=8, sticky='s')
    label2 = tk.Label(bedroom, image=img2, bg="bisque")
    label2.pack(fill=tk.BOTH, expand=True)

    # bedroom number
    bedroomNum = str(data[2])
    text5 = tk.Label(window, text=bedroomNum, bg="bisque", font=Font(weight="bold", size=42))
    text5.grid(column=1, row=8)

    # bathroom icon
    oldImg3 = Image.open("icons/bathroom.png")
    img3 = ImageTk.PhotoImage(oldImg3.resize((100,100)))
    bathroom = tk.Frame(master=window)
    bathroom.grid(column=2, row=8, sticky='s')
    label3 = tk.Label(bathroom, image=img3, bg="bisque")
    label3.pack(fill=tk.BOTH, expand=True)

    # bathroom number
    bathroomNum = str(data[3])
    text6 = tk.Label(window, text=bathroomNum, bg="bisque", font=Font(weight="bold", size=42))
    text6.grid(column=3, row=8)

    # on left or right arrow key press, destroy page
    def leftKey():
        page.destroy()

    def rightKey():
        page.destroy()
        
    # detects arrow key presses
    page.bind('<Left>', leftKey)
    page.bind('<Right>', rightKey)
    
    page.mainloop()


def main():
    backend = HouseTinder()
    while True:
        createGUI(backend.get_next_house())

main()
