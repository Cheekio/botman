"""Basically rooting my own system."""

from util import hook
from subprocess import Popen, PIPE


@hook.command
def butt(inp):
    """Basically the rooter."""
    print 'Firing one off'
    p = Popen(inp, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
    return p.communicate()[0]
    return inp + ", also you're a butt."
