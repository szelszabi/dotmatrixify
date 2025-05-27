import png
import numpy as np


def create_circle_from_pixel(pixel, radius=10):
    """
    Create a circle from a pixel value.
    The pixel value is expected to be a list of RGBA values.
    """
    diameter = radius * 2
    image = np.zeros((diameter, diameter, 4), dtype=np.uint8)  # 3D array for RGBA

    center_x, center_y = radius, radius
    if not isinstance(pixel, list) or len(pixel) != 4:
        raise ValueError("Pixel must be a list of 4 values (R, G, B, A).")

    if sum(pixel) == 0 or pixel[3] < 255:
        return image

    for y in range(diameter):
        for x in range(diameter):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius**2:
                image[y, x] = pixel  # Assign the RGBA pixel value

    return image


def main():
    diameter, diameter = 21, 21
    pixel = [255, 0, 255, 255]  # Example pixel value (R, G, B, A)
    image = create_circle_from_pixel(pixel)
    with open("circle.png", "wb") as f:
        writer = png.Writer(diameter, diameter, bitdepth=8, alpha=True, greyscale=False)
        writer.write(f, image)


if __name__ == "__main__":
    main()
