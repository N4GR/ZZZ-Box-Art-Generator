from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Scrollbar, Label, filedialog, Toplevel, END, messagebox
from os import getcwd, path
from itertools import count

from config import versioning

from startup import checks
checks()

from PIL import Image, ImageTk, ImageDraw

from functioning import BoxArt
from log import logging

import webbrowser

import re

import ctypes
myappid = 'vamptek.modtools.boxartgenerator.1_5' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

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
        self.processing = False
        self.complete_image_showing = False
        self.image_list = []

        self.about_conf = versioning()

        self.window = Tk()
        self.window.title("N4GR - ZZZ Box Art Generator")
        icon_image = PhotoImage(file = "assets/logo.png")
        self.window.wm_iconphoto(False, icon_image)

        self.button_background_colour = "#FFFFFF"
        self.background_colour = "#FEF7FF"
        self.preview_window_colour = "#FFFFFF"
        self.text_colour = "#2c2d30"
        self.about_flash_colour = "#FF69B4"

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

        #self.aboutPage()

        # File counter to count how many images have been inputted.
        self.counter_text = self.canvas.create_text(
            48,
            530,
            anchor = "center",
            text = f"{self.image_count}/53",
            fill = self.text_colour,
            font = ("Roboto", 20 * -1, "bold")
        )
        
        # Version label
        version_label = Label(
            self.canvas, 
            text = f"{self.about_conf.getCreator()} - {self.about_conf.getVersion()}", 
            font = ("Roboto", 10, "bold"), 
            background = self.background_colour, 
            anchor = "w",
            foreground = self.text_colour
        )

        version_label.place(x = 840, y = 552)

        # Loop start
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
        def checkImage(file_name: str):
            try:
                with Image.open(file_name) as img:
                    img.verify()

                return True
            except (IOError, SyntaxError) as error:
                print(logging().error(error))

                return False

        file_types = [
            ("Image files", "*.jpg *.jpeg *.png"),
        ]

        files = filedialog.askopenfiles(filetypes = file_types)
        if not files:
            return

        invalid_files = []

        invalid_warning = False

        for file in files:
            self.image_count += 1 # Adds to image count

            if self.image_count > 53: # If there's more than 53 images, stop this.
                if invalid_warning is False:
                    messagebox.showerror("Too many images", "You selected too many images, this won't have an effect on the outcome.")
                    invalid_warning = True

                continue

            if checkImage(file.name) is False: # Checks if the image is valid and not corrupt.
                invalid_files.append(file.name)
                continue

            if self.image_count == 53:
                self.upload_button.config(state = "disabled")
            
            # Add image to image list
            self.image_list.append(file.name)
            
            self.canvas.itemconfig(self.counter_text, text = f"{self.image_count}/53")

            if self.image_count >= 53:
                self.start_button.config(state = "normal")

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
        
        if len(invalid_files) != 0:
            invalid_files = [file_name.split("/")[-1] for file_name in invalid_files]
            print(invalid_files)
            messagebox.showerror("Invalid Image", f"You entered the invalid images:\n{''.join(file_name + "\n" for file_name in invalid_files)}")

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

        self.menu_button = Button(
            image = w.image,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.aboutPage,
            relief = "flat",
            bg = self.background_colour,
            activebackground = self.background_colour
        )

        self.menu_button.place(
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

        self.start_button.config(state = "disabled")
        #BoxArt(mod_name, self.image_list)

        self.window.wm_state("iconic")

        if self.complete_image_showing is True:
            self.complete_image.destroy()
            self.complete_image_showing = False

        self.modEntry()
        
        #self.completeFunction()

    def completeFunction(self):
        self.processing = False

        print(logging().success("COMPLETE"))

        image = Image.open(relative_to_assets("done.png"))
        image = image.resize((55, 55))
        image = ImageTk.PhotoImage(image)
        
        w = Canvas(self.window)
        w.image = image

        self.load_animation.destroy()

        self.complete_image_showing = True
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
            state = "normal",
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
        #self.restart_button.config(state = "disabled")
        self.start_button.config(state = "disabled")

        self.canvas.itemconfig(self.counter_text, text = "0/53")

        self.inner_canvas.config(yscrollcommand = None)
        self.inner_canvas.config(scrollregion = (0, 0, 0, 0))

        if self.complete_image_showing is True:
            self.complete_image.destroy()
            self.complete_image_showing = False
        #self.y_scroll.destroy()

    def closeModEntry(self):
        self.entry_root.destroy()
        self.window.deiconify()

        if self.processing is False:
            self.start_button.config(state = "normal")
            self.upload_button.config(state = "normal")

    def modEntry(self):
        window_height = 240
        window_width = 280
        self.entry_root = Toplevel(self.window)
        self.entry_root.resizable(False, False)
        self.entry_root.protocol("WM_DELETE_WINDOW", self.closeModEntry)
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
        
        def is_valid_folder_name(folder_name):
            # Define invalid characters for Windows
            invalid_chars_windows = r'<>:"/\|?*'
            invalid_chars_unix = r'/'
            
            # Define reserved names for Windows
            reserved_names = {
                'CON', 'PRN', 'AUX', 'NUL',
                'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
                'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
            }

            # Check for invalid characters
            if re.search(f"[{re.escape(invalid_chars_windows)}]", folder_name) or re.search(f"[{re.escape(invalid_chars_unix)}]", folder_name):
                return False

            # Check for reserved names (case-insensitive)
            if folder_name.upper() in reserved_names:
                return False

            # Check for leading/trailing spaces or periods (Windows specific)
            if folder_name.startswith(' ') or folder_name.endswith(' ') or folder_name.endswith('.'):
                return False

            # Check for null characters
            if '\0' in folder_name:
                return False

            # Check length (though practically, this is not often a limiting factor)
            max_length = 50  # Typical maximum filename length
            if len(folder_name) > max_length:
                return False

            return True
        
        name_validate = (self.entry_root.register(is_valid_folder_name), "%P")

        Label(self.entry_canvas, text = "Mod Name:", font = ("Roboto", 18 * -1), anchor = "center", foreground = self.text_colour, background = self.background_colour).place(relx = 0.5, x = -45, y = 40, anchor = "center")
        self.mod_name_entry = Entry(
            self.entry_canvas,
            width = 30,
            validate = "key",
            validatecommand = name_validate
        )
        self.mod_name_entry.place(relx = 0.5, y = 60, anchor = "center")

        Label(self.entry_canvas, text = "Export Directory:", font = ("Roboto", 18 * -1), anchor = "center", foreground = self.text_colour, background = self.background_colour).place(relx = 0.5, x = -25, y = 102, anchor = "center")
        self.exp_dir_entry = Entry(
            self.entry_canvas, 
            width = 30
        )
        
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
        self.window.deiconify()

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
        
        if passing is False: return
        
        new_name = mod_name.replace(" ", "_").lower()

        if not path.isdir(expo_dir):
            messagebox.showerror("Invalid Directory", "You need to add a valid directory.")
            passing = False
            return
        elif path.isdir(f"{expo_dir}\\{new_name}"):
            messagebox.showerror("Already Exists", "This mod directory already exists, pick a different name or export directory.")
            passing = False
            return
        # CHECK DIRECTORY + MOD NAME

        if passing is True: self.entryPass()
    
    def entryPass(self):
        mod_name = self.mod_name_entry.get()
        export_directory = self.exp_dir_entry.get()

        self.processing = True
        self.entry_root.destroy()
        self.window.deiconify()

        self.load_animation = ImageLabel(self.canvas, background = self.background_colour)
        self.load_animation.load("assets/loading.gif")
        self.load_animation.place(x = 23, y = 430)

        BoxArt(mod_name, self.image_list, export_directory)
        self.completeFunction()

    def aboutPage(self):
        def enableAboutButton():
            self.menu_button.config(state = "normal")
            about_root.destroy()
            self.window.deiconify()
        
        self.window.wm_state("iconic")
        self.menu_button.config(state = "disabled")

        window_height = 300
        window_width = 300
        about_root = Toplevel(self.window)
        about_root.resizable(False, False)
        about_root.protocol("WM_DELETE_WINDOW", enableAboutButton)

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
            current_color = flashing_author.cget("foreground")
            next_color = self.about_flash_colour if current_color == "black" else "black"
            flashing_author.config(foreground=next_color)
            about_canvas.after(500, flash_text)  # Schedule the function to be called again after 500 milliseconds

        # Add a label widget
        flashing_author = Label(
            about_canvas, 
            text = self.about_conf.getCreator(), 
            font = ("Roboto", 30, "bold"), 
            background = self.background_colour, 
            anchor = "center"
        )

        flashing_author.place(x = 90, y = 30)

        flash_text()

        github_image = createButton(55, 55, self.button_background_colour, "github.png")
    
        w = Canvas(about_root)
        w.github_image = github_image

        github_button = Button(
            master = about_canvas,
            image = w.github_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = browsing.openGitHub,
            relief = "flat",
            bg = self.background_colour,
            state = "normal",
            activebackground = self.background_colour
        )

        github_button.place(
            x = 90,
            y = 140,
            width = 55,
            height = 55
        )

        kofi_image = createButton(55, 55, self.button_background_colour, "ko-fi.png")
    
        w = Canvas(about_root)
        w.kofi_image = kofi_image

        kofi_button = Button(
            master = about_canvas,
            image = w.kofi_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = browsing.openKoFi,
            relief = "flat",
            bg = self.background_colour,
            state = "normal",
            activebackground = self.background_colour
        )

        kofi_button.place(
            x = 150,
            y = 140,
            width = 55,
            height = 55
        )

        paypal_image = createButton(110, 55, self.button_background_colour, "paypal.png")
    
        w = Canvas(about_root)
        w.paypal_image = paypal_image

        paypal_button = Button(
            master = about_canvas,
            image = w.paypal_image,
            borderwidth = 0,
            highlightthickness = 0,
            command = browsing.openPayPal,
            relief = "flat",
            bg = self.background_colour,
            state = "normal",
            activebackground = self.background_colour
        )

        paypal_button.place(
            x = 91,
            y = 80,
            width = 110,
            height = 55
        )

class browsing:
    def openPayPal():
        webbrowser.open(url = "https://www.paypal.me/n4gr")
    
    def openKoFi():
        webbrowser.open(url = "https://ko-fi.com/n4gr_")

    def openGitHub():
        webbrowser.open(url = "https://github.com/N4GR")

ui()