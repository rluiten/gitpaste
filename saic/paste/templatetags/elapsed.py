import datetime
from django import template
import repoze.timeago

register = template.Library()

# If you aren't using UTC time everywhere, this line can be used
# to customize repoze.timeago:
repoze.timeago._NOW = datetime.datetime.now

@register.filter(name='elapsed')
def elapsed(timestamp):
    """
    This filter accepts a datetime and computes an elapsed time from "now".
    The elapsed time is displayed as a "humanized" string.
    Examples:
        1 minute ago
        5 minutes ago
        1 hour ago
        10 hours ago
        1 day ago
        7 days ago

    """
    return repoze.timeago.get_elapsed(timestamp)
elapsed.is_safe = True
