from io import BytesIO
from PIL import Image
from colorthief import ColorThief
import colorsys
import numpy as np

def load_image(file_bytes: bytes) -> Image.Image:
    return Image.open(BytesIO(file_bytes)).convert("RGB")

def dominant_rgb(file_bytes: bytes) -> tuple[int, int, int]:
    ct = ColorThief(BytesIO(file_bytes))
    r, g, b = ct.get_color(quality=1)
    return (r, g, b)

def rgb_to_hsv_deg(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    r, g, b = [v/255.0 for v in rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return (h*360.0, s*100.0, v*100.0)

def hue_diff(h1: float, h2: float) -> float:
    d = abs(h1 - h2) % 360.0
    return min(d, 360.0 - d)

def image_avg_rgb(file_bytes: bytes) -> tuple[int, int, int]:
    img = load_image(file_bytes)
    arr = np.array(img)
    mean = arr.reshape(-1, 3).mean(axis=0)
    return tuple(int(x) for x in mean)