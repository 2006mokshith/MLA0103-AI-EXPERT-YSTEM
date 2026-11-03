import cv2

image = cv2.imread("image.jpg", 0)
template = cv2.imread("pattern.jpg", 0)

result = cv2.matchTemplate(
    image, template, cv2.TM_CCOEFF_NORMED
)

_, maximum, _, location = cv2.minMaxLoc(result)

if maximum > 0.8:
    print("Pattern detected")
    print("Location:", location)
else:
    print("Pattern not detected")
pip install opencv-python
