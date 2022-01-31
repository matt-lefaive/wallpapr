import serial
import ctypes
import os
import random
import time

serialPort = serial.Serial(port='COM4', baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

dir_path = os.path.dirname(os.path.realpath(__file__))

while 1:

	# Block until data in serial port to read
	flag = serialPort.readline().decode('Ascii').strip()
	
	if flag == 'NSFW':
		print('Setting NSFW')
		wallpaper = dir_path + '/nsfw/' + random.choice(os.listdir(dir_path + '/nsfw'))
		ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
	elif flag == 'SFW':
		print('Setting SFW')
		wallpaper = dir_path + '/sfw/' + random.choice(os.listdir(dir_path + '/sfw'))
		ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
	
	time.sleep(1)

		


