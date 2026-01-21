from PIL import ImageTk

class Animal:
    def __init__(self, name, habitat, desc, image):
        self.name = name
        self.habitat = habitat
        self.desc = desc
        self.image_pil = image
        self.image = ImageTk.PhotoImage(self.image_pil)  # Converting it to tk

    def get_name(self):
        return self.name

    def get_habitat(self):
        return self.habitat

    def get_desc(self):
        return self.desc

    def get_img(self):
        return self.image