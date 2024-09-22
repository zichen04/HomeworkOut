import cv2

def detectPushup() -> int:
    nums = 0


    # create the input stream from the webcam, 0 refers to default video capture device
    webcamIn = cv2.VideoCapture(0)
    webcamIn.set(cv2.CAP_PROP_FPS, 24)

    if not webcamIn.isOpened():
        print("Could not open webcam")
        return 10

    #creating background subtractor for masking
    detectPerson = cv2.createBackgroundSubtractorMOG2()

    while True:

        ret, frame = webcamIn.read()

        #mask and object detection with contours
        mask = detectPerson.apply(frame)

        contours, _ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:

            area = cv2.contourArea(c)
            if area > 15000:
                x, y, w, h = cv2.boundingRect(c)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        
        #escape from program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcamIn.release()
    cv2.destroyAllWindows()
    
    return 10


