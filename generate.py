from json import dump
from log import logging
from PIL import Image

import os

class generate:
    def config(directory = None, file_name = str) -> None:
        template = {
            "BoxArt1": {
                "canvas_size": {
                    "height": 1024,
                    "width": 1024
                },
                "positions": [
                    {
                        "name": "image1",
                        "image_x": 0,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image2",
                        "image_x": 135,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image3",
                        "image_x": 272,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image4",
                        "image_x": 410,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image5",
                        "image_x": 545,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image6",
                        "image_x": 680,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image7",
                        "image_x": 0,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image8",
                        "image_x": 135,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image9",
                        "image_x": 272,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image10",
                        "image_x": 410,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image11",
                        "image_x": 545,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image12",
                        "image_x": 680,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image13",
                        "image_x": 0,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image14",
                        "image_x": 135,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image15",
                        "image_x": 272,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image16",
                        "image_x": 410,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image17",
                        "image_x": 545,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image18",
                        "image_x": 680,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image19",
                        "image_x": 0,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image20",
                        "image_x": 135,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image21",
                        "image_x": 272,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image22",
                        "image_x": 410,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image23",
                        "image_x": 545,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image24",
                        "image_x": 680,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image25",
                        "image_x": 0,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image26",
                        "image_x": 135,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image27",
                        "image_x": 272,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image28",
                        "image_x": 410,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image29",
                        "image_x": 545,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    }
                ]
            },
            "BoxArt2": {
                "canvas_size": {
                    "height": 1024,
                    "width": 1024
                },
                "positions": [
                    {
                        "name": "image1",
                        "image_x": 511,
                        "image_y": 7,
                        "image_width": 159,
                        "image_height": 224,
                        "rotation": 0
                    },
                    {
                        "name": "image2",
                        "image_x": 689,
                        "image_y": 7,
                        "image_width": 163,
                        "image_height": 212,
                        "rotation": 0
                    },
                    {
                        "name": "image3",
                        "image_x": 868,
                        "image_y": 7,
                        "image_width": 150,
                        "image_height": 210,
                        "rotation": 0
                    },
                    {
                        "name": "image4",
                        "image_x": 538,
                        "image_y": 248,
                        "image_width": 142,
                        "image_height": 202,
                        "rotation": 0
                    },
                    {
                        "name": "image5",
                        "image_x": 709,
                        "image_y": 249,
                        "image_width": 141,
                        "image_height": 212,
                        "rotation": 0
                    },
                    {
                        "name": "image6",
                        "image_x": 866,
                        "image_y": 231,
                        "image_width": 151,
                        "image_height": 219,
                        "rotation": 0
                    },
                    {
                        "name": "image7",
                        "image_x": 545,
                        "image_y": 474,
                        "image_width": 144,
                        "image_height": 214,
                        "rotation": 0
                    },
                    {
                        "name": "image8",
                        "image_x": 702,
                        "image_y": 467,
                        "image_width": 152,
                        "image_height": 214,
                        "rotation": 0
                    },
                    {
                        "name": "image9",
                        "image_x": 864,
                        "image_y": 480,
                        "image_width": 158,
                        "image_height": 211,
                        "rotation": 0
                    },
                    {
                        "name": "image10",
                        "image_x": 683,
                        "image_y": 707,
                        "image_width": 165,
                        "image_height": 199,
                        "rotation": 0
                    },
                    {
                        "name": "image11",
                        "image_x": 872,
                        "image_y": 718,
                        "image_width": 143,
                        "image_height": 180,
                        "rotation": 0
                    }
                ]
            },
            "BoxArtBig": {
                "canvas_size": {
                    "height": 1024,
                    "width": 1024
                },
                "positions": [
                    {
                        "name": "image1",
                        "image_x": 0,
                        "image_y": 0,
                        "image_width": 260,
                        "image_height": 412,
                        "rotation": 0
                    },
                    {
                        "name": "image2",
                        "image_x": 259,
                        "image_y": 0,
                        "image_width": 254,
                        "image_height": 412,
                        "rotation": 0
                    },
                    {
                        "name": "image3",
                        "image_x": 513,
                        "image_y": 0,
                        "image_width": 253,
                        "image_height": 412,
                        "rotation": 0
                    },
                    {
                        "name": "image4",
                        "image_x": 766,
                        "image_y": 0,
                        "image_width": 258,
                        "image_height": 420,
                        "rotation": 0
                    },
                    {
                        "name": "image5",
                        "image_x": 0,
                        "image_y": 412,
                        "image_width": 248,
                        "image_height": 384,
                        "rotation": 0
                    },
                    {
                        "name": "image6",
                        "image_x": 247,
                        "image_y": 412,
                        "image_width": 227,
                        "image_height": 384,
                        "rotation": 0
                    },
                    {
                        "name": "image7",
                        "image_x": 474,
                        "image_y": 412,
                        "image_width": 230,
                        "image_height": 384,
                        "rotation": 0
                    },
                    {
                        "name": "image8",
                        "image_x": 703,
                        "image_y": 420,
                        "image_width": 202,
                        "image_height": 321,
                        "rotation": 270
                    },
                    {
                        "name": "image9",
                        "image_x": 698,
                        "image_y": 622,
                        "image_width": 202,
                        "image_height": 330,
                        "rotation": 270
                    },
                    {
                        "name": "image10",
                        "image_x": 698,
                        "image_y": 818,
                        "image_width": 210,
                        "image_height": 330,
                        "rotation": 270
                    },
                    {
                        "name": "image11",
                        "image_x": 0,
                        "image_y": 796,
                        "image_width": 228,
                        "image_height": 347,
                        "rotation": 270
                    },
                    {
                        "name": "image12",
                        "image_x": 347,
                        "image_y": 796,
                        "image_width": 228,
                        "image_height": 351,
                        "rotation": 270
                    }
                ]
            }
        }

        full_path = f"{file_name}.json" if not directory else f"{directory}/{file_name}.json"

        if not os.path.isfile(full_path):
            with open(full_path, "w") as file:
                dump(template, file, indent = 4)
        else:
            print("Already exists.")

    def ini(directory = None, file_name = str):
        template = """[TextureOverrideBoxArt1]
hash = 42c77e81
this = ResourceBoxArt1

[TextureOverrideBoxArt2]
hash = 89ca37db
this = ResourceBoxArt2

[TextureOverrideBoxArtBig]
hash = 3257c5f9
this = ResourceBoxArtBig

; Resources
[ResourceBoxArtBig]
filename = BoxArtBig.dds

[ResourceBoxArt1]
filename = BoxArt1.dds

[ResourceBoxArt2]
filename = BoxArt2.dds

[ShaderOverride BoxArt Shader]
hash = 892fed88d6c0149f
allow_duplicate_hash = false
checktextureoverride = ps-t1

; Mod Generated By N4GR
; https://github.com/N4GR
; https://github.com/N4GR/ZZZ-Box-Art-Generator
        """

        full_path = f"{file_name}.ini" if not directory else f"{directory}/{file_name}.ini"

        if not os.path.isfile(full_path):
            with open(full_path, "w") as file:
                file.write(template)
        else:
            print(logging().error(f"Tried to make a file that already exists... [{full_path}]"))

    def directory(path = None, name = str) -> None:
        full_path = name if not path else f"{path}/{name}"
        
        if not os.path.isdir(full_path):
            os.mkdir(full_path)
        else:
            print(logging().error(f"Tried to make a directory that already exists... [{full_path}]"))
    
    def image_list() -> list[str]:
        image_directory = "images"
        images = os.listdir(image_directory)

        file_count = len(images)
        error_count = 0
        print(logging().note(f"Detected {file_count} files, verifying integrity..."))
        for file in images:
            try:
                with Image.open(f"{image_directory}/{file}") as img:
                    img.verify()
                
                print(logging().success(f"[{file}] is a valid image..."))
            except (IOError, SyntaxError):
                print(logging().error(f"{image_directory}/{file}"))
                images.remove(file)
                error_count += 1

        print(logging().note(f"{file_count - error_count}/{file_count} usable files."))
        
        return images