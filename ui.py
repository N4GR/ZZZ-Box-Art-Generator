from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Scrollbar, Label, StringVar, filedialog, simpledialog, Toplevel
from tkinter.ttk import Progressbar
from os import getcwd

from startup import checks
checks()

from PIL import Image, ImageTk

from main import BoxArt

ASSETS_PATH = Path(fr"{getcwd()}\\assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def round_rectangle(canvas: Canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

class ui():
    def __init__(self) -> None:
        self.thumbnail_x_offset = 0
        self.thumbnail_y_offset = 0
        self.image_count = 0
        self.image_list = []
        self.window = Tk()

        self.window.geometry("936x570")
        self.window.configure(bg = "#FEF7FF")

        self.canvas = Canvas(
            self.window,
            bg = "#FEF7FF",
            height = 570,
            width = 936,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        #rounded_rect = round_rectangle(self.canvas, 0, 0, 823, 532, radius = 25, fill = "#FFFFFF")

        self.inner_canvas = Canvas(
            self.canvas,
            bg = "#FFFFFF",
            width = 823, 
            height = 530,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge",
        )
        self.inner_canvas.place(x = 90, y = 20)

        # Upload button
        self.uploadButton()

        # Three lined menu button
        self.menuButton()

        # Start button
        self.startButton()

        #self.complete()
        #self.modEntry()
        self.restartButton()

        self.counter_text = self.canvas.create_text(
            48,
            530,
            anchor = "center",
            text = f"{self.image_count}/53",
            fill = "#000000",
            font = ("Roboto", 20 * -1, "bold")
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def openImage(self):
        file_types = [
            ("Image files", "*.jpg *.jpeg *.png"),
        ]

        files = filedialog.askopenfiles(filetypes = file_types)
        if not files:
            return

        for file in files:
            self.image_list.append(file.name)
            self.image_count += 1
            self.canvas.itemconfig(self.counter_text, text = f"{self.image_count}/53")

            #print(self.image_list, self.thumbnail_y_offset)

            if self.image_count >= 53:
                self.start_button.config(state = "normal")
                #self.modEntry()

            if self.thumbnail_x_offset == 770:
                self.thumbnail_x_offset = 0
                self.thumbnail_y_offset += 125

            if self.thumbnail_y_offset == 375:
                self.y_scroll = Scrollbar(self.inner_canvas, orient = "vertical", command = self.inner_canvas.yview)
                self.y_scroll.place(x = 806, y = 0, height = 530)

                self.inner_canvas.config(yscrollcommand = self.y_scroll.set)
            
            if self.thumbnail_y_offset >= 375:
                self.inner_canvas.config(scrollregion = (0, 0, 0, self.thumbnail_y_offset + 150))

            self.addThumbnail(self.thumbnail_x_offset, self.thumbnail_y_offset, file)
            self.thumbnail_x_offset += 110

        #for x in self.image_display():
        #    x = None

        #self.inner_canvas.delete("all")

    def addThumbnail(self, thumbnail_x_offset: int, thumbnail_y_offset: int, file):
        #image = Image.open("assets/frame0/image_preview.png")
        #image = image.resize((100, 100))
        #image = ImageTk.PhotoImage(image)

        thumbnail_name = file.name.split("/")[-1]

        if len(thumbnail_name) > 20:
            thumbnail_name = f"{thumbnail_name[:15]}..."

        try:
            image = Image.open(file.name)
            image.thumbnail((100, 100))
            image = ImageTk.PhotoImage(image)
        
            w = Canvas(self.window)
            w.image = image

            self.inner_canvas.create_image(
                80 + thumbnail_x_offset,
                70 + thumbnail_y_offset,
                image = w.image
            )
        except:
            image = Image.open("assets/frame0/image_preview.png")
            image = image.resize((100, 100))
            image = ImageTk.PhotoImage(image)

            w = Canvas(self.window)
            w.image = image

            self.inner_canvas.create_image(
                80 + thumbnail_x_offset,
                70 + thumbnail_y_offset,
                image = w.image
            )
        
        self.inner_canvas.create_text(
            80 + thumbnail_x_offset,
            130 + thumbnail_y_offset,
            anchor = "center",
            text = thumbnail_name,
            fill = "#000000",
            font = ("Roboto", 11 * -1)
            )
        

    def menuButton(self):
        image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        
        w = Canvas(self.window)
        w.image = image

        button_1 = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("button_1 clicked"),
            relief = "flat",
            bg = "#FEF7FF",
            activebackground = "#FEF7FF"
        )

        button_1.place(
            x = 36.0,
            y = 34.0,
            width = 24.0,
            height = 24.0
        )

    def uploadButton(self):
        image = PhotoImage(file = relative_to_assets("button_2.png"))

        w = Canvas(self.window)
        w.image = image
        
        self.upload_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.openImage,
            relief = "flat",
            bg = "#FEF7FF",
            activebackground = "#FEF7FF"
        )

        self.upload_button.place(
            x = 23.0,
            y = 77.0,
            width = 55.0,
            height = 50.0
        )

    def startButton(self):
        #image = PhotoImage(file = relative_to_assets("play.png"))

        image = Image.open(relative_to_assets("play.png"))
        image = image.resize((55, 55))
        image = ImageTk.PhotoImage(image)
        
        w = Canvas(self.window)
        w.image = image

        self.start_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.startFunction,
            relief = "flat",
            bg = "#FEF7FF",
            state = "disabled",
            activebackground = "#FEF7FF"
        )

        self.start_button.place(
            x = 23,
            y = 135,
            width = 55,
            height = 55
        )
    
    def startFunction(self):
        #mod_name = self.mod_name_var.get()
        #if mod_name == "":
        #    messagebox.showerror("Mod Name Needed", "Name your mod, it's required to create the directory.")
        #    return

        self.upload_button.config(state = "disabled")
        self.start_button.config(state = "disabled")
        #BoxArt(mod_name, self.image_list)

        self.modEntry()
        
        self.completeFunction()

    def completeFunction(self):
        image = Image.open(relative_to_assets("done.png"))
        image = image.resize((55, 55))
        image = ImageTk.PhotoImage(image)
        
        w = Canvas(self.window)
        w.image = image


        self.complete_image = Label(self.canvas, image = w.image, background = "#FEF7FF")
        self.complete_image.place(
            x = 20,
            y = 430
        )

        #self.canvas.create_image(
        #        50,
        #        430,
        #        image = w.image
        #)

        self.restart_button.config(state = "normal")
        self.start_button.config(state = "disabled")
    
    def restartButton(self):
        image = Image.open(relative_to_assets("restart.png"))
        image = image.resize((55, 55))
        image = ImageTk.PhotoImage(image)
        
        w = Canvas(self.window)
        w.image = image

        self.restart_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.restartFunction,
            relief = "flat",
            bg = "#FEF7FF",
            state = "disabled",
            activebackground = "#FEF7FF"
        )

        self.restart_button.place(
            x = 23,
            y = 193,
            width = 55,
            height = 55
        )
    
    def restartFunction(self):
        self.inner_canvas.delete("all")

        self.thumbnail_x_offset = 0
        self.thumbnail_y_offset = 0
        self.image_count = 0
        self.image_list = []

        self.upload_button.config(state = "normal")
        self.restart_button.config(state = "disabled")

        self.canvas.itemconfig(self.counter_text, text = "0/53")

        self.inner_canvas.config(yscrollcommand = None)
        self.inner_canvas.config(scrollregion = (0, 0, 0, 0))

        self.complete_image.destroy()
        #self.y_scroll.destroy()

    def modEntry(self):
        top = Toplevel(self.window)
        top.geometry("750x250")
        entry = Entry(top, width= 25)
        entry.pack()
        
        #mod_name = simpledialog.askstring(title="Mod Name Entry", prompt="What's your mod called?:")
        
        #self.mod_name_var = StringVar()

        #name_label = Label(self.canvas, text = "Mod Name", font = ("Roboto", 18 * -1, "bold"), anchor = "center", background = "#FEF7FF")
        #name_label.place(x = 87, y = 563)
        #name_entry = Entry(self.canvas, textvariable = self.mod_name_var, font = ("Roboto", 18 * -1), width = 17)
        #name_entry.place(x = 190, y = 563)

ui()