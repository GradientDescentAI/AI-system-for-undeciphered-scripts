import cv2
import numpy as np
import os

def normalize_page(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Contrast normalization (removes yellowing)
    gray = cv2.equalizeHist(gray)

    # Threshold just to find page edges
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Find page contour
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    page_contour = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(page_contour)
    cropped = gray[y:y+h, x:x+w]

    return cropped

def find_grid_area(img):
    edges = cv2.Canny(img, 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi/180,
        threshold=200,
        minLineLength=200,
        maxLineGap=10
    )

    xs, ys = [], []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        xs.extend([x1, x2])
        ys.extend([y1, y2])

    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    return img[y_min:y_max, x_min:x_max]

