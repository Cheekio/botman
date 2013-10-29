from util import hook
import time

@hook.command
@hook.singlethread
def wait(inp):
	try:
		if int(inp) < 20000:
			time.sleep(int(inp))
			return inp
	except:
		return 'not a number dumbass'
