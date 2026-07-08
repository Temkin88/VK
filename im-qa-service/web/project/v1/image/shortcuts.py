import json
import math
from typing import Union, Any

import io
from PIL import Image, ImageStat, ImageDraw, ImageChops


def image_to_BytesIO(image: Image) -> io.BytesIO:
    image_bytes = io.BytesIO()
    image.save(image_bytes, 'PNG')
    image_bytes.seek(0)
    return image_bytes


def validate_meta(meta: Union[list[list[int]], str]) -> bool:
    if isinstance(meta, str):
        meta = json.loads(meta)

    if isinstance(meta, list):
        for meta_item in meta:
            if not isinstance(meta_item, list) or len(meta_item) != 4:
                return False
            for item in meta_item:
                if not isinstance(item, int) and not isinstance(item, float):
                    return False
        else:
            return True
    else:
        return False


def load_image_from_path(image_path: str) -> Image:
    image = Image.open(fp=image_path)
    if image.mode != 'RGB':
        image_with_background = Image.new(
            "RGB", image.size, (255, 255, 0)
        )
        image_with_background.paste(
            image,
            mask=image.split()[3]
        )
        image = image_with_background

    return image


def get_mean_sum_and_extrema(
        image_from_request: Image,
        origin_image: Image,
        image_cut_region: list[list[int]],
        image_size: float
) -> Union[float, float, Any]:
    if len(image_cut_region) > 0:
        resulted_origin_image = ImageDraw.Draw(origin_image)
        resulted_test_image = ImageDraw.Draw(image_from_request)

        for rectangle in image_cut_region:
            mult_rectangle = tuple([
                float(math.ceil(i * image_size)) for i in rectangle
            ])
            resulted_origin_image.rectangle(
                mult_rectangle, fill=(200, 200, 200)
            )
            resulted_test_image.rectangle(
                mult_rectangle, fill=(200, 200, 200)
            )

    difference_img = ImageChops.difference(
        origin_image.convert('RGBA'),
        image_from_request.convert('RGBA')
    )

    return difference_img.convert('L').getextrema(), \
           sum(ImageStat.Stat(difference_img).mean), \
           difference_img
