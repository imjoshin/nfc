import RPi.GPIO as GPIO
from time import sleep
import motorVars as M
import settings, struct, readline, fcntl, termios, sys

def lock():
	#print "Locking door - spinning motor backward for %d seconds." % (settings.SPINTIME)
	spinMotor("backward", settings.SPINTIME)

def unlock():
	#print "Unlocking door - spinning motor forward for %d seconds." % (settings.SPINTIME)
	spinMotor("forward", settings.SPINTIME)

def spinMotor(direction, length):
	if(direction == "forward"):
		GPIO.output(M.F1,GPIO.HIGH)
		GPIO.output(M.B1,GPIO.LOW)
		GPIO.output(M.O1,GPIO.HIGH)
	else:
		GPIO.output(M.F1,GPIO.LOW)
		GPIO.output(M.B1,GPIO.HIGH)
		GPIO.output(M.O1,GPIO.HIGH)

	sleep(length)
	GPIO.output(M.O1,GPIO.LOW)
	GPIO.output(M.O2,GPIO.LOW)

def blank_current_readline():
	# Next line said to be reasonably portable for various Unixes
	(rows,cols) = struct.unpack('hh', fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ,'1234'))

	text_len = len(readline.get_line_buffer())+2

	# ANSI escape sequences (All VT100 except ESC[0G)
	sys.stdout.write('\x1b[1A')                         # Move cursor up
	sys.stdout.write('\x1b[0G')                         # Move to start of line
	sys.stdout.write('\x1b[2K')                         # Clear current line

def initMotor():
	print "Setting up GPIO..."

	GPIO.setmode(GPIO.BOARD)
	initMotor1()
	initMotor2()
	blank_current_readline()
	print "Setting up GPIO... Completed!"

def initMotor1():
	print "Configuring Motor 1..."
	GPIO.setup(M.F1,GPIO.OUT)
	GPIO.setup(M.B1,GPIO.OUT)
	GPIO.setup(M.O1,GPIO.OUT)

	blank_current_readline()
	print "Configuring Motor 1... Completed!"

def initMotor2():
	print "Configuring Motor 2..."
	GPIO.setup(M.F2,GPIO.OUT)
	GPIO.setup(M.B2,GPIO.OUT)
	GPIO.setup(M.O2,GPIO.OUT)

	blank_current_readline()
	print "Configuring Motor 2... Completed!"
