import co
import getAudio
import sampleBing
import sys
import os
import json
from pytube import YouTube
import time

def getCaptionBySplit(vid,st,en):
	t=30*1000
	finalCaption=""
	while st<en:
		getAudio.getAudio(vid,st,min(st+t,en),"audio.wav")
		caption=sampleBing.getCaption("audio.wav")
		os.remove("audio.wav")
		finalCaption+=caption[0]
		st+=t
	return finalCaption


def main():
	le=len(sys.argv)
	li=sys.argv
	vid=li[1]
	me=li[2]
	YouTube(vid).streams.filter(res = "360p",file_extension = "mp4", progressive=True).first().download()
	os.rename((YouTube(vid).title)+".mp4", "video.mp4")
	vid="video.mp4"
	if(me=="F"):
		breaks=co.getBreaks(vid,0)
	else:
		breaks=co.IntBraks(vid)
	f_ans=[]
	for x in breaks:
		n_dict={}
		n_dict['st']=x[0]
		n_dict['en']=x[1]
		n_dict['caption']=getCaptionBySplit(vid,x[0],x[1])
		f_ans.append(n_dict)
	r=json.dumps(f_ans)
	print(r)
  	
main()

