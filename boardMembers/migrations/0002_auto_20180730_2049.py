# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardMembers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='picture',
            new_name='PictureLink',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='position',
            new_name='Position',
        ),
    ]
