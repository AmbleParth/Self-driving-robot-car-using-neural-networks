import cv2

def detect_stop_sign():
    ss = cv2.CascadeClassifier('stop_sign.xml')
    cap = cv2.VideoCapture(0)
    cap.set(4, 480)
    cap.set(3, 480)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        SS = ss.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in SS:
            print("Stop sign detected")
            
        key = cv2.waitKey(30)
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    detect_stop_sign()
