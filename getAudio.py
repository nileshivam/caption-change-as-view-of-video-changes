
import moviepy.editor as mp

def getAudio(vid,st,en,outaud):
	stN=st/1000
	enN=en/1000
	video_clip=mp.VideoFileClip(vid)
	clip = video_clip.subclip(stN,enN)
	clip.audio.write_audiofile(outaud, verbose=False, progress_bar=False)
	video_clip.reader.close()
	video_clip.audio.reader.close_proc()

