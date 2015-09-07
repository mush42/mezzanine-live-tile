from django.db import models
from mezzanine.core.fields import FileField

class Notification(models.Model):
	"""A fallback notification class which can be edited in admin to provide manually edited notifications which can be pulled by windows to display in the live tile"""
	headline = models.CharField(max_length=100)
	body_text = models.CharField(max_length=240)
	image = FileField(max_length=200, upload_to='live', format='Image', null=True, blank=True)
	pub_date = models.DateTimeField("Publication Date", auto_now=True)
	
	def __unicode__(self):
		return self.headline
	
	class Meta:
		app_label = "mezzanine_live_tile"
