def convolution(
    input_image_path,
    output_image_path,
    kernel_width,
    kernel_height,
):
    from PIL import Image
    import numpy as np

    # Load the input image
    img = Image.open(input_image_path).convert("RGBA")
    img_data = np.array(img)

    # Get the dimensions of the input image
    height, width, channels = img_data.shape

    # Calculate the dimensions of the output image
    new_height = height // kernel_height
    new_width = width // kernel_width

    # Create an empty array for the compressed image
    compressed_data = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    # Perform the averaging operation
    for i in range(new_height):
        for j in range(new_width):
            # Extract the n x n block
            block = img_data[
                i * kernel_height : (i + 1) * kernel_height,
                j * kernel_width : (j + 1) * kernel_width,
                :,
            ]
            # Compute the average for each channel
            compressed_data[i, j] = block.mean(axis=(0, 1))

    # Save the output image
    output_img = Image.fromarray(compressed_data)
    output_img.save(output_image_path)


def main():
    # Compress the image by averaging 3x3 blocks
    convolution("hirez.png", "hirez_output.png", 10, 10)


if __name__ == "__main__":
    main()
