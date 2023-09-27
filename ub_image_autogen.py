import cv2 as cv


def pixel_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

img = cv.imread("ub.jpg", cv.IMREAD_GRAYSCALE)

img = cv.resize(img, (70, 70), interpolation = cv.INTER_AREA)

for black in range(1, 50):
    for gray in range(1, 50):
        for white in range(1, 50):
            pixel_range = [0 for i in range(black)] + [128 for i in range(gray)] + [255 for i in range(white)]
            img1 = img.copy()

            for i in range(len(img1)):
                for j in range(len(img1[0])):
                    img1[i][j] = pixel_range[int(pixel_map(img1[i][j], 0, 255, 0, black + gray + white - 1))]

            cv.imwrite(f"ub_variants/ub_70_tri_{black}+{gray}+{white}.jpg", img1)
