from typing import Tuple, List, Dict
from color_utils import rgb_to_hsv_deg, hue_diff

def classify_undertone(rgb: Tuple[int, int, int]) -> str:
    r, g, b = rgb
    if r > b + 20:
        return "Warm"
    elif b > r + 20:
        return "Cool"
    else:
        return "Neutral"

def harmony_type(hue1: float, hue2: float) -> str:
    d = hue_diff(hue1, hue2)
    if abs(d - 180) <= 15:
        return "Complementary"
    elif d <= 30:
        return "Analogous"
    else:
        return "Clashing"

PALETTES: Dict[str, List[str]] = {
    "Warm":    ["Olive", "Coral", "Mustard", "Cream", "Red-Orange"],
    "Cool":    ["Navy", "Rose", "Emerald", "Gray", "Lavender"],
    "Neutral": ["Beige", "White", "Teal", "Charcoal", "Soft Pink"],
}