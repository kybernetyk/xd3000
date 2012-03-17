from django.db import models
import datetime

# Create your models here.
class Image(models.Model):
    filename = models.TextField()
    urlname = models.TextField()
    pub_date = models.DateTimeField('date published')
    pub_ip = models.TextField()
    content_type = models.TextField()

    def __unicode__(self):
        return "id: " + str(self.id) + " | filename: " + self.filename + " | urlname: " + self.urlname + " | content type: " + self.content_type

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    was_published_today.short_description = 'uploaded today?'

