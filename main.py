from startup import checks, inputs
from log import logging
from config import config
from generate import generate

from PIL import Image, ImageDraw, ImageFont, ImageOps
from colorthief import ColorThief
from wand import image
from random import choice
import os

if checks() is False:
    os.abort()

def inputChecks() -> dict[str | int]:
    while True:
        inp = inputs()

        mod_name = inp["mod_name"]
        mod_path = f"mods/{inp["mod_name"]}"

        if os.path.isdir(mod_path) is False:
            generate.directory("mods", mod_name)
            return inp
        else:
            print(logging().error("Mod already exists in 'mods/' directory"))

def BoxArt():
    inp = inputChecks()
    mod_name = inp["mod_name"]
    mod_path = f"mods/{mod_name}"

    conf = config()

    # The art to generate
    files = [conf.BoxArt1, conf.BoxArt2, conf.BoxArtBigger]
    #files = [conf.BoxArt1()]

    images = generate.image_list()

    for file in files:
        file_name = file.__name__
        file = file()
    
        canvas = Image.new(mode = "RGB", size = (file["canvas_size"]["width"], file["canvas_size"]["height"]))


        for cover_data in file["positions"]:
            print(logging().note(f"Processing images/{images[0]}"))
            image_directory = f"images/{images[0]}"
            cover = Image.open(image_directory)
            cover = cover.resize((cover_data["image_width"], cover_data["image_height"]), Image.Resampling.LANCZOS)
            cover = cover.rotate(cover_data["rotation"], expand = True)

            canvas.paste(cover, (cover_data["image_x"], cover_data["image_y"]))

            if file_name == "BoxArt1":
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

        canvas = ImageOps.flip(canvas)
        canvas.save(f"{mod_path}/{file_name}.png")
        with image.Image(filename = f"{mod_path}/{file_name}.png") as img:
            img.compression = "dxt5"
            img.save(filename = f"{mod_path}/{file_name}.dds")
    
    generate.ini(mod_path, mod_name)

BoxArt()