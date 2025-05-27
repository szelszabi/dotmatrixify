from PIL import Image
import numpy as np


def color_distance(c1, c2):
    return np.linalg.norm(np.array(c1[:3]) - np.array(c2[:3]))


def edge_aware_downsample(img, window_size=4, color_threshold=30):
    pixels = np.array(img)
    h, w, _ = pixels.shape

    new_h = h // window_size
    new_w = w // window_size
    output = np.zeros((new_h, new_w, 4), dtype=np.int8)

    for y in range(new_h):
        for x in range(new_w):
            block = pixels[
                y * window_size : (y + 1) * window_size,
                x * window_size : (x + 1) * window_size,
            ].reshape(-1, 4)

            # Use the center pixel as reference for edge-aware filtering
            center = block[len(block) // 2]
            similar = np.array(
                [px for px in block if color_distance(px, center) < color_threshold]
            )

            if len(similar) == 0:
                avg_color = center  # fallback
            else:
                avg_color = similar.mean(axis=0)

            avg_color = list(map(int, avg_color))
            output[y, x] = avg_color

    return output


if __name__ == "__main__":
    # Example usage
    output_img = edge_aware_downsample(
        "input_image/hirez.png", window_size=4, color_threshold=40
    )
    output_img.save("output_image/downsampled_edge_aware.png")
