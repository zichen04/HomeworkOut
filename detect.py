import cv2
import cv2.legacy

def detectPushup() -> int:
    nums = 0
    pushup = 0
    isFirst = True
    initialYPos = 0

    # create the input stream from the webcam, 0 refers to default video capture device
    webcamIn = cv2.VideoCapture(0)
    webcamIn.set(cv2.CAP_PROP_FPS, 24)

    if not webcamIn.isOpened():
        print("Could not open webcam")
        return 10

    ret, frame = webcamIn.read()

    # create a bbox and intialize a KCF tracker object
    bbox = (180, 250, 450, 200)
    boxCenter = (int(bbox[0] + 0.5*bbox[2]), int(bbox[1] + 0.5*bbox[3]))
    print(f"x: {bbox[0]}, y: {bbox[1]}, width: {bbox[2]}, height: {bbox[3]}")

    trackPerson = cv2.legacy.TrackerKCF.create()
    
    trackPerson.init(frame, bbox)
    
    # give the user 15 seconds to get into position
    for i in range(15):
        frame[:] = 0
        cv2.putText(frame, str(15 - i), (320, 240), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 255), 2)
        cv2.imshow("Tracking", frame)
        cv2.waitKey(1000)

    while True:

        ret, frame = webcamIn.read()

        # Update the tracker with the new frame
        success, bbox = trackPerson.update(frame)

        if success:
            # draw the bounding box
            x, y, w, h = [int(v) for v in bbox]
            boxCenter = (int(x + 0.5*w), int(y + 0.5*h))

            if isFirst:
                initialYPos = boxCenter[1]
                isFirst = False
            else:
                if boxCenter[1] > initialYPos + 27: 
                    pushup = 1
                elif boxCenter[1] < initialYPos + 5:
                    nums += pushup
                    pushup = 0

            cv2.putText(frame, str(boxCenter[1]), (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 255), 2)
            cv2.putText(frame, str(nums), (0, 100), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle
            cv2.circle(frame, boxCenter, 2, (0, 0, 255), 2)  # point

            boxCenter = (x + 0.5*w, y + 0.5*h)

        else: 
            # If tracking fails, display a message
            cv2.putText(frame, "Tracking failed", (350, 350), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 0, 255), 2)

        # Display the frame with the tracking result
        cv2.imshow("Tracking", frame)

            
        #escape from program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcamIn.release()
    cv2.destroyAllWindows()
    
    return 10


