import pyautogui
import cv2
import numpy
import easyocr


# determine if youtube has been playing for 10 minutes total
def isTimeUp() -> bool:

    return False

# returns how many minutes youtube has been playing
def trackMinutes() -> int:
    minutes = 0
    seconds = 0

    reader = easyocr.Reader(['en'])  

    while True:
        frame = getURL()
        # get text from frame
        url = reader.readtext(frame)

        urlStr = url[0][1]
        print(urlStr)

        cv2.imshow('URL Capture', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    return minutes

# returns frame from screen
def getURL():
    region = (110, 40, 700, 50)
    screenshot = pyautogui.screenshot(region=region)
    
    url = numpy.array(screenshot)
    url = cv2.cvtColor(url, cv2.COLOR_RGB2BGR)
    return url