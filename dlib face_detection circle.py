import cv2
import dlib


detector = dlib.get_frontal_face_detector()

def show(img):
	cv2.imshow("IMG", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



img = cv2.imread(r'C:\Users\dell\Desktop\neo.jpeg')
d = detector(img, 1)
d = d[0]

x = (d.left()+d.right())//2
y = (d.top()+d.bottom())//2
cv2.circle(img, (x, y), y//2, (255,255,255) , 5, lineType=cv2.LINE_AA)

show(img)