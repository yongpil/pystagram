# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0003_auto_20160718_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='filtered_image_file',
            field=models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
