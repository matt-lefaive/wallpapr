import serial
import ctypes
import os
import random
import time

serialPort = serial.Serial(port='COM4', baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

dir_path = os.path.dirname(os.path.realpath(__file__))

while True:

	# Block until data in serial buffer to read
	flag = serialPort.readline().decode('Ascii').strip()
	
	if flag == 'a':
		print('Setting a')
		wallpaper = dir_path + '/a/' + random.choice(os.listdir(dir_path + '/a'))
		ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
	elif flag == 'b':
		print('Setting SFW')
		wallpaper = dir_path + '/b/' + random.choice(os.listdir(dir_path + '/b'))
		ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
	
	time.sleep(1)

		


