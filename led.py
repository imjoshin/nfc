import subprocess, settings, signal, sys
import RPi.GPIO as GPIO
from time import sleep

def set(r, g, b):
	GPIO.output(settings.RED, r)
	GPIO.output(settings.GREEN, g)
	GPIO.output(settings.BLUE, b)

def lock():
	flash = True
	for i in range(0, settings.SPINTIME * 2):
		if flash:
			set(1, 1, 0)
		else:
			set(0, 1, 0)
		flash = not flash
		sleep(.5)

def unlock():
	flash = True
	for i in range(0, settings.SPINTIME * 2):
		if flash:
			set(0, 1, 1)
		else:
			set(0, 1, 0)
		flash = not flash
		sleep(.5)

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(settings.GREEN, GPIO.OUT)
	GPIO.setup(settings.RED, GPIO.OUT)
	GPIO.setup(settings.BLUE, GPIO.OUT)
	GPIO.output(settings.GREEN, False)
	GPIO.output(settings.RED, False)
	GPIO.output(settings.BLUE, False)

def exit():
	set(0, 0, 0)
	GPIO.cleanup()
