from util import http, hook


@hook.command(autohelp=False)
def vegfest(inp, say=None):
    ".vegfest -- gets current number of facebook attendees for the 2014 Worcester VegFest"
    data = http.get_json("https://worcester-vegfest-attendees.herokuapp.com/api")
    say("Worcester VegFest has " + data['number_of_event_attendees'] + " attendees on facebook.")
