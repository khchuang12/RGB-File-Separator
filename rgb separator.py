import os
import shutil
from PIL import Image
import rawpy
import numpy as np

def get_average_color(image_path):
    # Check if the image is a raw file, and use rawpy for raw files
    if image_path.lower().endswith(('.arw', '.cr2', '.nef', '.dng')):
        with rawpy.imread(image_path) as raw:
            img = raw.postprocess()
    else:
        # Use PIL for other image formats
        img = Image.open(image_path)

    # Convert the image to an RGB NumPy array
    img_array = np.array(img)

    # Get the average color by computing the mean of each color channel
    r, g, b = img_array.mean(axis=(0, 1)).astype(int)

    return r, g, b

def classify_color(rgb):
    # Classify the color based on the channel with the highest intensity
    r, g, b = rgb

    if r > g and r > b:
        return "red"
    elif g > r and g > b:
        return "green"
    else:
        return "blue"

def sort_photos(input_folder):
    output_folder = input_folder
    red_folder = os.path.join(output_folder, 'red')
    green_folder = os.path.join(output_folder, 'green')
    blue_folder = os.path.join(output_folder, 'blue')

    # Create folders if they don't exist
    for folder in [red_folder, green_folder, blue_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    for filename in os.listdir(input_folder):
        # Check if the file is an image with a supported extension
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.arw', '.cr2', '.nef', '.dng')):
            image_path = os.path.join(input_folder, filename)
            average_color = get_average_color(image_path)
            apparent_color = classify_color(average_color)

            # Move the image to the corresponding color folder
            if apparent_color == "red":
                shutil.move(image_path, os.path.join(red_folder, filename))
            elif apparent_color == "green":
                shutil.move(image_path, os.path.join(green_folder, filename))
            elif apparent_color == "blue":
                shutil.move(image_path, os.path.join(blue_folder, filename))

if __name__ == '__main__':
    # Replace with the path to your input folder
    input_folder = r'your/local/folder/path'
    sort_photos(input_folder)
