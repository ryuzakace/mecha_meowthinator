from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    YourName = models.CharField(max_length=255, blank=True)
    Phone = models.CharField(max_length=12, blank=True)
    texx = models.CharField(max_length=12, blank=True, default=None)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.YourName + str(self.uploaded_at)
