# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
                ('body_text', models.CharField(max_length=240)),
                ('image', mezzanine.core.fields.FileField(max_length=200, null=True, blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'Publication Date')),
            ],
        ),
    ]
