# import soundcard as sc
# import numpy as np

# default_mic = sc.default_microphone()
# default_speaker = sc.default_speaker()

# with default_mic.recorder(samplerate=44100) as mic, default_speaker.player(samplerate=44100) as sp:
# 	tracker = 0

# 	while True:
# 		data = mic.record(numframes=1024)
# 		newData = np.array_split(data, 10)

# 		for d in newData:
# 			mean = np.mean(d)
# 			if(mean < -9):
# 				print("Low")
# 			elif(mean > 0.05):
# 				print("high" + str(tracker))
# 				tracker = tracker + 1

# 		sp.play(data)

import pyaudio
import numpy as np
import random
import os
from Naked.toolshed.shell import execute_js, muterun_js
from subprocess import STDOUT, check_output


CHUNK = 2**11
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
			  frames_per_buffer=CHUNK)

# for i in range(int(10*44100/1024)): #go for a few seconds
i = 0
j = 0
total = [0]
previousInt = 0
localPeak = False
while True:
	average = sum(total)/float(len(total))
	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
	peak=np.average(np.abs(data))*2
	num = int(250*peak/2**16)
	bars="#"*num
	total.append(num)

	arr = np.array(total)
	std = np.std(arr)
	if(num > std + average and not localPeak):
		change = True
		localPeak = True
	else:
		change = False




	previousInt = num 
	if(change):
		#os.system('tplight hsb 192.168.0.30 ' + str(random.randint(1,360)) + ' 100 ' + '100')
		try:
			execute_js('party.js')
		except:
			print("failure")
		
		test = 'peak'
	else:
		test = ''
	print("%04d %05d %03d %d %s %s"%(i,peak,average, std, bars, test))
	i = i + 1
	if(i % 50 == 0):
		total = total[int(len(total)/2):]
	if(localPeak and j > 3):
		localPeak = False;
		j = 0
	elif(localPeak):
		j = j + 1
	

stream.stop_stream()
stream.close()
p.terminate()
