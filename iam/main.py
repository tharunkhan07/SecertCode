import os
import time
from PIL import Image
from gtts import gTTS

# ===== SETTINGS =====
IMAGE_PATH = "friend.jpg"
WIDTH = 80
# ====================

chars = "@%#*+=-:. "

def clear():
    os.system("clear")

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

def laugh_loud():
    text = (
        "Hahahahahaha! "
        "Oh my god hahahahaha! "
        "This is so funny hahahahaha!"
    )

    tts = gTTS(text=text, lang="en")
    tts.save("laugh.mp3")

    os.system("termux-media-player play laugh.mp3")

# ---------- START ----------
clear()
ascii_image = image_to_ascii(IMAGE_PATH)
print(ascii_image)

laugh_loud()

print("\n😂 THIS IS YOUR FRIEND 😂")
