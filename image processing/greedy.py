import numpy as np
import cv2 as cv


def greedy_snake(image, contour, num_iterations=100, alpha=0.1):
    # Convert the image to grayscale if it's not already
    if len(image.shape) > 2:
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        image_gray = image

    # Compute image gradients
    gradient_x = cv.Sobel(image_gray, cv.CV_64F, 1, 0, ksize=3)
    gradient_y = cv.Sobel(image_gray, cv.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Iterate over the contour
    for _ in range(num_iterations):
        for i in range(len(contour)):
            # Convert contour coordinates to integers
            x, y = map(int, contour[i])

            # Compute local energy using image gradients
            energy = gradient_magnitude[y, x]

            # Move the point greedily in the direction of minimum energy
            min_energy = energy
            best_move = (0, 0)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x = x + dx
                    new_y = y + dy
                    new_energy = gradient_magnitude[new_y, new_x]
                    if new_energy < min_energy:
                        min_energy = new_energy
                        best_move = (dx, dy)

            # Update the contour point
            contour[i] = (x + alpha * best_move[0], y + alpha * best_move[1])

    return contour


# Example usage
img = cv.imread('0001.jpg')
initial_contour = [(100, 100), (150, 150), (200, 100)
                   ]  # Initial contour coordinates
final_contour = greedy_snake(img, initial_contour)

# Draw the final contour on the image
for point in final_contour:
    cv.circle(img, (int(point[0]), int(point[1])), 3, (0, 255, 0), -1)

# Display the result
cv.imshow('Greedy Snake Result', img)
cv.waitKey(0)
cv.destroyAllWindows()
