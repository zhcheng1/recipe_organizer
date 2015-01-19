# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(help_text=b'This is a quick description of your recipe', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(help_text=b'How to make the recipe'),
            preserve_default=True,
        ),
    ]
