import os
import sys
import time
import pyttsx3
from PIL import Image

# ===== SETTINGS =====
IMAGE_PATH = "friend.jpg"
WIDTH = 80
# ====================

chars = "@%#*+=-:. "

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def image_to_ascii(path):
    img = Image.open(path).convert("L")
    w, h = img.size
    aspect_ratio = h / w
    img = img.resize((WIDTH, int(WIDTH * aspect_ratio * 0.55)))

    pixels = img.getdata()
    ascii_str = "".join(chars[pixel * len(chars) // 256] for pixel in pixels)

    ascii_img = ""
    for i in range(0, len(ascii_str), img.width):
        ascii_img += ascii_str[i:i+img.width] + "\n"
    return ascii_img

# 🔊 DEFINE FUNCTION FIRST
def laugh_loud():
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)
    engine.setProperty("volume", 1.0)

    laughs = [
        "Hahahahahaha!",
        "HAHAHAHAHAHA!",
        "Oh my god hahahahaha!",
        "This is so funny hahahahaha!"
    ]

    for l in laughs:
        engine.say(l)

    engine.runAndWait()

# ---------- START ----------
clear()
ascii_image = image_to_ascii(IMAGE_PATH)
print(ascii_image)

laugh_loud()

print("\n😂 THIS IS YOUR FRIEND 😂")


