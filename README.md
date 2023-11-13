# Image Color Classifier

This Python script efficiently classifies images based on their average color and organizes them into color-specific folders. It supports a variety of image formats, including raw files.

## Features

- **Color Classification:** Determines the average color of each image by computing the mean of its RGB channels.
- **Organized Sorting:** Categorizes images into "red," "green," and "blue" folders based on their predominant color.
- **Format Compatibility:** Supports common image formats (.jpg, .jpeg, .png, .gif) and various raw file formats (.arw, .cr2, .nef, .dng).

## Dependencies

- **rawpy:** Used for reading and processing raw image files.
- **PIL (Pillow):** Handles image processing for non-raw formats.
- **NumPy:** Enables efficient numerical operations for array manipulations.

## Usage

1. **Clone Repository:**
   ```bash
   git clone https://github.com/your-username/image-color-classifier.git
2. **Navigate to Project Folder**
   ```bash
   cd image-color-classifier
3. **Install Dependencies**
   ```bash
   pip install rawpy pillow numpy
5. **Run the Script**
   ```bash
   python image_classifier.py
6. **Specify Input Folder**
   Replace the input_folder variable with the path to your local image folder in the script.

## Example

- Consider running the script on a folder containing a mix of JPEG, PNG, and RAW image files. The script will create subfolders ('red', 'green', 'blue') and organize images based on their predominant color.
```bash
python image_classifier.py

## Contributing

- Contributions are welcome! Feel free to open issues, submit feature requests, or create pull requests to enhance the functionality of the script.
