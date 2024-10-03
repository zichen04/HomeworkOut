# No Exercise No Entertainment

I've been lacking in the exercise department. So I came up with this project, the idea is that this program will detect when i have a youtube video playing. And every 10 minutes it will pause my video and freeze my mouse and keyboard input (so i can't unpause). My inputs will be frozen until 10 pushups are done.

The idea originally started as "homeworkout" as in, homework workout. Instead of youtube, I was going to make myself do pushups while I was doing homework. However I realized this was a bad idea, because I would end up putting off both homework and exercise.


Currently as of 10/2/2024:

The pushup detection algorithm is fully functional. I am using OpenCV and the built in KCF tracking to track my person, and detect when pushups are performed. At the very beginning, I was trying to use masking and contours to track the person. However this proved to be very problematic, as the countours would often track things I didn't want tracked, for example it would track my shadow and then also track my hand thinking it was a seperate thing. So I read into the tracking algorithms available in the openCV library and felt KCF tracking was the best for my use case. This was an article that helped a lot -> https://broutonlab.com/blog/opencv-object-tracking/

Here is a demo of pushup tracking: https://github.com/user-attachments/assets/1bde371b-964c-4cc2-b3d1-e43cb736a7b5

