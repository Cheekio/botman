from util import hook


@hook.command
def oper(inp, nick="", conn=None):
    channel, secret=inp.split(' ')
    if secret == "ska4lyfe":
        conn.cmd("mode", [channel,'+o',nick])