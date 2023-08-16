from PIL import Image
import imagehash
import os
from collections import defaultdict

# Specify the directory containing the images
image_directory = '/home/riot/convert_bag_to_images/lap_images_15_08_2023/'

# Create a dictionary to store hashes and file paths
image_hashes = defaultdict(list)

# Iterate through images and calculate hashes
for filename in os.listdir(image_directory):
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        image_path = os.path.join(image_directory, filename)
        img = Image.open(image_path)
        img_hash = imagehash.average_hash(img)
        image_hashes[img_hash].append(image_path)

# Remove duplicate images
for img_hash, paths in image_hashes.items():
    if len(paths) > 1:
        print(f"Duplicate images with hash {img_hash}:")
        for path in paths[1:]:
            os.remove(path)
            print(f"Removed: {path}")

print("Duplicate removal process completed.")

