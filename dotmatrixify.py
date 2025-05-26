from circle import create_circle_from_pixel
from PIL import Image
import numpy as np


def dotmatrixify(
    input_image_path, output_image_path, kernel_length=20, circle_radius=11
):
    # Load the input image
    img = Image.open(input_image_path).convert("RGBA")
    img_data = np.array(img)

    diameter = (circle_radius - 1) * 2

    # Get the dimensions of the input image
    height, width, channels = img_data.shape

    # Calculate the dimensions of the output image
    new_height = height // kernel_length
    new_width = width // kernel_length

    # Create an empty array for the dot matrix image
    dot_matrix_data = np.zeros(
        (new_height * diameter, new_width * diameter, channels), dtype=np.uint8
    )

    # Create circles for each pixel in the compressed image
    for i in range(new_height):
        for j in range(new_width):
            # Extract the n x n block
            block = img_data[
                i * kernel_length : (i + 1) * kernel_length,
                j * kernel_length : (j + 1) * kernel_length,
                :,
            ]
            # Compute the average for each channel
            avg_pixel = block.mean(axis=(0, 1)).astype(int)
            avg_pixel = avg_pixel.tolist()
            circle_image = create_circle_from_pixel(avg_pixel, radius=circle_radius)
            dot_matrix_data[
                i * diameter : (i + 1) * diameter, j * diameter : (j + 1) * diameter
            ] = circle_image

    # Save the output image
    output_img = Image.fromarray(dot_matrix_data)
    output_img.save(output_image_path)


def main():
    dotmatrixify("input_image/example.png", "output_image/example.png", 8, 20)


if __name__ == "__main__":
    main()
