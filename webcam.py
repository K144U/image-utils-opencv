import cv2

webcam = cv2.VideoCapture(0)  # 0 for the default webcam


while True:
    ret, frame = webcam.read()
    if not ret:
        break

    cv2.imshow('Webcam', frame)
    cv2.waitKey(40)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'Esc' to exit  
        break
webcam.release()
cv2.destroyAllWindows()