from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Scrollbar, Label, filedialog, Toplevel, END, messagebox, OptionMenu, StringVar
from tkinter.ttk import Progressbar
from os import getcwd
from itertools import count

from config import versioning

from startup import checks
checks()

from PIL import Image, ImageTk, ImageDraw

from main import BoxArt

ASSETS_PATH = Path(fr"{getcwd()}\\assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def createButton(width: int, height: int, colour: str, file_name: str, flip = False):
    image = Image.new("RGBA", (width, height))
    image_draw = ImageDraw.Draw(image)
    image_draw.rounded_rectangle((0, 0, width, height), fill = colour, width = 3, radius = round(((width + height) / 2) / 4))

    pasting_image = Image.open(relative_to_assets(file_name)).resize((width, height))
    image.paste(pasting_image, (0, 0), pasting_image)

    if flip: image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    return ImageTk.PhotoImage(image)

class ImageLabel(Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

class ui():
    def __init__(self) -> None:
        self.thumbnail_x_offset = 0
        self.thumbnail_y_offset = 0
        self.warn_count = 0
        self.image_count = 0
        self.image_list = []

        self.window = Tk()
        self.window.title("N4GR - ZZZ Box Art Generator")

        self.button_background_colour = "#FFFFFF"
        self.background_colour = "#FEF7FF"
        self.preview_window_colour = "#FFFFFF"
        self.text_colour = "#2c2d30"

        self.window_height = 570
        self.window_width = 936
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.window.configure(bg = self.background_colour)
        self.window.resizable(False, False)

        self.center_window(self.window, self.window_width, self.window_height)

        self.canvas = Canvas(
            self.window,
            bg = self.background_colour,
            height = self.window_height,
            width = self.window_width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        #rounded_rect = round_rectangle(self.canvas, 0, 0, 823, 532, radius = 25, fill = "#FFFFFF")
        
        self.inner_canvas = Canvas(
            self.canvas,
            bg = self.preview_window_colour,
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

        # Restart button
        self.restartButton()

        self.aboutPage()

        self.counter_text = self.canvas.create_text(
            48,
            530,
            anchor = "center",
            text = f"{self.image_count}/53",
            fill = self.text_colour,
            font = ("Roboto", 20 * -1, "bold")
        )
        
        self.window.mainloop()
    
    def center_window(self, root: Tk, width: int, height: int):
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

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
            command = self.aboutPage,
            relief = "flat",
            bg = self.background_colour,
            activebackground = self.background_colour
        )

        button_1.place(
            x = 36.0,
            y = 34.0,
            width = 24.0,
            height = 24.0
        )

    def uploadButton(self):
        image = createButton(55, 55, self.button_background_colour, "button_upload.png")
        
        w = Canvas(self.window)
        w.image = image

        self.upload_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.openImage,
            relief = "flat",
            bg = self.background_colour,
            activebackground = self.background_colour
        )

        self.upload_button.place(
            x = 23.0,
            y = 77.0,
            width = 55.0,
            height = 50.0
        )

    def startButton(self):
        image = createButton(55, 55, self.button_background_colour, "button_play.png")
        
        w = Canvas(self.window)
        w.image = image

        self.start_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.startFunction,
            relief = "flat",
            bg = self.background_colour,
            state = "disabled",
            activebackground = self.background_colour
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

        self.window.wm_state("iconic")

        self.modEntry()
        
        #self.completeFunction()

    def completeFunction(self):
        image = Image.open(relative_to_assets("done.png"))
        image = image.resize((55, 55))
        image = ImageTk.PhotoImage(image)
        
        w = Canvas(self.window)
        w.image = image

        self.load_animation.destroy()

        self.complete_image = Label(self.canvas, image = w.image, background = self.background_colour)
        self.complete_image.place(x = 23, y = 430)

        self.restart_button.config(state = "normal")
        self.start_button.config(state = "disabled")
    
    def restartButton(self):
        image = createButton(55, 55, self.button_background_colour, "button_restart.png")

        w = Canvas(self.window)
        w.image = image

        self.restart_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.restartFunction,
            relief = "flat",
            bg = self.background_colour,
            state = "disabled",
            activebackground = self.background_colour
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
        window_height = 240
        window_width = 280
        self.entry_root = Toplevel(self.window)
        self.entry_root.resizable(False, False)
        #entry_root.overrideredirect(True)

        self.center_window(self.entry_root, window_width, window_height)

        self.entry_canvas = Canvas(
            self.entry_root,
            bg = self.background_colour,
            height = 240,
            width = 280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.entry_canvas.place(x = 0, y = 0)
        
        Label(self.entry_canvas, text = "Mod Name:", font = ("Roboto", 18 * -1), anchor = "center", foreground = self.text_colour, background = self.background_colour).place(relx = 0.5, x = -45, y = 40, anchor = "center")
        self.mod_name_entry = Entry(self.entry_canvas, width = 30)
        self.mod_name_entry.place(relx = 0.5, y = 60, anchor = "center")

        Label(self.entry_canvas, text = "Export Directory:", font = ("Roboto", 18 * -1), anchor = "center", foreground = self.text_colour, background = self.background_colour).place(relx = 0.5, x = -25, y = 102, anchor = "center")
        self.exp_dir_entry = Entry(self.entry_canvas, width = 30)
        self.exp_dir_entry.place(relx = 0.5, y = 127, anchor = "center")
        self.exp_dir_entry.insert(0, f"{getcwd()}/mods")

        # Creating two buttons
        button_image = ("button_cancel.png", "button_play.png")
        command = [self.modEntryCancel, self.modEntryCheck]
        for x in range(2):
            image = createButton(55, 55, self.button_background_colour, button_image[x])
            w = Canvas(self.entry_canvas)
            w.image = image

            entry_start_button = Button(
                self.entry_root,
                image = w.image,
                borderwidth = 0,
                highlightthickness = 0,
                command = command[x],
                relief = "flat",
                bg = self.background_colour,
                state = "normal",
                activebackground = self.background_colour
            )

            entry_start_button.place(relx = 0.5, x = 40 if x == 1 else -40, y = 190, anchor = "center", width = 55, height = 55)

        image = createButton(20, 20, self.button_background_colour, "dir_select.png")
        w = Canvas(self.entry_canvas)
        w.image = image

        dir_entry_button = Button(
            self.entry_root,
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.modEntryDirSelect,
            relief = "flat",
            bg = self.background_colour,
            state = "normal",
            activebackground = self.background_colour
        )

        dir_entry_button.place(relx = 0.5, x = 100, y = 127, anchor = "center", width = 20, height = 20)

    def modEntryDirSelect(self):
        directory = filedialog.askdirectory()

        self.exp_dir_entry.delete(0, END)
        self.exp_dir_entry.insert(0, directory)

        self.mod_directory = directory

    def modEntryCancel(self):
        self.entry_root.destroy()
        self.upload_button.config(state = "normal")
        self.start_button.config(state = "normal")

    def modEntryCheck(self):
        mod_name = self.mod_name_entry.get()
        expo_dir = self.exp_dir_entry.get()

        passing = True

        warning_image = Image.open(relative_to_assets("warning.png")).resize((20, 20))
        warning_image = ImageTk.PhotoImage(warning_image)
        w = Canvas(self.entry_canvas)
        w.image = warning_image

        def placeWarning(y: int):
            warning_mod_name = Label(self.entry_root, image = w.image, background = self.background_colour)
            warning_mod_name.place(relx = 0.5, x = -110, y = y, anchor = "center", width = 20, height = 20)

            self.warn_count += 1

        def warnCheck(error_message: str):
            if self.warn_count > 1:
                messagebox.showerror("No Entry", error_message)
                self.warn_count = 0

        iter_count = 0
        warning_text = ["Missing mod name.", "Missing directory entry."]
        for entry in [mod_name, expo_dir]:
            if entry == "":
                warnCheck(warning_text[iter_count])
                placeWarning(60 if iter_count == 0 else 127)
                passing = False
            iter_count += 1

        if passing is True: self.entryPass()
    
    def entryPass(self):
        mod_name = self.mod_name_entry.get()
        export_directory = self.exp_dir_entry.get()
        self.entry_root.destroy()

        self.window.deiconify()

        self.load_animation = ImageLabel(self.canvas, background = self.background_colour)
        self.load_animation.load("assets/loading.gif")
        self.load_animation.place(x = 23, y = 430)

        BoxArt(mod_name, self.image_list, export_directory)
        self.completeFunction()

    def aboutPage(self):
        window_height = 300
        window_width = 300
        about_root = Toplevel(self.window)
        about_root.resizable(False, False)

        self.center_window(about_root, window_width, window_height)

        about_canvas = Canvas(
            about_root,
            bg = self.background_colour,
            height = window_height,
            width = window_height,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        about_canvas.place(x = 0, y = 0)
        
        load_animation = ImageLabel(about_root, background = self.background_colour)
        load_animation.load("assets/about_bot.gif")
        load_animation.place(x = 0, y = 200)

        def flash_text():
            current_color = label.cget("foreground")
            next_color = "red" if current_color == "black" else "black"
            label.config(foreground=next_color)
            about_canvas.after(500, flash_text)  # Schedule the function to be called again after 500 milliseconds

        # Add a label widget
        label = Label(
            about_canvas, 
            text="Flashing Text", 
            font=("Roboto", 30, "bold"), 
            background = self.background_colour, 
            anchor = "center"
        )
        
        label.place(x = 150, y = 150)

        flash_text()

ui()