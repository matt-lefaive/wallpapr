import serial
import ctypes
import os
import random
import time

serialPort = serial.Serial(port='COM3', baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

previous_flag = '0'
dir_path = os.path.dirname(os.path.realpath(__file__))

while 1:

	# Wait until there is data waiting in the serial buffer
	if serialPort.in_waiting > 0:
		# Read data out of the buffer until a carriage return/new line is found
		serial_data = serialPort.readline().decode('Ascii')
		flag = serial_data[0]
		serialPort.flushInput()

		# If flag == 1, load random NSFW wallpaper, else random SFW
		if flag == '1' and previous_flag != '1':
			print('Setting NSFW')
			wallpaper = dir_path + '/nsfw/' + random.choice(os.listdir(dir_path + '/nsfw'))
			ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
			previous_flag = '1'
			time.sleep(4)
		elif flag == '2' and previous_flag != '2':
			print('Setting SFW')
			wallpaper = dir_path + '/sfw/' + random.choice(os.listdir(dir_path + '/sfw'))
			ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)
			previous_flag = '2'
			time.sleep(4)

		


