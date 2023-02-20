# Write a script that can be run from the command line with the following:
# take TWO command line inputs:
# first argument being the folder with the images e.g. Pokedex
# second argument being a new folder directory, i.e. create a new folder if doesn't exist e.g. converted_Pokedex
import sys
import os
from PIL import Image

# grab the first and second argument
source_fldr_name = sys.argv[1]
output_fldr_name = sys.argv[2]
source_path = f'./image-Playground/{source_fldr_name}'

if os.path.exists(source_path):
    # create destination folder if doesn't exist
    os.makedirs(f'./image-Playground/{output_fldr_name}', exist_ok=True)

    for img in os.listdir(source_path):
        img_name, img_extension = os.path.splitext(img)
        if 'jpg' in img_extension:
            converted_img = Image.open(f'{source_path}/{img}')
            converted_img.save(f'./image-Playground/{output_fldr_name}/{img_name}.png', format='PNG')
            print(f'Image: {img} has been converted to PNG and placed in this folder: {output_fldr_name} successfully!')
else:
    print('Please input a correct source folder and try again!')