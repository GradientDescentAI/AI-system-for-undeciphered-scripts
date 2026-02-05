import cv2
import os
import csv
import numpy as np

INPUT_DIR = "signs_norm"
OUTPUT_CSV = "sign_inventory.csv"

rows = []

for fname in sorted(os.listdir(INPUT_DIR)):
    if not (fname.startswith("sign_") and fname.endswith(".png")):
        continue

    sign_id = int(fname.replace("sign_", "").replace(".png", ""))

    path = os.path.join(INPUT_DIR, fname)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Skipping unreadable file: {fname}")
        continue

    # Ensure binary
    _, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Find tight bounding box
    coords = cv2.findNonZero(bw)
    x, y, w, h = cv2.boundingRect(coords)

    glyph = bw[y:y+h, x:x+w]

    area_px = int(np.count_nonzero(glyph))

    rows.append([
        sign_id,
        fname,
        w,
        h,
        area_px
    ])

# Write CSV
with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "sign_id",
        "file_name",
        "width_px",
        "height_px",
        "area_px"
    ])
    writer.writerows(rows)

print(f"Created {OUTPUT_CSV} with {len(rows)} entries.")
