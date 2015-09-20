import subprocess, settings, signal, sys, datetime, threading
import RPi.GPIO as GPIO
import led, motor
from time import sleep

def main():
	last = datetime.datetime.now()
	locked = False
	motor.initMotor()
	while True:
		proc = subprocess.Popen(["./scan-nfc", ""], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		ID = out.replace("\n", "").replace("  ", "")

		delta = (datetime.datetime.now() - last).total_seconds()
		last = datetime.datetime.now()

		if ID in settings.WHITELIST:
			print "ID: \033[32m0x%s\033[0m" % (ID)
			#led.set(0, 1, 0)
			if locked:
				thr = threading.Thread(target = led.unlock, args=(), kwargs={})
				thr.start()
				motor.unlock()
				thr.join()
			else:
				thr = threading.Thread(target = led.lock, args=(), kwargs={})
				thr.start()
				motor.lock()
				thr.join()
			locked = not locked
		else:
			print "ID: \033[31m0x%s\033[0m" % (ID)
			led.set(1, 0, 0)
		sleep(1)
		led.set(0, 0, 0)

def exit_handler(signal, frame):
	led.exit()
	sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)
led.setup()
main()
