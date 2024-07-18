import os
import json
from PIL import Image, ImageOps
from random import choice

def imgtoddf(file_name: str) -> bool:
    try:
        os.system(f"quicktex encode auto {file_name}")
        return True
    except Exception as error:
        print(error+"\n")
        print("Image to DDF conversion error, you'll need to do this manually with the images generated.")
        return False

def config_template():
    return {
        "image_directory": "images/",
        "required_images": 54,
        "image_size": {
            "height": 1024,
            "width": 1024
        },
        "BoxArt2Positions": [
            {   
                "name": "image1",
                "image_x": 682,
                "image_y": 101,
                "image_width": 180,
                "image_height": 225
            },
            {   
                "name": "image2",
                "image_x": 861,
                "image_y": 121,
                "image_width": 163,
                "image_height": 205
            },
            {   
                "name": "image3",
                "image_x": 523,
                "image_y": 325,
                "image_width": 169,
                "image_height": 228
            },
            {   
                "name": "image4",
                "image_x": 699,
                "image_y": 325,
                "image_width": 159,
                "image_height": 234
            },
            {   
                "name": "image5",
                "image_x": 857,
                "image_y": 325,
                "image_width": 167,
                "image_height": 237
            },
            {   
                "name": "image6",
                "image_x": 506,
                "image_y": 572,
                "image_width": 174,
                "image_height": 208
            },
            {   
                "name": "image7",
                "image_x": 689,
                "image_y": 561,
                "image_width": 165,
                "image_height": 264
            },
            {   
                "name": "image8",
                "image_x": 865,
                "image_y": 572,
                "image_width": 158,
                "image_height": 221
            },
            {   
                "name": "image9",
                "image_x": 494,
                "image_y": 794,
                "image_width": 188,
                "image_height": 230
            },
            {   
                "name": "image10",
                "image_x": 682,
                "image_y": 794,
                "image_width": 175,
                "image_height": 230
            },
            {   
                "name": "image11",
                "image_x": 867,
                "image_y": 806,
                "image_width": 152,
                "image_height": 208
            }
        ],
        "BoxArtBigger": [
            {   
                "name": "image1",
                "image_x": 0,
                "image_y": 606,
                "image_width": 262,
                "image_height": 418,
                "rotation": 0
            },
            {   
                "name": "image2",
                "image_x": 262,
                "image_y": 606,
                "image_width": 251,
                "image_height": 418,
                "rotation": 0
            },
            {   
                "name": "image3",
                "image_x": 512,
                "image_y": 606,
                "image_width": 256,
                "image_height": 418,
                "rotation": 0
            },
            {   
                "name": "image4",
                "image_x": 768,
                "image_y": 606,
                "image_width": 256,
                "image_height": 418,
                "rotation": 0
            },
            {   
                "name": "image5",
                "image_x": 0,
                "image_y": 228,
                "image_width": 248,
                "image_height": 381,
                "rotation": 0
            },
            {   
                "name": "image6",
                "image_x": 246,
                "image_y": 228,
                "image_width": 228,
                "image_height": 381,
                "rotation": 0
            },
            {   
                "name": "image7",
                "image_x": 474,
                "image_y": 228,
                "image_width": 228,
                "image_height": 381,
                "rotation": 0
            },
            {   
                "name": "image8",
                "image_x": 702,
                "image_y": 402,
                "image_width": 200,
                "image_height": 321,
                "rotation": 90
            },
            {   
                "name": "image9",
                "image_x": 702,
                "image_y": 203,
                "image_width": 200,
                "image_height": 321,
                "rotation": 90
            },
            {   
                "name": "image10",
                "image_x": 702,
                "image_y": 0,
                "image_width": 180,
                "image_height": 225,
                "rotation": 90
            },
            {   
                "name": "image11",
                "image_x": 0,
                "image_y": 0,
                "image_width": 228,
                "image_height": 349,
                "rotation": 90
            },
            {   
                "name": "image12",
                "image_x": 350,
                "image_y": 0,
                "image_width": 228,
                "image_height": 228,
                "rotation": 90
            }
        ]
    }

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
            
            template = config_template()
            
            with open("config.json", "w") as file:
                json.dump(template, file, indent = 4)

config = get_config()
image_size = config["image_size"]["height"], config["image_size"]["width"]
image_directory = config["image_directory"]
image_amount_requirement = config["required_images"]
BoxArt2Positions = config["BoxArt2Positions"]
BoxArtBigger = config["BoxArtBigger"]
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
    image = Image.open("template/BoxArt1.png")
    
    times_iterated = 0
    x = 0
    y = 0
    for file in image_list:
        pasting_image = Image.open(f"{image_directory}{file}")

        # Pasting outer cover
        image.paste(pasting_image.resize(video_outer_cover_size), box = (x, y))
        # Pasting inner cover
        image.paste(pasting_image.resize(video_inner_cover_size), box = (x, y))

        times_iterated += 1
        x += 136
        if times_iterated % 6 == 0:
            x = 0
            y += 204

        if times_iterated >= 30:
            break

    file_name = "BoxArt1.png"
    image.save(file_name)
    
    os.system(f"quicktex encode auto {file_name}")

def BoxArt2():
    image = Image.open("template/BoxArt2.png")

    pasted_images = []

    for data in BoxArt2Positions:
        while True:
            img = choice(image_list)
            if img not in pasted_images:
                pasted_images.append(img)
                break
        
        pasting_image = Image.open(f"{image_directory}{img}")
        flipped = ImageOps.flip(pasting_image.resize((data["image_width"], data["image_height"]), Image.Resampling.LANCZOS))
        # Pasting image
        image.paste(flipped, box = (data["image_x"], data["image_y"]))

    file_name = "BoxArt2.png"
    mirrored = ImageOps.flip(image)
    mirrored.save(file_name)
    
    os.system(f"quicktex encode auto {file_name}")

def BoxArtBig():
    image = Image.new(mode = "RGB", size = (1024, 1024))
    pasted_images = []

    for data in BoxArtBigger:
        while True:
            img = choice(image_list)
            if img not in pasted_images:
                pasted_images.append(img)
                break
        
        pasting_image = Image.open(f"{image_directory}{img}")
        pasting_image = pasting_image.resize((data["image_width"], data["image_height"]), Image.Resampling.LANCZOS).transpose(Image.ROTATE_180)
        pasting_image = ImageOps.mirror(pasting_image)

        if data["rotation"] == 90:
            pasting_image = pasting_image.transpose(Image.ROTATE_90)

        ImageOps.flip(image)

        image.paste(pasting_image, box = (data["image_x"], data["image_y"]))
    
    file_name = "BoxArtBig.png"
    mirrored = ImageOps.flip(image)
    mirrored.save(file_name)
    
    os.system(f"quicktex encode auto {file_name}")

BoxArt1()
BoxArt2()
BoxArtBig()