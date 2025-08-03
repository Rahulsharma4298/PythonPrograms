import os
import time
from concurrent.futures import ThreadPoolExecutor
import uuid

import requests

images = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=400",
    "https://images.unsplash.com/photo-1494526585095-c41746248156?w=400",
    "https://images.unsplash.com/photo-1500534623283-312aade485b7?w=400",
    "https://images.unsplash.com/photo-1495567720989-cebdbdd97913?w=400",
    "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=400",
    "https://images.unsplash.com/photo-1432821596592-e2c18b78144f?w=400",
    "https://images.unsplash.com/photo-1433878455169-4698e60005b1?w=400",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=400",
    "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=400",
    "https://images.unsplash.com/photo-1504198453319-5ce911bafcde?w=400"
]

def download_image(url):
    try:
        resp = requests.get(url)
        if not resp.ok:
            return
        img_name = str(uuid.uuid1()) + '.jpeg'
        with open(os.path.join('images', img_name), 'wb') as file:
            file.write(resp.content)
        print(f"{img_name} was downloaded")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        results = executor.map(download_image, images)
    # [download_image(_) for _ in images]
    end = time.perf_counter()
    print(f"Completed in {(end - start):.2f} seconds")
