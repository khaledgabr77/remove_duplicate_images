# Remove Duplicate Images

To remove duplicate images from a collection, you can use image `hashing` techniques. Image `hashing` involves generating a unique fingerprint for each image based on its pixel values. Here's a high-level overview of the process:

- **Calculate Image Hashes:** For each image in your collection, calculate its hash using algorithms like `Average Hash`, `Difference Hash`, or `DCT Hash`.

- **Identify Duplicates:** Compare the generated hashes of all the images to identify duplicate images. Images with the same hash are likely duplicates.

- **Remove Duplicates:** Once you've identified duplicate images, you can remove the duplicates and keep only one instance of each unique image.

## Before Running the Code

Before running the code, specify the directory containing the images `line 7`:

```python
image_directory = "path/to/images"
```

## Run the Code

```bash
python3 hashImages.py
```

Please replace `"path/to/images"` with the actual path to the directory containing your images.
