import cv2
i
# get user values
imagePath = 'Test_Photo.png'
cascadePath = 'haarcascade_frontalface_default.xml'
# create the haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# detect faces
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors= 5,
    minSize = (30,30)
)
print('Found {0} faces'. format(len(faces)))
# draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)