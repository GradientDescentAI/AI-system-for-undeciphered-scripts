import os

DIR = "output/signs"   # change if needed
PREFIX = "sign_"       # or "crop_"
START = 220
END = 327

for i in range(START, END + 1):
    filename = f"{PREFIX}{i:03d}.png"
    path = os.path.join(DIR, filename)

    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted {filename}")
    else:
        print(f"Missing {filename}")
