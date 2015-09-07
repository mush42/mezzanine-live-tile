from django.conf.urls import patterns, include, url
from mezzanine.core.views import direct_to_template
from . import views

urlpatterns = [
    url(r"^browserconfig/$", direct_to_template, {"template": "tile/tileconf/browserconfig.xml"}, name="browserconfig"),
    url(r"^notifications/(?P<notification_index>[1-5])/$", views.get_tile_details, name="notifications"),
  ]