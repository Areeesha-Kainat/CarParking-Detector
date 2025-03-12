import cv2
import pickle

# Define parking space size
width, height = 107, 48

# Load saved parking positions or create a new list
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []

# Function to handle mouse clicks
def mouseClick(event, x, y, flags, params):
    global posList
    if event == cv2.EVENT_LBUTTONDOWN:  # Left click to add a parking spot
        posList.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:  # Right click to remove a parking spot
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                break  # Stop after removing one to avoid index issues

    # Save updated positions
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

# Read the image
img = cv2.imread('carParkImg.png')
if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Create window and set mouse callback
cv2.namedWindow("Parking Space Picker")
cv2.setMouseCallback("Parking Space Picker", mouseClick)

while True:
    img_copy = img.copy()  # Avoid modifying original image

    # Draw all parking spaces
    for pos in posList:
        cv2.rectangle(img_copy, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Parking Space Picker", img_copy)

    # Exit if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()





