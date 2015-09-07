from django.shortcuts import render
from django.http import Http404
from mezzanine.conf import settings
from mezzanine.utils.importing import import_dotted_path
from collections import namedtuple
from . import model_class_path, fields

model_class = import_dotted_path(model_class_path)

def get_tile_details(request, notification_index):
	try:
		raw_data = model_class.objects.order_by("-%(pub_date)s" %fields)[int(notification_index)-1]
	except (IndexError, model_class.DoesNotExist):
		raise Http404
	headline = getattr(raw_data, fields["headline"], "")
	body_text = getattr(raw_data, fields["body_text"], "")
	image = getattr(raw_data, fields["image"], None)
	Notification = namedtuple("Notification", ["headline", "body_text", "image"])
	return render(request, "tile/tileconf/notification.xml", {"notification": Notification(headline, body_text, image)})