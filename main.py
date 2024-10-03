import detect
import youtube

def main():
    minutes = 0

    while True:     
        
        if (youtube.isTimeUp()):
            if (detect.detectPushup()):
                # do stuff
                print("good job!")
    
