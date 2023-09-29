from keras.preprocessing.image import ImageDataGenerator
from skimage import io
import numpy as np
import os
from PIL import Image

import os
os.environ["PILLOW_DECOMPRESSION_BOMB_TOLERANCE"] = "200000000"  # Set a higher limit
from PIL import Image

# Set the path to the directory containing original images
image_directory = r'D:/Codes/projects/Wall Crack detection/images/'

# Set the desired output directory for augmented images
output_directory = r'D:/Codes/projects/Wall Crack detection/dataset/images'

# Set the image size
SIZE = 224

# Create an ImageDataGenerator with augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=40,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=(0.5, 1.5)
)

# Initialize an empty dataset to store images
dataset = []

# List all image files in the image_directory
my_images = os.listdir(image_directory)

# Loop through the images and perform data augmentation
for i, image_name in enumerate(my_images):
    if image_name.endswith('.jpg'):
        # Read the original image
        image = io.imread(image_directory + image_name)
        image = Image.fromarray(image, 'RGB')
        
        # Resize the image to the desired size
        image = image.resize((SIZE, SIZE))
        
        # Append the image to the dataset
        dataset.append(np.array(image))

# Convert the dataset to a NumPy array
x = np.array(dataset)

# Initialize a counter for augmented images
i = 0

# Generate augmented images and save them to the output directory
for batch in datagen.flow(x, batch_size=16, save_to_dir=output_directory, save_prefix='dr', save_format='jpg'):
    i += 1
    if i > 50:  # Generate 50 augmented images per original image
        break
