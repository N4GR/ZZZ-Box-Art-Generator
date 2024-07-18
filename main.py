import os
import json
from PIL import Image

###
# Obtaining JSON config and assigning variables
###
def get_config():
    while True:
        try:
            with open("config.json") as file:
                config = json.load(file)

                return config

        except FileNotFoundError:
            print("Config JSON not found, generating one from template...")
            
            template = {
                "image_directory": "images/",
                "required_images": 54,
                "image_size": {
                    "height": 1024, 
                    "width": 1024
                    }
            }
            
            with open("config.json", "w") as file:
                json.dump(template, file, indent = 4)

config = get_config()
image_size = config["image_size"]["height"], config["image_size"]["width"]
image_directory = config["image_directory"]
image_amount_requirement = config["required_images"]
video_outer_cover_size = 135, 206
video_inner_cover_size = 104, 206

###
#
###
def get_image_list() -> dict[str]:
    if not os.path.exists(image_directory):
        print("Images folder not found, generating one...")
        os.makedirs("images")
        print(f"Successfully generated images folder at: {os.getcwd()}\\images")
        input("Please populate the images directory with images, then press Enter to continue...")

    image_list = os.listdir(image_directory)
    return image_list


image_list = get_image_list()

# Checks if files are images or corrupt.
for file in image_list:
    file_directory = f"{image_directory}{file}"

    try:
        image = Image.open(file_directory)
        image.verify()
        image.close()
    except (IOError, SyntaxError):
        print(f"[{file}] isn't an image or is corrupt, removing from list.")
        image_list.remove(file)
        continue

# Generating Box Art 1 image
def BoxArt1():
    image = Image.new(mode = "RGB", size = image_size)
    image.paste((53, 51, 51), (0, 0, image.size[0], image.size[1]))
    
    times_iterated = 0
    x = 0
    y = 0
    for file in image_list:
        pasting_image = Image.open(f"{image_directory}{file}")

        # Pasting outer cover
        image.paste(pasting_image.resize(video_outer_cover_size).rotate(180).transpose(method=Image.FLIP_LEFT_RIGHT), box = (x, y))
        # Pasting inner cover
        image.paste(pasting_image.resize(video_inner_cover_size).rotate(180).transpose(method=Image.FLIP_LEFT_RIGHT), box = (x, y))

        times_iterated += 1
        x += 136
        if times_iterated % 6 == 0:
            x = 0
            y += 204

        if times_iterated >= 30:
            break
    
    image.show()

BoxArt1()