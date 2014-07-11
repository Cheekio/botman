# yodude yos people

from util import hook#, http
#import requests

@hook.command
def yodude(inp):
    return "Test Works: {0}".format(inp)
#    '''.yodude <username> -- it will yo someone, dude'''
#    r = requests.post('http://yofor.me/' + inp + '/BOTMAN')
#    if r.status_code == 200:
#        return '''yo successful'''
#    else:
#       return '''yo failed'''
