# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class torrentModel(models.Model):
    torrentName = models.CharField(max_length=300)
    torrentLink = models.URLField(max_length=255, null=True, blank=True)
    torrentInfo = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.torrentName
    def __unicode__(self):
        return self.torrentName
