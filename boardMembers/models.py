# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Member(models.Model):
    # pk aka id --> numbers
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + " - " + self.position
