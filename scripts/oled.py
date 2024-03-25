import sys
import time
import subprocess
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c=busio.I2C(SCL, SDA)

disp=adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()

width=disp.width
height=disp.height
image=Image.new("1", (width, height))

draw=ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

font = ImageFont.load_default()

if len(sys.argv) > 1:
	if sys.argv[1] == 'init':
		draw.text((0, 0), 'INITIALIZING   h0t_d0g',  font=font, fill=255)
		draw.text((0, 15), 'PLEASE   WAIT', font=font, fill=255)
	elif sys.argv[1] == 'pass':
		draw.text((0, 0), 'PASS',  font=font, fill=255)
		draw.text((0, 15), 'THAT"S   A   HOTDOG!', font=font, fill=255)
	elif sys.argv[1] == 'fail':
		draw.text((0, 0), 'FAIL   !!!',  font=font, fill=255)
		draw.text((0, 15), 'NOT   A   HOTDOG', font=font, fill=255)
		draw.text((0, 30), 'NOT   A   HOTDOG', font=font, fill=255)
		draw.text((0, 45), 'NOT   A   HOTDOG', font=font, fill=255)
	elif sys.argv[1] == 'ready':
		draw.text((0, 15), 'PRESS   BUTTON',  font=font, fill=255)
		draw.text((0, 30), 'WHEN   READY',  font=font, fill=255)
	elif sys.argv[1] == 'calc':
		draw.text((0, 0), 'PROCESSING',  font=font, fill=255)
	elif sys.argv[1] == 'pic':
		draw.text((0, 15), 'HOLD STILL!',  font=font, fill=255)
	else:
		print("INVALID ARGUMENT")
else:
	print("INVALID ARGUMENT")

disp.image(image)
disp.show()
