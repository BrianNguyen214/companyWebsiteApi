# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Member(models.Model):
    # pk aka id --> numbers
    Name = models.CharField(max_length=250)
    Position = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    PictureLink = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name + " - " + self.Position
