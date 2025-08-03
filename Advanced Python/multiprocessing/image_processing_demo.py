import os
import time
from concurrent.futures import ProcessPoolExecutor

from PIL import Image, ImageFilter


def process_image(image_path: str, output_dir: str = "processed_images") -> str | None:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        img = Image.open(image_path)
        img_grayscale = img.convert('L')
        img_sharp = img_grayscale.filter(ImageFilter.SHARPEN)
        img_processed = img_sharp.filter(ImageFilter.GaussianBlur(radius=2))

        file_name = os.path.basename(image_path)
        output_path = os.path.join(output_dir, f"processed_{file_name}")
        img_processed.save(output_path)
        print(f"Processed image {output_path} saved")
        return output_path

    except (FileNotFoundError, Exception) as e:
        print(e)
        return None

if __name__ == '__main__':
    images_dir = os.path.abspath('../multithreading/images')
    images = [os.path.join(images_dir, filename) for filename in os.listdir(images_dir)
              if filename.lower().endswith('.jpeg')]

    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        result = executor.map(process_image, images)

    end = time.perf_counter()
    print(f"Completed in {(end - start):.2f} seconds")

