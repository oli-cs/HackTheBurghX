import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

def main():
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
    oldImg = Image.open("assets/house1.jpg")
    img = ImageTk.PhotoImage(oldImg.resize((700,500)))
    
    # image is set to take the top left 4 grid boxes of the grid
    imageFrame.grid(column=0, columnspan=4, row=0, rowspan=6, sticky='nw', padx=10, pady=10)
    label = tk.Label(imageFrame, image = img)
    label.pack(fill=tk.BOTH, expand=True)

    # price
    price = "£500,000"
    text = tk.Label(window, text=price, bg="bisque", font=Font(weight="bold", size=50))
    text.grid(column=4, columnspan=4, row=0, sticky='n')

    #address
    address = "Barnehurst Road, Eltham, SE9"
    text2 = tk.Label(window, text=address, bg="bisque", font=Font(size=35))
    text2.grid(column=4, columnspan=4, row=1, sticky='n')

    # description
    description = "testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    text3 = tk.Label(window, text=description, bg="bisque", wraplength=(94*7))
    text3.grid(column=4, columnspan=4, row=2, rowspan=3, sticky='n')

    # agency
    agency = "Decent Landlord Lettings"
    text2 = tk.Label(window, text=agency, bg="bisque", font=Font(size=15), padx=10)
    text2.grid(column=0, columnspan=4, row=6, sticky='n')

    
    
    page.mainloop()
    
main()
