from subprocess import call
from util import hook

@hook.command
@hook.singlethread
def rebase(inp):
    call("git", "pull", "origin", "master")
    return "Well, if that's going to work, then it did."
