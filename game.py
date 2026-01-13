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

# --- 100 WORDS LIST ---
words = [
    "matrix", "kernel", "python", "terminal", "process",
    "memory", "socket", "binary", "compile", "execute",
    "encryption", "firewall", "overflow", "payload",
    "algorithm", "recursion", "exception", "deadlock",
    "segmentation", "synchronization", "thread", "cache",
    "pointer", "object", "class", "method", "function",
    "loop", "condition", "array", "stack", "queue",
    "hash", "database", "query", "index", "protocol",
    "packet", "router", "switch", "node", "client",
    "server", "virtual", "cloud", "docker", "container",
    "threading", "multiprocessing", "api", "endpoint",
    "json", "xml", "yaml", "script", "debug",
    "compiletime", "runtime", "syntax", "variable",
    "constant", "module", "package", "library",
    "framework", "interface", "implementation",
    "inheritance", "polymorphism", "encapsulation",
    "abstraction", "lambda", "decorator", "iterator",
    "generator", "exceptionhandling", "assert",
    "boolean", "integer", "float", "double", "char",
    "string", "pointerarithmetic", "bitmask", "opcode",
    "interrupt", "driver", "bootloader", "firmware",
    "kernelpanic", "deadlockdetection", "concurrency",
    "asynchronous", "synchronous", "mutex", "semaphore",
    "event", "listener", "callback", "signal", "threadsafe",
    "optimization", "profiling", "benchmark", "refactor",
    "virtualization", "encryptionkey"
]

points = 0
MAX_LEVEL = 20
retry_available = True  # One-time chance

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

    failed = False
    if user_input != word:
        failed = True
        reason = "WRONG WORD"
    elif elapsed > time_limit:
        failed = True
        reason = "TOO SLOW"

    if failed:
        if retry_available:
            retry_available = False
            typewriter(f"\n⚠️ You {reason}! But here's a ONE-TIME CHANCE!", 0.07)
            typewriter("⏱️ Time limit for retry: 4.00 seconds", 0.05)
            print(f"\nTYPE THIS WORD: >>> {word} <<<")

            start = time.time()
            user_input = input("\n> ")
            elapsed = time.time() - start

            if user_input != word or elapsed > 4.0:
                typewriter("\n💀 Failed again!", 0.07)
                break
            else:
                gained = int((4.0 - elapsed) * 100)
                points += max(10, gained)
                typewriter("\n✅ CORRECT ON RETRY!", 0.07)
                typewriter(f"⚡ Speed bonus: +{max(10, gained)}", 0.04)
                time.sleep(0.7)
                continue  # move to next level
        else:
            typewriter(f"\n💀 {reason}!", 0.07)
            break

    gained = int((time_limit - elapsed) * 100)
    points += max(10, gained)
    typewriter("\n✅ CORRECT!", 0.07)
    typewriter(f"⚡ Speed bonus: +{max(10, gained)}", 0.04)
    time.sleep(0.7)

# --- GAME OVER / WIN ---
if level == MAX_LEVEL and not failed:
    clear()
    typewriter("🏆 YOU BEAT ALL 20 LEVELS!", 0.07)
    typewriter(f"🔥 FINAL SCORE: {points}", 0.07)
else:
    typewriter("\n💀 GAME OVER", 0.07)
    typewriter(f"⭐ FINAL SCORE: {points}", 0.07)
