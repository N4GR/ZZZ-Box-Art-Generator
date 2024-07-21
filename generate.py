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
                        "image_x": 136,
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
                        "image_x": 408,
                        "image_y": 0,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image5",
                        "image_x": 544,
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
                        "image_x": 136,
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
                        "image_x": 408,
                        "image_y": 204,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image11",
                        "image_x": 544,
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
                        "image_x": 136,
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
                        "image_x": 408,
                        "image_y": 408,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image17",
                        "image_x": 544,
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
                        "image_x": 136,
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
                        "image_x": 408,
                        "image_y": 612,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image23",
                        "image_x": 544,
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
                        "image_x": 136,
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
                        "image_x": 408,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image29",
                        "image_x": 544,
                        "image_y": 816,
                        "image_width": 104,
                        "image_height": 178,
                        "rotation": 0
                    },
                    {
                        "name": "image30",
                        "image_x": 680,
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
                        "image_x": 682,
                        "image_y": 101,
                        "image_width": 180,
                        "image_height": 225,
                        "rotation": 0
                    },
                    {
                        "name": "image2",
                        "image_x": 861,
                        "image_y": 121,
                        "image_width": 163,
                        "image_height": 205,
                        "rotation": 0
                    },
                    {
                        "name": "image3",
                        "image_x": 523,
                        "image_y": 325,
                        "image_width": 169,
                        "image_height": 228,
                        "rotation": 0
                    },
                    {
                        "name": "image4",
                        "image_x": 699,
                        "image_y": 325,
                        "image_width": 159,
                        "image_height": 234,
                        "rotation": 0
                    },
                    {
                        "name": "image5",
                        "image_x": 857,
                        "image_y": 325,
                        "image_width": 167,
                        "image_height": 237,
                        "rotation": 0
                    },
                    {
                        "name": "image6",
                        "image_x": 506,
                        "image_y": 572,
                        "image_width": 174,
                        "image_height": 208,
                        "rotation": 0
                    },
                    {
                        "name": "image7",
                        "image_x": 689,
                        "image_y": 561,
                        "image_width": 165,
                        "image_height": 264,
                        "rotation": 0
                    },
                    {
                        "name": "image8",
                        "image_x": 865,
                        "image_y": 572,
                        "image_width": 158,
                        "image_height": 221,
                        "rotation": 0
                    },
                    {
                        "name": "image9",
                        "image_x": 494,
                        "image_y": 794,
                        "image_width": 188,
                        "image_height": 230,
                        "rotation": 0
                    },
                    {
                        "name": "image10",
                        "image_x": 682,
                        "image_y": 794,
                        "image_width": 175,
                        "image_height": 230,
                        "rotation": 0
                    },
                    {
                        "name": "image11",
                        "image_x": 867,
                        "image_y": 806,
                        "image_width": 152,
                        "image_height": 208,
                        "rotation": 0
                    }
                ]
            },
            "BoxArtBigger": {
                "canvas_size": {
                    "height": 1024,
                    "width": 1024
                },
                "positions": [
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
                        "image_width": 200,
                        "image_height": 321,
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
                        "image_height": 356,
                        "rotation": 90
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
            print("Already exists.")

    def directory(path = None, name = str) -> None:
        full_path = name if not path else f"{path}/{name}"
        
        if not os.path.isdir(full_path):
            os.mkdir(full_path)
        else:
            print("Already exists.")
    
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
            except (IOError, SyntaxError):
                print(logging().error(f"{image_directory}/{file}"))
                images.remove(file)
                error_count += 1

        print(logging().note(f"{file_count - error_count}/{file_count} usable files."))
        
        return images