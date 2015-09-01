import subprocess, settings, signal, sys
import RPi.GPIO as GPIO
import led
from time import sleep

def main():
	while True:
		proc = subprocess.Popen(["./scan-nfc", ""], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		ID = out.replace("\n", "").replace("  ", "")
		if ID in settings.WHITELIST:
			print "ID: \033[32m0x%s\033[0m" % (ID)
			led.set(0, 1, 0)
		else:
			print "ID: \033[31m0x%s\033[0m" % (ID)
			led.set(1, 0, 0)
		sleep(.5)
		led.set(0, 0, 0)

def exit_handler(signal, frame):
	led.exit()
	sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)
led.setup()
main()
