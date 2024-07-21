from startup import startChecks
from log import logging
from config import config

from os import listdir
from PIL import Image, ImageDraw, ImageFont, ImageOps
from colorthief import ColorThief
from wand import image

from random import choice

def image_list() -> list[str]:
    image_directory = "images"
    images = listdir(image_directory)

    file_count = len(images)
    error_count = 0
    print(logging().note(f"Detected {file_count} files, verifying integrity..."))
    for file in images:
        try:
            with Image.open(f"{image_directory}/{file}") as img:
                img.verify()
        except (IOError, SyntaxError):
            print(logging().error(f"{image_directory}/{file}"))
            images.remove(file)
            error_count += 1

    print(logging().note(f"{file_count - error_count}/{file_count} usable files."))
    
    return images

def BoxArt1():
    conf = config()

    #files = [conf.BoxArt1(), conf.BoxArt2(), conf.BoxArtBigger()]
    files = [conf.BoxArt1()]

    images = image_list()

    file_count = 0 # 0 = BoxArt1, 1 = BoxArt2, 3 = BoxArtBigger
    for file in files:
        canvas = Image.new(mode = "RGB", size = (file["canvas_size"]["width"], file["canvas_size"]["height"]))


        for cover_data in file["positions"]:
            print(logging().note(f"Processing images/{images[0]}"))
            image_directory = f"images/{images[0]}"
            cover = Image.open(image_directory)
            cover = cover.resize((cover_data["image_width"], cover_data["image_height"]), Image.Resampling.LANCZOS)

            canvas.paste(cover, (cover_data["image_x"], cover_data["image_y"]))

            if file_count == 0:
                # Pasting bottom bar
                dominant_colour = ColorThief(image_directory).get_color(quality = 8)
                canvas.paste(dominant_colour, (cover_data["image_x"], cover_data["image_y"] + cover_data["image_height"], cover_data["image_x"] + cover_data["image_width"] + 26, cover_data["image_y"] + cover_data["image_height"] + 26))

                canvas.paste(dominant_colour, (cover_data["image_x"] + cover_data["image_width"], cover_data["image_y"], cover_data["image_x"] + cover_data["image_width"] + 26, cover_data["image_y"] + cover_data["image_height"]))

                # Logos
                txt = ImageDraw.Draw(canvas)
                txt.text((cover_data["image_x"] + cover_data["image_width"] + 2, cover_data["image_y"] + cover_data["image_height"] - 5), "VHS", font = ImageFont.truetype("template/marv.ttf", 20), fill = (255, 255, 255), anchor = "lb")

                # Now I draw the circle:
                ratings = [{
                    "colour": (0, 255, 0),
                    "text": "U"
                },
                {
                    "colour": (255, 215, 0),
                    "text": "PG"
                },
                {
                    "colour": (255, 0, 0),
                    "text": "18"
                },
                {
                    "colour": (255, 165, 0),
                    "text": "12"
                },
                {
                    "colour": (255, 69, 0),
                    "text": "15"
                }]

                rating = choice(ratings)

                p_x, p_y = cover_data["image_x"] + cover_data["image_width"] + 13, cover_data["image_y"] + 20
                txt.ellipse((p_x - 10, p_y - 10, p_x + 10, p_y + 10), fill = rating["colour"])

                txt.text((p_x + 1, p_y), rating["text"], font = ImageFont.truetype("template/uniq.ttf", 10), fill = (255, 255, 255), anchor = "mm")
            
            del images[0]

        file_count += 1
    
    canvas.show()
    canvas = ImageOps.flip(canvas)
    canvas.save("hello.png")
    with image.Image(filename = "hello.png") as img:
        img.compression = "dxt5"
        img.save(filename = "hello.dds")

BoxArt1()