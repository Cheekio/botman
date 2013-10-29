from util import hook
import time

def run420(channel, connection):
	hours = 16-int(time.strftime('%H'))
	minutes = 20-int(time.strftime('%M'))
	seconds = 0-int(time.strftime('%S'))
	wait_time = (hours*60+minutes)*60+seconds
	east_coast = True
	if -10800 < wait_time < 0:
		wait_time += 60*60*3
		east_coast = False
	if wait_time < -10800:
		wait_time += 60*60*24
	time.sleep(wait_time)
	if east_coast:
		connection.cmd("PRIVMSG", [channel, "Happy 4:20 East Coast!"])
		time.sleep(3*60*60)
	connection.cmd("PRIVMSG", [channel, 'Happy 4:20 West Coast!'])
	run420(channel, connection)

@hook.command
@hook.singlethread
def set420(inp, nick=None, conn=None, chan=None):
	if nick=='Cheekio':
		hours = 16-int(time.strftime('%H'))
		minutes = 20-int(time.strftime('%M'))
		seconds = 0-int(time.strftime('%S'))
		wait_time = (hours*60+minutes)*60+seconds
		east_coast = True
		if -10800 < wait_time < 0:
			wait_time += 60*60*3
			east_coast = False
		if wait_time < -10800:
			wait_time += 60*60*24
		conn.cmd("PRIVMSG", [chan, 'Be seeing you... (420 alert is set)'])
		run420(chan, conn)
	else:
		conn.cmd("PRIVMSG", [chan, 'quit meddling you muppet!'])
