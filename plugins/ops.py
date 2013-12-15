"""
Written by @waltz.
"""

from util import hook

@hook.command
def ops(input, nick=None, conn=None, chan=None):
    # """Grants operator priveleges to the requesting user."""
    conn.cmd('MODE', [ chan, '+o', nick ])
