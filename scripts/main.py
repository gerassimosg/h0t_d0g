import os
import sys
import time
import RPi.GPIO as GPIO

sw=17
init="bash /home/jer/h0t_d0g/init.sh"
ready="bash /home/jer/h0t_d0g/ready.sh"
calc="bash /home/jer/h0t_d0g/calc.sh"
pic="bash /home/jer/h0t_d0g/pic.sh"
take_pic="rpicam-jpeg -t 2000 -o /home/jer/h0t_d0g/pic.jpg"
pic_test="/home/jer/h0t_d0g/pic.jpg"
pass_test="bash /home/jer/h0t_d0g/pass.sh"
fail_test="bash /home/jer/h0t_d0g/fail.sh"
model_test="/home/jer/h0t_d0g/yolov8n.pt"
results_test="/home/jer/h0t_d0g/yolov8n.pt"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN)

def wait_for_switch():
	while not (GPIO.input(sw)):
		time.sleep(0.1)

os.system(init)

from ultralytics import YOLO
model=YOLO(model_test)

os.system(ready)

while True:
	results_flag=False

	wait_for_switch()
	os.system(pic)
	os.system(take_pic)

	os.system(calc)
	results=model(pic_test, conf=0.5)
	model_names=results[0].names
	model_class=results[0].boxes.cls

	for i in range(len(model_class)):
		if model_names[int(model_class[i])] == 'hot dog':
			results_flag=True
			break

	if results_flag:
		os.system(pass_test)
	else:
		os.system(fail_test)
