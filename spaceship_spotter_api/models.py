# This is where the models go!
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Using the user: user = models.ForeignKey(settings.AUTH_USER_MODEL)
class Report(models.Model):
    timestamp = models.DateTimeField()
    lon = models.FloatField()
    lat = models.FloatField()

    def __unicode__(self):
        return "Report-(%s)-%s,%s" % (self.timestamp, self.lon, self.lat)

class Reading(models.Model):
    sensor = models.CharField(max_length=255)
    type = models.IntegerField()
    accuracy = models.IntegerField()
    timestamp = models.DateTimeField()

    report = models.ForeignKey(Report)

    def __unicode__(self):
        return "Reading-(%s)-%s-%s-%s" % (self.timestamp, self.sensor, self.type, self.accuracy)

class Values(models.Model):
    reading = models.ForeignKey(Reading)
    value = models.FloatField()
