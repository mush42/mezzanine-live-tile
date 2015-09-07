

Mezzanine Live Tile
================

A Plug and play app for mezzanine CMS to provide live tile and notifications for new website content for your Windows 8,Windows 8.1, Windows 10, or Windows Phone visitors.


Introduction
-----


In Windows 8 and above Microsoft introduced the start screen with Metro UI. Every app is represented by a static tile, and the app can make that tile live by providing notifications which Windows will cycle between them instead of displaying a static tile.    


Internet Explorer and Microsoft Edge took this further by enabling websites owners to insert a special meta  tags in the head of their pages in order to provide live tile functionality to their visitors.


Visitors can click on ``Favorites`` and then ``Pinn To Start`` and a new tile will be added to their start screen.


This app makes it easier for sites built on top of mezzanine CMS to provide this functionality without any hassle, just plug the app, configure settings as descried billow, and you are ready to engage your visitors and push updated content to them right to their start screen.


Setup
-----


1. Run ``$ pip install mezzanine-live-tile``
2. In ``settings.py`` add ``mezzanine_live_tile`` to your ``INSTALLED_APPS`` above
   mezzanine apps.
3. Include ``mezzanine_live_tile`` urls in your projects ``urls.py`` as follows::
    from mezzanine_live_tile import urls as tile_urls
	...
    url(r"^tile/", include(tile_urls, namespace="tile")),
4. Run migrate::
    $ python manage.py migrate mezzanine_live_tile
5. Tweak settings as described below


Settings
---------


Template
===============


In your ``base.html`` insert the meta tags required to pin your site by loading ``tile_tags`` and inserting the following template tag in the ``head``:
    {% tile_meta %}


By default the app uses ``settings.SITE_TITLE`` to get the name that Windows will display for the tile in the start screen (analogous to app name). Alternatively you can pass a name to the ``tile_meta`` template tag to be used instead:
    {% tile_meta "My Awesome Site" %}


Tile Images:
===============


You must provide 4 different size images to be used as tile images for different tile sizes. For your convenience here are the recommended sizes taken from `this MSDN page`_::
- small (128x128) 
- medium (270x270)
- wide (558x270)
- large (558x558)


To override the provided ``food truck`` place-holder images, you should upload your own images to ``<static_dir>/tile/images/``.


For each image the name is the same as image size ("small" for small, "medium" for medium..etc.), we expect a ".png" image format in our template.


Notifications
==================


The app provide live tile notifications for new contents and updates, when a visitor pin your site windows notification system will pull updates from your server regularly and cycle between them in his start screen.


In order to support live tile notifications, you need to configure a class from which the app pulls new notifications which windows will cycle between in the live tile. 


By default, If ``mezzanine.blog`` is installed, then the app will use ``BlogPost`` model as the notification class, this simply means that the live tile will cycle between the recent five blog posts, this is fine for most situations.


If ``mezzanine.blog`` is not installed then the app has its own fallback ``Notification`` class which will be listed in the admin, and in this case you must edit the notifications manually to ensure that your users get updated content.


Also you can configure your own  class to be used as a notification class by configuring ``WINDOWS_TILE_MODEL`` setting in your ``settings.py``. It is a tuple of two items, the first item is the dotted path to the model class and the second one is a dictionary mapping notifications field names to your class field names::

    WINDOWS_TILE_MODEL = ("my_app.models.MyCustomNotificationClass",
     {
      "headline": "title",
      "body_text": "description",
      "image": "featured_image",
      "pub_date":"publish_date"
     }
    )


Editable Settings
==================


A handful of options are provided to customize the look and behavior of your tile, you can edit those options in the ``admin > settings``. here is a quick run through::
- ``TILE_COLOR``
    A background/accent color to use in the tile, this must be in the format (009900)
- ``LIVE_TILE_UPDATES_COUNT``
    How many notification windows will cycle between in the live tile.
- ``UPDATE_FREQUENCY``
    How often windows will pull updates from your website (default to one hour).
- ``TILE_BRANDING``
    What will windows display in the corner of the live tile (default to web site's favicon)
- ``CYCLE_OPTION``
    Restrict cycling in certain tile sizes.


Overriding Notification Templates
==================


By default the app uses a (header - body) text-only template for all tile sizes, but  you can override the default template to use your own notification template instead.


First read this `MSDN article about template catalog`_.


After you are comfortable  with the template design, copy the template from "<mezzanine_live_tile>/templates/tile/tileconf/notification.xml" to your project's ``templates`` path or your own app templates path, in the latter case your app must appear in the `INSTALLED_APPS` list before `mezzanine_live_tile`.


Then you can edit your newly copied template. To make your life easier you may make use of ``wrap_text`` and ``text_node_for`` template tags, see the original template for sample usage.


Note also that you must test your templates before shipping them to your visitors, because you do not have any way to debug those templates it can be a little tricky to design custom templates, so make sure they are working for all tile sizes before shipping them.

License
-------

Copyright (c) 2015 `Musharraf Omer`_


Mezzanine Live Tile  is licensed under the MIT license (See ``LICENSE`` for more details).




.. Links

.. _this MSDN page: https://msdn.microsoft.com/library/dn455106.aspx#CreatingLiveTiles
.. _MSDN article about template catalog: https://msdn.microsoft.com/en-us/library/hh761491.aspx
.. _Musharraf Omer: https://www.twitter.com/mush42
