import picamera
from time import sleep
import datetime as dt
import os, sys



camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
camera.framerate = 25
max_files = 15
car_name = "dmclark"
camera.annotate_text = car_name + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

end_recording = False
#time_Interval = 60
time_Interval = 1200

def start_recording():
	f_name = str(next_file()) + ".h264"
	camera.start_recording(f_name)

def split():
	stop()
	start_recording()

def stop():
	camera.stop_recording()
	

def next_file():
	# Open a file 
	log = open("log.txt", "rw+")
	num_str = log.read(10);
	
	index = int(num_str) + 1
	
	print "Read String is : ", index
	if index >= max_files:
		index = 0
	log.seek(0, 0)
	log.write( str(index) +"           " )
	# Close opend file
	log.close()


	#try:
		#sys.stdout.close()
	#except:
		#pass
	try:
		sys.stderr.close()
	except:
		pass


	return index

def loop_recording():
	i = 0
	end_recording = False
	start_recording()
	while (not end_recording):
		if i >= 20:
			end_recording = True
		


		for x in xrange(1,(time_Interval * 10)):
			camera.annotate_text = car_name + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			sleep(.1)


		split()
		i = i + 1





loop_recording()















































