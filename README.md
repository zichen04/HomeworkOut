# No Exercise No Entertainment

I've been lacking in the exercise department. So I came up with this project, the idea is that this program will detect when i have a youtube video playing. And every 10 minutes it will pause my video and freeze my mouse and keyboard input (so i can't unpause). My inputs will be frozen until 10 pushups are done.
The idea originally started as "homeworkout" as in, homework workout. Instead of youtube, I was going to make myself do pushups while I was doing homework. However I realized this was a bad idea, because I would end up putting off both homework and exercise.

Currently as of 10/2/2024:
The pushup detection algorithm is fully functional. I am using OpenCV and the built in KCF tracking to track my persons, and detect when pushups are performed.

demo of pushup tracking
https://github.com/user-attachments/assets/1bde371b-964c-4cc2-b3d1-e43cb736a7b5

