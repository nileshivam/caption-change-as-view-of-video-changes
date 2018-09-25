---------------------------------------------------------------------------

About the package:
It will generate captions of youtube video as the view of video changes.

Example:

For example, the Video https://www.youtube.com/watch?v=EkWfwRPyTG8

In this video from time 00:00:00 to 00:00:06 the view the video is same. And from 00:00:06 to
00:00:09 the view is same. So, there is a change at 00:00:06 and 00:00:09. So, we can load captions from 00:00:00-00:00:06 and 00:00:06-00:00:09 together.

---------------------------------------------------------------------------

Beofore you run:

Python Packages you will need:
numpy, scipy, image_match, opencv-python, pytube, ez_setup, moviepy, requests, ffmpeg-python

Here's how you download them"

pip3 install numpy
pip3 install scipy
pip3 install image_match
pip3 install opencv-python
pip3 install pytube
pip3 install ez_setup
pip3 install moviepy
pip3 install requests
pip3 install ffmpeg-python

In samplebing.py you have to add your subscription key in "self.sub_key".

---------------------------------------------------------------------------

How You run:

You can run this script like this: 

python integreate.py https://www.youtube.com/watch?v=EkWfwRPyTG8 F

Here F will give you captions accroding as view of video changes.

python integreate.py https://www.youtube.com/watch?v=EkWfwRPyTG8 T 
This will give you captions in every 10 seconds.

If you have any questions, mail me at: dwivedinilesh11@gmail.com

---------------------------------------------------------------------------
