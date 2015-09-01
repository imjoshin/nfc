import subprocess, settings, signal, sys
import RPi.GPIO as GPIO
import led
from time import sleep

def main():
	while True:
		for r in range(0, 2):
			for g in range(0, 2):
				for b in range(0, 2):
					if r+g+b is 0:
						continue
					led.set(r, g, b)
					sleep(.1)	

def exit_handler(signal, frame):
	led.exit()
	sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)
led.setup()
main()
