# yodude yos people

from util import hook, http
import requests

@hook.command
def yodude(inp):
    '''.yodude <username> -- it will yo someone, dude'''
    r = requests.post('http://yofor.me/' + inp + '/BOTMAN')
    if r.status_code == 200:
      '''yo successful'''
    else:
      '''yo failed'''
