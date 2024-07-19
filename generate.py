import os, json

class generate:
    def config(directory = None, file_name = str) -> None:
        template = {
                    "image_directory": "images",
                    "mods_directory": "mods",
                    "required_images": 54,
                    "image_size": {
                        "height": 1024,
                        "width": 1024
                },

                "BoxArt1": {
                    "canvas_size": {
                        "height": 1024,
                        "width": 1024
                    },

                    "cover_size": {
                        "inner": [
                            135,
                            206
                        ],
                        "outer": [
                            104,
                            206
                        ]
                    }
                },

                "BoxArt2": {
                    "positions": [
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
                    ]
                },

                "BoxArtBigger": {
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
                json.dump(template, file, indent = 4)
        else:
            print("Already exists.")

    def ini(directory = None, file_name = str):
        template = """
[TextureOverrideBoxArt1]
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

; Box Art Check.ini
[ShaderOverride BoxArt Shader]
hash = 892fed88d6c0149f
allow_duplicate_hash = false
checktextureoverride = ps-t1
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