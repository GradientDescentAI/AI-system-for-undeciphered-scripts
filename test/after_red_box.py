import cv2
import numpy as np
import os

# ---------- CONFIG ----------
IMAGE_PATH = "pages_raw/signs/aftr_grid/sign_pg4.png"
OUTPUT_DIR = "output/signs"
MIN_BOX_AREA = 500  # filters noise
# ----------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

img = cv2.imread(IMAGE_PATH)
if img is None:
    raise RuntimeError("Image not found")

# Convert to HSV (best for color detection)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Red color range (two ranges because red wraps HSV)
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 | mask2

# Clean mask
kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Find contours (red boxes)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort boxes top-to-bottom, left-to-right
boxes = []
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    area = w * h
    if area > MIN_BOX_AREA:
        boxes.append((x, y, w, h))

boxes = sorted(boxes, key=lambda b: (b[1], b[0]))

START_SIGN_ID = 330

for idx, (x, y, w, h) in enumerate(boxes):
    sign_id = START_SIGN_ID + idx
    crop = img[y:y+h, x:x+w]
    filename = f"sign_{sign_id:03d}.png"
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), crop)


print(f"Extracted {len(boxes)} signs")
