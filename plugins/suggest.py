from xml.dom import minidom
import json
import random
import re

from util import hook, http


@hook.command
def suggest(inp, inp_unstripped=''):
    ".suggest [#n] <phrase> -- gets a random/the nth suggested google search"

    inp = inp_unstripped
    m = re.match('^#(\d+) (.+)$', inp)
    if m:
        num, inp = m.groups()
        num = int(num)
        if num > 10:
            return 'can only get first ten suggestions'
    else:
        num = 0

    #page = http.get('http://suggestqueries.google.com/complete/search', output='json', client='hp', q=inp)
    page = http.get('http://suggestqueries.google.com/complete/search', output='toolbar', hl='en', q=inp)

    xml = minidom.parseString(page)
    suggestions = xml.getElementsByTagName("CompleteSuggestion")

    #page_json = page.split('(', 1)[1][:-1]
    #suggestions = json.loads(page_json)[1]
    if not suggestions:
        return 'no suggestions found'
    if num:
        if len(suggestions) + 1 <= num:
            return 'only got %d suggestions' % len(suggestions)
        out = suggestions[num-1].childNodes[0].getAttribute('data')
        out = suggestions[num - 1]
    else:
        choice = random.randint(1, len(suggestions))-1
        out = suggestions[choice].childNodes[0].getAttribute('data')
    return '#%d: %s' % (choice+1, out)
