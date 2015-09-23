import settings, signal, sys, datetime, threading
import RPi.GPIO as GPIO
import led, motor
from time import sleep
from subprocess import Popen, PIPE, STDOUT

def main():
	last = datetime.datetime.now()
	locked = False
	motor.initMotor()
	while True:
		proc = Popen(["./scan-nfc", ""], stdout=PIPE, shell=True)
		(out, err) = proc.communicate()
		ID = out.replace("\n", "").replace("  ", "")

		delta = (datetime.datetime.now() - last).total_seconds()
		last = datetime.datetime.now()

		if ID in settings.WHITELIST:
			print "ID: \033[32m0x%s\033[0m" % (ID)
			#led.set(0, 1, 0)
			if locked:
				unlock()
			else:
				lock()
			locked = not locked
		#access denied
		else:
			print "ID: \033[31m0x%s\033[0m" % (ID)
			speak(settings.ACCESSDENIED)
			led.set(1, 0, 0)
		sleep(1)
		led.set(0, 0, 0)

def lock():
	thr = threading.Thread(target = led.unlock, args=(), kwargs={})
	thr.start()
	motor.lock()
	thr.join()

def unlock():
	speak("Access Granted.")
	thr = threading.Thread(target = led.lock, args=(), kwargs={})
	thr.start()
	motor.unlock()
	thr.join()

def speak(msg):
	wget = Popen(["echo \"%s\" | espeak -s %d -p %d" % (msg, settings.SPEAKSPEED, settings.SPEAKPITCH), ""], stdout=PIPE, stderr=STDOUT, shell=True)

def exit_handler(signal, frame):
	led.exit()
	sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)
led.setup()
main()
