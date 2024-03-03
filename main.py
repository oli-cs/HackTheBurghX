import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from suggestionAlgorithm import HouseTinder

def createGUI(data,backend):
    page = tk.Tk()
    page.attributes("-fullscreen", True)

    # window with border are created as frames
    border = tk.Frame(master=page, width=210, height=110, bg="DeepPink4")
    window = tk.Frame(master=border, width=200, height=100, bg="thistle1")

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
    text = tk.Label(window, text=price, bg="thistle1", font=Font(weight="bold", size=50))
    text.grid(column=4, columnspan=4, row=0, sticky='n')

    # address
    address = data[5]
    text2 = tk.Label(window, text=address, bg="thistle1", font=Font(size=35))
    text2.grid(column=4, columnspan=4, row=1, sticky='n')

    # description
    description = data[7]
    text3 = tk.Label(window, text=description, bg="thistle1", font=Font(size=23), wraplength=(94*7))
    text3.grid(column=4, columnspan=4, row=2, rowspan=4, sticky='n')

    # agency
    agency = data[1]
    text4 = tk.Label(window, text=agency, bg="thistle1", font=Font(size=23), padx=10)
    text4.grid(column=0, columnspan=4, row=6, sticky='n')

    # padding
    padding = tk.Label(window, text=" ", bg="thistle1", font=Font(size=80))
    padding.grid(column=0, row=7)
    
    # bedroom icon
    oldImg2 = Image.open("icons/bedroom.png")
    img2 = ImageTk.PhotoImage(oldImg2.resize((100,100)))
    bedroom = tk.Frame(master=window)
    bedroom.grid(column=0, row=8, sticky='s')
    label2 = tk.Label(bedroom, image=img2, bg="thistle1")
    label2.pack(fill=tk.BOTH, expand=True)

    # bedroom number
    bedroomNum = str(data[2])
    text5 = tk.Label(window, text=bedroomNum, bg="thistle1", font=Font(weight="bold", size=42))
    text5.grid(column=1, row=8)

    # bathroom icon
    oldImg3 = Image.open("icons/bathroom.png")
    img3 = ImageTk.PhotoImage(oldImg3.resize((100,100)))
    bathroom = tk.Frame(master=window)
    bathroom.grid(column=2, row=8, sticky='s')
    label3 = tk.Label(bathroom, image=img3, bg="thistle1")
    label3.pack(fill=tk.BOTH, expand=True)

    # bathroom number
    bathroomNum = str(data[3])
    text6 = tk.Label(window, text=bathroomNum, bg="thistle1", font=Font(weight="bold", size=42))
    text6.grid(column=3, row=8)

    # left arrow
    oldImg4 = Image.open("icons/left_arrow.png")
    img4 = ImageTk.PhotoImage(oldImg4.resize((100,100)))
    leftArrow = tk.Label(window, image=img4, bg="thistle1")
    leftArrow.grid(column=5, row=6)

    # dislike
    text5 = tk.Label(window, text="dislike", bg="thistle1")
    text5.grid(column=5, row=7, sticky='n')

    # right arrow
    oldImg5 = Image.open("icons/right_arrow.png")
    img5 = ImageTk.PhotoImage(oldImg5.resize((100,100)))
    rightArrow = tk.Label(window, image=img5, bg="thistle1")
    rightArrow.grid(column=6, row=6)

    # like
    text5 = tk.Label(window, text="like", bg="thistle1")
    text5.grid(column=6, row=7, sticky='n')

    # reason text
    if (backend.get_recommendation_reason() != "randomised"):
        reason = tk.Label(window, text=backend.get_recommendation_reason(), bg='bisque')
        reason.grid(row=8, column=7, sticky='se')
        
    # on left or right arrow key press, destroy page
    def leftKey(event):
        backend.append_left(data[0])
        page.destroy()

    def rightKey(event):
        backend.append_right(data[0])
        page.destroy()
        
    # detects arrow key presses
    page.bind('<Left>', leftKey)
    page.bind('<Right>', rightKey)
    
    page.mainloop()

    return()


def end():
    page = tk.Tk()
    page.attributes("-fullscreen", True)

    # window with border are created as frames
    border = tk.Frame(master=page, width=210, height=110, bg="DeepPink4")
    window = tk.Frame(master=border, width=200, height=100, bg="thistle1")

    # the frame that holds the image is created
    imageFrame = tk.Frame(master=window)

    # border and windows are packed to fit the page
    border.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
    window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # check back later text
    text = tk.Label(window, text="You have viewed \n all properties in your \n area! Check back later \n for new additions.", font=Font(size=40), bg="thistle1")
    text.pack(pady=50)

    # logo
    oldImg = Image.open("icons/logo.png")
    img = ImageTk.PhotoImage(oldImg.resize((100,100)))
    logo = tk.Label(window, image=img, bg="thistle1")
    logo.pack(side='bottom', pady=50)
    
    page.mainloop()

def main():
    backend = HouseTinder()
    createGUI(backend.get_next_house(),backend)
    while True:
        nextHouse = backend.get_next_house()
        if nextHouse != []:
            createGUI(nextHouse,backend)
        else:
            end()
            return

main()
