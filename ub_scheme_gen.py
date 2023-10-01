import cv2 as cv
import numpy as np


def pixel_fix(n):
    if n < 80:
        return 0
    if 80 <= n <= 200:
        return 158
    return 255

img = cv.imread("ub_70_tri_8+2+9.jpg", cv.IMREAD_GRAYSCALE)

for i in range(len(img)):
    for j in range(len(img[0])):
        img[i][j] = pixel_fix(img[i][j])

scheme = np.zeros((70 * 20, 70 * 20), np.uint8)
for i in range(0, 1400, 20):
    for j in range(0, 1400, 20):
        part = np.array(
            [
                [
                    img[i // 20][j // 20] + 40
                    if img[i // 20][j // 20] < (255 - 40)
                    else img[i // 20][j // 20]
                    for _ in range(20)
                ]
                for _ in range(20)
            ],
            np.uint8,
        )
        cv.putText(
            part,
            str([0 + 40, 158 + 40, 255].index(int(part[0][0])) + 1),
            (3, 16),
            cv.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
        )
        part = cv.rectangle(part, (0, 0), (19, 19), (0, 0, 0), 1)
        scheme[i : i + 20, j : j + 20] = part

cv.imwrite("ub_70_tri_scheme_8+2+9.jpg", scheme)
