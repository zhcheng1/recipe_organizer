# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_organizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='delicious',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=b'This is a default description', help_text=b'This is a quick description of your recipe', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default=b'This is a default direction', help_text=b'How to make the recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='email',
            field=models.EmailField(default=b'email', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='url',
            field=models.URLField(default=b'http://'),
            preserve_default=True,
        ),
    ]
