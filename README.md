# No Exercise No Entertainment

I've been lacking in the exercise department. So I came up with this project, the idea is that this program will detect when i have a youtube video playing. And every 10 minutes it will pause my video and freeze my mouse and keyboard input (so i can't unpause). My inputs will be frozen until 10 pushups are done.

The idea originally started as "homeworkout" as in, homework workout. Instead of youtube, I was going to make myself do pushups while I was doing homework. However I realized this was a bad idea, because I would end up putting off both homework and exercise.
<br />
<br />
<br />

**As for the pushup detection algorithm.** I am using OpenCV and the built in KCF tracking to track my person. Originally, I was trying to create my own tracking algorithm with mask and contours. However countours would often track things I didn't want tracked, like it would track my shadow. So I read into the tracking algorithms available in the openCV library and felt KCF tracking was the best for my use case. This was an article that helped a lot -> https://broutonlab.com/blog/opencv-object-tracking/

Here is a demo of pushup tracking: https://github.com/user-attachments/assets/1bde371b-964c-4cc2-b3d1-e43cb736a7b5 
<br />
<br />
<br />

**For detecting whether or not youtube is playing a video.** I am using the easyocr library to take frames from my display. It checks for if there is a youtube . com / watch, and it also checks for if a certain threshold of movement on the screen is met. If both conditions are true then it is determined that youtube is running.

There are some major limitations to this, currently it only works if your chrome tab is taking up the entire screen. And it also doesn't work if the youtube video is fullscreened, because then it cannot find the URL. I realize that I could probably instead make this project a chrome extension, which would then easily let me check if a youtube video was playing. However I would have to rewrite pretty much everything, as compiling my python code to JS would mean the python libraries i'm using will not work.
