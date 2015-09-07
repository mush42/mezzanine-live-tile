from __future__ import unicode_literals
from mezzanine import template
from mezzanine.conf import settings
from textwrap import wrap
from . import strip_all_white_space

register = template.Library()

@register.simple_tag(takes_context=True)
def text_node_for(context, text):
	"""Outputs the text node with the forloop.counter incremented"""
	return ('<text id="%d">%s</text>' %(context["forloop"]["counter"]+1, text))

@register.assignment_tag
def wrap_text(paragraph, line_count, min_char_per_line=0):
	"""Wraps the given text to the specified number of lines."""
	one_string = strip_all_white_space(paragraph)
	if min_char_per_line:
		lines = wrap(one_string, width=min_char_per_line)
		try:
			return lines[:line_count]
		except IndexError:
			return lines
	else:
		return wrap(one_string, len(one_string)/line_count)

@register.assignment_tag
def counter(num):
	"""Returns a list of numbers indexed based in 1 to use as a counter."""
	return [i+1 for i in range(int(num))]

@register.inclusion_tag('tile/tileconf/tile_meta.html')
def tile_meta(app_name=""):
	"""Renders meta tags required for windows tile"""   
	app_name = app_name if app_name else settings.SITE_TITLE
	return {"app_name": app_name}
