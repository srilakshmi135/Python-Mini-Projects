import cv2

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

image = cv2.imread("sample_image.jpg")

print("Image loaded:", image is not None)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5
)

print("Faces detected:", len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x+w, y+h),
        (255, 0, 0),
        2
    )

cv2.imshow("Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Face detection completed!")