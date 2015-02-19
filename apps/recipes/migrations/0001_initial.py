# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text=b'This is a quick description of your recipe', null=True, blank=True)),
                ('directions', models.TextField(help_text=b'How to make the recipe')),
                ('ingredients', models.TextField(max_length=400)),
                ('photo', models.ImageField(null=True, upload_to=b'photos', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('reviews', models.TextField(help_text=b'User review here.')),
                ('star', models.PositiveIntegerField(null=True, blank=True)),
                ('username', models.CharField(max_length=20)),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
