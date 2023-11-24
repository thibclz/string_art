import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def bresenheim(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1
    sign_y = 1 if dy > 0 else -1

    dx, dy = abs(dx), abs(dy)

    xx, xy, yy, yx = sign_x, 0, sign_y, 0
    if dx < dy:
        dx, dy = dy, dx
        xx, xy, yy, yx = 0, sign_y, 0, sign_x

    error = 2 * dy - dx
    y = 0
    L = []
    for x in range(dx + 1):
        L.append((x1 + xx * x + yx * y, y1 + xy * x + yy * y))

        if error >= 0:
            y += 1
            error -= 2 * dx
        error += 2 * dy
    return L


def circle_approx_error(number_of_nails, pixels_by_length):
    radius = radius = pixels_by_length // 2
    approx = np.array([[round(radius * math.cos(2 * k * np.pi / number_of_nails)), round(radius * math.sin(2 * k * np.pi / number_of_nails))] for k in range(number_of_nails)])
    perfect = np.array([[radius * math.cos(2 * k * np.pi / number_of_nails), radius *
                       math.sin(2 * k * np.pi / number_of_nails)] for k in range(number_of_nails)])
    return np.sum(np.sqrt(np.sum(np.square(perfect-approx), axis = 1)))/(number_of_nails * pixels_by_length)


def compute_approx(max_nails, max_pixels):
    subdiv = 1
    result = np.zeros((max_nails//subdiv + 1, max_pixels//subdiv + 1))
    for i in range(1, max_nails + 1, subdiv):
        for j in range(1, max_pixels + 1, subdiv):
            result[i//subdiv, j//subdiv] = circle_approx_error(i, j)
    Xl = np.arange(1, max_nails + 2, subdiv)
    Yl = np.arange(1, max_pixels + 2, subdiv)
    X, Y = np.meshgrid(Xl, Yl)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_surface(X.T, Y.T, np.log(result))
    ax.set_xlabel('$nails$', fontsize=20)
    ax.set_ylabel('$pixels$')
    plt.show()

  #TODO : for a given number of nail find a loss function to minimize to find the best numbe of pixels to take

def generate_combination_matrix(number_of_nails, pixels_by_length):
    radius = pixels_by_length // 2
    nails = np.array([(radius + math.floor(radius * math.cos(2 * k * np.pi / number_of_nails)), math.floor(
        radius + radius * math.sin(2 * k * np.pi / number_of_nails))) for k in range(number_of_nails)]) #TODO : round is an issue because it may go out of boundaries
    A = np.zeros((number_of_nails * (number_of_nails - 1) // 2, ( 2 + pixels_by_length) * ( 2 + pixels_by_length)))
    for index, (nail1, nail2) in enumerate(generate_combinations(nails)):
        A[index] = generate_vector_for_combination(nail1[0], nail1[1], nail2[0], nail2[1], pixels_by_length)
    return A

def generate_combinations(nails_coordinates):
    for nail1 in range(len(nails_coordinates) - 1):
        for nail2 in range(nail1 + 1, len(nails_coordinates)):
            yield (nails_coordinates[nail1], nails_coordinates[nail2])

def generate_vector_for_combination(x1, y1, x2, y2, pixels_by_length):
    ans = np.zeros((pixels_by_length + 2, pixels_by_length + 2), dtype = bool)
    for pixel in bresenheim(x1, y1, x2, y2) :
        ans[pixel[0] + 1, pixel[1] + 1] = True
    return ans.flatten()



if __name__ == "__main__":
    number_of_nails = 9
    pixels_by_length = 100
    # number_of_nails = 5
    # pixels_by_length = 11
    A = generate_combination_matrix(number_of_nails, pixels_by_length)

    # fig, ax = plt.subplots()
    # circle1 = plt.Circle((radius, radius), radius, color='r', fill=False)
    # plt.grid(True)
    # ax.scatter(nails[:, 0], nails[:, 1])
    # ax.add_patch(circle1)
    # plt.show()
    # print(bresenheim(0, 0, -2, 10))
    # compute_approx(10, 30)
    # print(circle_approx_error(4,4))
