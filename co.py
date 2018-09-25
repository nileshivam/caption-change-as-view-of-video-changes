import cv2
import os
from image_match.goldberg import ImageSignature
import math
import json
import sys

# Check if images "ne" and "prev" are same or not
def is_simillar(ne,prev):
  gis = ImageSignature()
  a = gis.generate_signature(ne)
  b = gis.generate_signature(prev)
  x=gis.normalized_distance(a,b)
  if(x<0.5):
    return True
  else:
    return False

def get_elid(ne,prev):
  gis = ImageSignature()
  a = gis.generate_signature(ne)
  b = gis.generate_signature(prev)
  x=gis.normalized_distance(a,b)
  return x

    
# It save the frame at specific time "time" in the video with name im
# Return the status 
def saveFrame(vidcap,time):
  vidcap.set(cv2.CAP_PROP_POS_MSEC,time)
  success,image = vidcap.read()
  return (success,image)


def find_dur(vidcap):
  length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  videotime = length/fps
  videotime=videotime*1000
  videotime=math.floor(videotime)
  x=saveFrame(vidcap,videotime)
  return videotime


def bSearch(vidcap,left,right,leftImg,rightImg):
  if((left+1==right) or (left==right)):
    return left
  mid=math.floor((left+right)/2)
  x=saveFrame(vidcap,mid);
  if(is_simillar(leftImg,x[1])):
    return bSearch(vidcap,mid,right,x[1],rightImg)
  else:
    return bSearch(vidcap,left,mid,leftImg,x[1])

def convertTime(mill):
  s=math.floor(mill/1000)
  m=math.floor(s/60)
  print("Minute:",m)
  print("Sec:",s%60)
  print("Mill:",mill%1000)


def breakWithThesHold(l,T):
  if(T==0):
    return l
  index=(-1)
  new_l=[]
  while (index+1<len(l)):
    if((not index==-1) and (prev+T<l[index+1])):
        new_l.append(prev+T)
        prev+=T
    else:
      index+=1
      prev=l[index]
      new_l.append(l[index])
  return new_l

def saveImage(vid,t,name):
  x=saveFrame(vid,t)
  cv2.imwrite(name, x[1])

def saveListImage(vid,l):
  index=0
  for x in l:
    saveImage(vid,x,"frame%d.jpg" % index)
    index+=1


def getBreaks(vid,th):
  vidcap = cv2.VideoCapture(vid)
  count=0
  doneTill=0
  iBreaks=[0]
  while True:
    x=saveFrame(vidcap,count*1000)
    if(not x[0]):
      break
    if(count==0):
      prev=x[1]
    if(not is_simillar(prev,x[1])):
      doneTill=bSearch(vidcap,(count-1)*1000,count*1000,prev,x[1])
      iBreaks.append(doneTill)                       #increase the count
      prev=x[1]
    count+=1
  iBreaks.append(find_dur(vidcap))
  new_iBreaks=breakWithThesHold(iBreaks,th*1000)
  f_ans=[]
  index=1
  while index<len(new_iBreaks):
    n_dict=(new_iBreaks[index-1],new_iBreaks[index])
    f_ans.append(n_dict)
    index+=1
  return f_ans


def IntBraks(vid):
  vidcap = cv2.VideoCapture(vid)
  l=find_dur(vidcap);
  li=[]
  li.append(0)
  li.append(l)
  new_iBreaks=breakWithThesHold(li,10*1000)
  f_ans=[]
  index=1
  while index<len(new_iBreaks):
    n_dict=(new_iBreaks[index-1],new_iBreaks[index])
    f_ans.append(n_dict)
    index+=1
  return f_ans