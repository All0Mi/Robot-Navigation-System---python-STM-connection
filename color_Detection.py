import cv2
import numpy as np
from matplotlib import pyplot as plt

def colorDetection(imagePath, BGRColors, tolerance=60):
    """
    Detect and draw bounding boxes around regions of specified colors in an image.

    :param image_path: Path to the image file (e.g., 'image.png').
    :param hsv_colors: Target color in BGR format, e.g. 'np.array([B, G, R])'.
    :param tolerance: Tolerance for color detection.
    """
    # Load the image
    img = cv2.imread(imagePath)
    if img is None:
        raise FileNotFoundError(f"Image not found at path: {imagePath}")
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    lowerBoundColor = np.array([BGRColors[0] - tolerance, BGRColors[1] - tolerance,BGRColors[2] - tolerance])
    upperBoundColor = np.array([BGRColors[0] + tolerance,BGRColors[1] + tolerance,BGRColors[2] + tolerance])
    
    #create mask
    mask = cv2.inRange(img, lowerBoundColor, upperBoundColor)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)

    #process only the largest contour if it exists:
    if contours:
        largestContour = contours[0]
        x,y,w,h = cv2.boundingRect(largestContour)
        cv2.rectangle(imgRGB, (x, y), (x + w, y + h ), (0, 255, 0), 5)
    
    # Display
    plt.imshow(imgRGB)
    plt.axis('off')
    plt.show()



# # Example usage
# color = np.array([15, 18, 180])     # (B, G, R)
# image = "red.jpg"
# colorDetection(image, color)
