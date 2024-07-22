from startup import checks
from log import logging
from config import config
from generate import generate
from versioning import version_check

from PIL import Image, ImageOps
from wand import image
import os
from collections import Counter
import threading
import argparse

def argCheck(arg: str) -> dict[str | int]:
    mod_name = arg.replace(" ", "_").lower()
    mod_path = f"mods/{mod_name}"

    if os.path.isdir(mod_path) is False:
        generate.directory("mods", mod_name)
        generate.directory(f"mods/{mod_name}", "previews")
        return mod_name
    else:
        print(logging().error("Mod already exists in 'mods/' directory"))
        os.abort()

def BoxArt1(canvas: Image.Image, cover_data: dict, cover: Image.Image):
    def botbar():
        # Pasting bottom bar

        colours = cover.getdata()
        filtered_colours = [colour for colour in colours if colour != (255, 255, 255) and colour != (0, 0, 0)]
        colour_counts = Counter(filtered_colours)
        common_colour = colour_counts.most_common(1)[0]
        most_common_rgb = common_colour[0]

        dark_grey = (53, 51, 51)
        canvas.paste(dark_grey, (cover_data["image_x"] + cover_data["image_width"], cover_data["image_y"], cover_data["image_x"] + cover_data["image_width"] + 31, cover_data["image_y"] + cover_data["image_height"]))
        canvas.paste(most_common_rgb, (cover_data["image_x"] + cover_data["image_width"] + 5, cover_data["image_y"], cover_data["image_x"] + cover_data["image_width"] + 26, cover_data["image_y"] + cover_data["image_height"]))
        canvas.paste(most_common_rgb, (cover_data["image_x"], cover_data["image_y"] + cover_data["image_height"], cover_data["image_x"] + cover_data["image_width"] + 26, cover_data["image_y"] + cover_data["image_height"] + 26))

    botbar()

def place_covers(cover_data, canvas: Image.Image, file_name: str, cover_image: str):
    print(logging().note(f"Processing images/{cover_image}"))
    image_directory = f"images/{cover_image}"
    cover = Image.open(image_directory)
    cover = cover.resize((cover_data["image_width"], cover_data["image_height"]), Image.Resampling.LANCZOS)
    cover = cover.rotate(cover_data["rotation"], expand = True)

    canvas.paste(cover, (cover_data["image_x"], cover_data["image_y"]))

    if file_name == "BoxArt1": BoxArt1(canvas, cover_data, cover)

def BoxArt(mod_name: str):
    mod_path = f"mods/{mod_name}"

    conf = config()

    # The art to generate
    files = [conf.BoxArt1, conf.BoxArt2, conf.BoxArtBig]

    images = generate.image_list()

    for file in files:
        file_name = file.__name__
        file = file()
    
        canvas = Image.new(mode = "RGB", size = (file["canvas_size"]["width"], file["canvas_size"]["height"]))
        template = Image.open(f"template/{file_name}.png")
        canvas.paste(template, (0, 0))

        thread_counter = 0
        threads = []
        for cover_data in file["positions"]:
            cover_image = images[thread_counter]
            t = threading.Thread(target = place_covers, args = (cover_data, canvas, file_name, cover_image))
            t.start()
            threads.append(t)
            thread_counter += 1
        
        for thread in threads:
            thread.join()

        canvas = ImageOps.flip(canvas)
        canvas.save(f"{mod_path}/previews/{file_name}.png")
        with image.Image(filename = f"{mod_path}/previews/{file_name}.png") as img:
            img.compression = "dxt5"
            img.save(filename = f"{mod_path}/{file_name}.dds")
        
        os.remove(f"{mod_path}/previews/{file_name}.png")
        canvas = ImageOps.flip(canvas)
        canvas.save(f"{mod_path}/previews/{file_name}.png")
    
    generate.ini(mod_path, mod_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process the --name argument.")
    parser.add_argument("--name", type=str, required=True, help="Name of the mod")

    args = parser.parse_args()



    if checks() is False:
        os.abort()

    print(args.name)
    print(type(args.name))

    BoxArt(argCheck(args.name))