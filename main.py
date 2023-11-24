from image_processing import *
from string_manager import *
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    number_of_nails = 50
    pixels_by_length = 100
    image = cv2.imread('./test2.jpg')
    pixels_by_length = 200
    img_final = resize_image(convert_image_in_grayscale(image), pixels_by_length)
    img_final_with_border = np.zeros((pixels_by_length + 2, pixels_by_length + 2))
    img_final_with_border[1:-1, 1:-1] = img_final
    img_final_border_flatten = img_final_with_border.ravel()/255
    A = generate_combination_matrix(number_of_nails, pixels_by_length)
    reg = LinearRegression().fit(A.T, img_final_border_flatten)
    result = reg.predict(A.T).reshape(img_final_with_border.shape)
    result = np.round((result - np.min(result))/(np.max(result) - np.min(result)) * 255)
    plt.imshow(result, cmap='gray', vmin=0, vmax=255)
    plt.show()
    