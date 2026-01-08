import os
import time
from time import strftime, gmtime



w=os.walk('./')
filesCount=0
filepath=[]
for dirpath,dirnames,filenames in w:
	for filename in filenames:
		if(filename[-4:]=='.flv'):
			try:
				os.system("ffmpeg --help full >ffmpeg_help.txt") #帮助文档
				T1 = time.time()
				# os.system("ffmpeg -i \""+filename+"\" -c:v libx265 -preset placebo  -level:v 5.1 -crf 0 \""+filename[:-4]+"-libx265-best.mkv\"") #智能编码 
				# os.system("ffmpeg -i \""+filename+"\" -c:v libx265 -preset veryslow  -level:v 4.2 -crf 16 \""+filename[:-4]+"-libx265-high.mkv\"") #智能编码 
				# os.system("ffmpeg -i \""+filename+"\" -c copy \""+filename[:-4]+".mkv\"")
				# inputFileName="\""+filename[:-4]+".mkv\""
				inputFileName="\""+filename+"\""
				outputFileName="\""+filename[:-4]+"-nvenc-r40-rext-bf5-p7-62-crf0.mkv\""

				convertCmd="ffmpeg -hwaccel cuda  -i "+inputFileName+" -r 40  -c:v hevc_nvenc -profile:v rext -profile_tier high -map_metadata 0  -c:a copy -bf 5 -preset p7 -level:v 6.2 -crf 0 "+outputFileName
				print("cmd=",convertCmd)
				os.system(convertCmd) #转码 

				# evaluateCmd="ffmpeg -i "+inputFileName+" -i "+outputFileName+" -frames 200 -lavfi psnr=\"stats_file="+strftime("%H-%M-%S", gmtime(T1))+"-quality.log\" -f null -"
				# print("cmd=",evaluateCmd)
				# os.system(evaluateCmd) #转码质量评估 
				# ffmpeg  -i ../卓舒晨_346647515_2024-04-30_21-19-22_0000.flv  -i 卓舒晨_346647515_2024-04-30_21-19-22_0000-libx265-high2.mkv -lavfi psnr="stats_file=psnr.log" -f null -
				# os.system("ffmpeg -i \""+filename+"\" -r 25 -c:v libx265 \""+filename[:-4]+"-r25-libx265.mkv\"") #智能编码 
				T2 = time.time()
				print('程序运行时间:%s' % (strftime("%H:%M:%S", gmtime(T2 - T1))))
			except Exception as e:
				print(e)
				pass


