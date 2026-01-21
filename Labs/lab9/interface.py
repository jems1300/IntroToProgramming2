from Animal import Animal
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()

root.title("Museum Catalog")
root.geometry("700x500")

grasshopper = Animal("Grasshopper", "Everglades", "A grasshopper can jump up to 30 inches. "
                                                  "That's roughly 20 times its body length.",
                                                  Image.open("Grasshopper.webp"))

name_label = tk.Label(root, text=grasshopper.get_name())
name_label.pack()
habitat_label = tk.Label(root, text=grasshopper.get_habitat())
habitat_label.pack(pady=10)
desc_label = tk.Label(root, text=grasshopper.get_desc())
desc_label.pack()
image_label = tk.Label(root, image=grasshopper.get_img())
image_label.pack(padx=10, pady=10)

root.mainloop()