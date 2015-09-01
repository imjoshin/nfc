import subprocess, settings, signal, sys
import RPi.GPIO as GPIO

def set(r, g, b):
	GPIO.output(settings.RED, r)
	GPIO.output(settings.GREEN, g)
	GPIO.output(settings.BLUE, b)

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
