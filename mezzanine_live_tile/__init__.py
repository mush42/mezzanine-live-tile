"""
Check that we have a valid class to work upon in our live tile notifications
"""

from django.core.exceptions import ImproperlyConfigured
from mezzanine.utils.importing import import_dotted_path
from mezzanine.conf import settings

model_class_path, fields = settings.WINDOWS_TILE_MODEL
try:
	import_dotted_path(model_class_path)
except ImportError:
	raise ImproperlyConfigured("The WINDOWS_TILE_MODEL setting contains %s modle which can not be imported" %model_class_path)
