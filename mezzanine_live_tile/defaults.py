from __future__ import unicode_literals
from django.conf import settings
from mezzanine.conf import register_setting

cycle_choices = [
  "Cycle for all tile sizes(default)",
  "Cycle for medium tiles",
  "Cycle for wide tiles",
  "Cycle for large tiles",
  "Only cycle for medium or wide tiles",
  "Only cycle for medium or large tiles",
  "Only cycle for wide or large tiles"
 ]

register_setting(
    name="TILE_COLOR",
	label="Tile Color:",
    description="Value of the color to use in windows tile.",
    editable=True,
    default="009900",
)

register_setting(
    name="LIVE_TILE_UPDATES_COUNT",
	label="Live Tile Notification Quantity:",
    description="How many notifications windows will display/cycle between in the live tile (maximum 5).",
    choices=[(i+1, str(i+1)) for i in range(5)],
	editable=True,
    default=5,
)

register_setting(
    name="UPDATE_FREQUENCY",
    label="Update Pulling Frequeancy:",
	description="How often windows will pull new notifications from your server.",
    editable=True,
    choices=[
		(30, "Every 30 minutes"),
		(60, "Every Hour"),
		(360, "Every 6 hours"),
		(720, "Every 12 hours"),
		(1440, "Every Day")],
	default=60,
)

register_setting(
    name="TILE_BRANDING",
    label="Live Tile Branding Type:",
	description="What windows will display inside your live tile.",
    editable=True,
    choices=[
		("none", "Nothing"),
		("logo", "Website's Favicon"),
		("name", "Website's Name (not supported in medium size tiles)"),],
	default="logo",
)

register_setting(
    name="CYCLE_OPTION",
    label="Live Tile Cycling Method:",
	description="How windows will cycle between notifications in your live tile.",
    choices=[(i+1, cycle_choices[i]) for i in range(7)],
	editable=True,
    default=1,
)

register_setting(
    name="WINDOWS_TILE_MODEL",
	description="A tuple containing Dotted path to the model class and dictionary mapping from tile variables to model fields.",
	editable=False,
    default=("mezzanine.blog.models.BlogPost", {"headline":"title", "body_text":"description", "image":"featured_image", "pub_date":"publish_date"},) if "mezzanine.blog" in settings.INSTALLED_APPS else ("tile.models.Notification", {"headline":"headline", "body_text":"body_text", "image":"image", "pub_date":"pub_date"}),
	append=True
)

register_setting(
	name="TEMPLATE_ACCESSIBLE_SETTINGS",
	description="Sequence of setting names available within templates.",
	editable=False,
    default=(
		"TILE_COLOR",
		"LIVE_TILE_UPDATES_COUNT",
		"UPDATE_FREQUENCY",
		"CYCLE_OPTION",
		"TILE_BRANDING",
	),
    append=True,
)
