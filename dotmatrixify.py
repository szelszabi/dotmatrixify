#!env/bin/python

from circle import create_circle_from_pixel
from PIL import Image
import numpy as np
from sys import argv

from convolution import edge_aware_downsample


def usage():
    print("USAGE:")
    print(
        "dotmatrixify.py -i <input_path> -o <output_path> -k <kernel_size> -r <circle_radius>"
    )
    print("-i \t Input file path")
    print("-o \t Output file path")
    print("-k \t Kernel size - NxN matrix that does the averaging")
    print("-r \t Each pixel's circle radius")
    exit(127)


def handle_args(argv: list):
    if len(argv) != 9:
        usage()

    flags = argv[1::2]

    if len(set(["-i", "-o", "-k", "-r"])) != len(set(flags)):
        usage()

    input_file_path = argv[argv.index("-i") + 1]
    output_file_path = argv[argv.index("-o") + 1]
    kernel_size = int(argv[argv.index("-k") + 1])
    circle_radius = int(argv[argv.index("-r") + 1])

    if kernel_size < 0 or circle_radius < 0:
        print("The kernel size and the radius can't be less than 0!")
        exit(126)

    return (input_file_path, output_file_path, kernel_size, circle_radius)


def dotmatrixify(
    input_image_path, output_image_path, kernel_length=20, circle_radius=10
):
    img = Image.open(input_image_path).convert("RGBA")
    pixels = np.array(img)
    h, w, _ = pixels.shape
    color_threshold = 30
    new_h = h // kernel_length
    new_w = w // kernel_length

    diameter = circle_radius * 2
    dot_matrix_data = np.zeros((new_h * diameter, new_w * diameter, 4), dtype=np.uint8)

    convolution_data = edge_aware_downsample(
        img, window_size=kernel_length, color_threshold=color_threshold
    )

    for y in range(new_h):
        for x in range(new_w):
            circle = create_circle_from_pixel(
                list(map(int, convolution_data[y, x])), radius=circle_radius
            )
            dot_matrix_data[
                y * diameter : (y + 1) * diameter, x * diameter : (x + 1) * diameter
            ] = circle

    # Save the output image
    output_img = Image.fromarray(dot_matrix_data)
    output_img.save(output_image_path)


def main(argv):
    input_file_path, output_file_path, kernel_size, circle_radius = handle_args(argv)

    dotmatrixify(input_file_path, output_file_path, kernel_size, circle_radius)


if __name__ == "__main__":
    main(argv)
