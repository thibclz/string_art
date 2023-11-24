import cv2
import numpy as np

def convert_image_in_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def resize_image(image, pixels_per_line):

    return cv2.resize(image, (pixels_per_line, pixels_per_line))

if __name__ == "__main__" :
    image = cv2.imread('./test1.jpg')
    pixels_by_length = 200
    img_final = resize_image(convert_image_in_grayscale(image), pixels_by_length)
    # cv2.imwrite('kqjsfd.png', img_final)
    img_final_with_border = np.zeros((pixels_by_length + 2, pixels_by_length + 2))
    img_final_with_border[1:-1, 1:-1] = img_final
    print(img_final_with_border.flatten())