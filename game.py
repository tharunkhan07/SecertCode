import time
import os
import random
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def parrot_dance(duration=3):
    """Simple ASCII parrot dance animation."""
    frames = [
        r"""
   \\
   (o>
   //\
   V_/_   """,
        r"""
   \\
   (o>
   //\
   _V\_   """,
        r"""
   \\
   (o>
   //\
   \_V_   """,
    ]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            clear()
            print(frame)
            typewriter("🎮 TERMINAL REFLEX CHALLENGE", 0.03)
            typewriter("Type the word EXACTLY before time runs out!", 0.01)
            time.sleep(0.2)

words = [
    "matrix", "kernel", "python", "terminal", "process",
    "memory", "socket", "binary", "compile", "execute",
    "encryption", "firewall", "overflow", "payload",
    "algorithm", "recursion", "exception", "deadlock",
    "segmentation", "synchronization"
]

points = 0
MAX_LEVEL = 20

# --- INTRO ---
clear()
parrot_dance(3)
input("\nPress ENTER to start...")

# --- GAME LOOP ---
for level in range(1, MAX_LEVEL + 1):
    clear()
    time_limit = max(0.5, 3 - (level * 0.12))
    word = random.choice(words)

    typewriter(f"🔥 LEVEL {level} / {MAX_LEVEL}", 0.05)
    typewriter(f"⏱️  Time limit: {time_limit:.2f} seconds", 0.04)
    typewriter(f"⭐ Points: {points}", 0.04)
    print("\nTYPE THIS WORD:")
    print(f">>> {word} <<<")

    start = time.time()
    user_input = input("\n> ")
    elapsed = time.time() - start

    if user_input != word:
        typewriter("\n❌ WRONG WORD!", 0.07)
        break

    if elapsed > time_limit:
        typewriter("\n⏰ TOO SLOW!", 0.07)
        break

    gained = int((time_limit - elapsed) * 100)
    points += max(10, gained)

    typewriter("\n✅ CORRECT!", 0.07)
    typewriter(f"⚡ Speed bonus: +{max(10, gained)}", 0.04)
    time.sleep(0.7)

else:
    clear()
    typewriter("🏆 YOU BEAT ALL 20 LEVELS!", 0.07)
    typewriter(f"🔥 FINAL SCORE: {points}", 0.07)
    sys.exit()

typewriter("\n💀 GAME OVER", 0.07)
typewriter(f"⭐ FINAL SCORE: {points}", 0.07)

