# Zenless Zone Zero Box Art Mod Generator

ZZZ Box Art Generator is a quick multi-threaded tool that will allow people to seamlessly modify the VHS tapes, posters and more in your store, Random Play. This tool is simple to use, you drop the images into the images directory, launch up the script providing it with a name for your mod and the tool will do the rest.

![Cover Image](https://i.imgur.com/jrytysQ.png)
![Cover Image 2](https://i.imgur.com/HaeYoQh.jpeg)
![Cover Image 3](https://i.imgur.com/C4q37LW.jpeg)

## Download & Install

This section will tell you how to download and Install the latest version of ZZZ Box Art Generator along with its dependencies to get the ball rolling. If you already have python installed and understand how to install dependencies; you only need to download the [ImageMagick](https://imagemagick.org/script/download.php#windows) library and you can skip these steps.

> [!IMPORTANT]
> This tool will not function without its dependencies, ensure these steps are followed thoroughly.

1. Download the latest version of the tool.
    - Click on versions, or head to this link for the latest download: [GitHub Release](https://github.com/N4GR/ZZZ-Box-Art-Generator/releases/lates)
    - Under Assets, click the N4GR-Box-Art-Gen-v*.zip to begin the download.
    - Move the archive to a desired location.
2. Extract the archive using tools like [7Zip](https://www.7-zip.org/) or [WinRAR](https://www.win-rar.com), whatever works for you.
![Extraction context menu](https://i.imgur.com/lboVjhl.png)

3. Head over to [Python](https://www.python.org/downloads/)'s website and download the latest version of python.
> [!WARNING]
> Make sure "Add to PATH" is a selected option when installing python.
4. Head over to to [ImageMagick](https://imagemagick.org/script/download.php#windows)'s website, this contains libraries for converting PNG to DLL. Once there, click on the latest version to download and install it.
![ImageMagick Install](https://i.imgur.com/UeZvZOD.png)

5. Once python is installed, open terminal by pressing the windows key and searching for it.
![Terminal Navigation](https://i.imgur.com/pRSIbIg.png)
    - Verify Python is working using the following command in terminal:
```
python --version
```
which should output:
![Python Image](https://i.imgur.com/YeqxO7t.png)

6. Close the terminal and head into the ZZZ-Box-Art folder you extracted earlier.
    - Rick click an empty space inside the folder and you should see "Open in Terminal"
    - Select that option and it should launch the terminal inside the directory.
7. Run the following command in the terminal to install the dependencies for the tool:
    - Wait for the download to complete before following onto the next step.
```
pip install -r "requirements.txt"
```
8. Congratulations, you now have a fully functioning version of the tool!


## Usage/Examples

Using the tool is definitely easier than installing it, this section will guide you through the process of actually generating the mod.

1. Obtain images.
- These can be images you have gathered online or created yourself (Lucky you!)
- For the program to function, there's a requirement of 53 images that need to be populated in the images/ directory, this is because otherwise there will be duplicate images everywhere.
- If you're looking to just test the tool, I have a sample of 53 images you can use: [test-images.zip](https://github.com/N4GR/ZZZ-Box-Art-Generator/releases/download/v1/test-images.zip)
> [!NOTE]
> Ensure the images are appropriately proportioned; a square image isn't going to look nice being stretched to a rectangle!

4. To run the script, use the following command:
```
python .\main.py
```
5. Add your images to the UI using the + button, once all 53 images have been populated, the start button is displayed.
6. Click on the start button and enter in your mod name and the directory you want the mod to export to.
5. Let the script do it's thing, once it's complete you will see a green tick.
6. Navigate to the export folder you selected and you should see a folder with the name you given the tool, this folder should containg:
- Previews directory containing PNG previews.
- DDS files.
- Populated .ini file with hashes.

![generated folder](https://i.imgur.com/wMNT7R3.png)

7. Move the generated folder into your mods directory of your model importer for ZZZ.
8. Launch your game and ensure the mod is functioning.
9. Pat yourself on the back!

> [!NOTE]
> Make sure you aren't launching your newly generated mod alongside another mod that modifies the same area - they won't work together.

## License

[ZZZ Box Art Generator](https://github.com/N4GR/ZZZ-Box-Art-Generator) © 2024 by [N4GR](https://github.com/N4GR) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
