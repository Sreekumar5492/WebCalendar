from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userprofile(models.Model):
  name = models.CharField(max_length=20)
  user = models.ForeignKey(User)
  email = models.EmailField(null=True);
  def __unicode__(self):
	return self.name

class events(models.Model):
    name                = models.CharField(max_length=20)
    user                = models.ForeignKey(User)
    event_type          = models.CharField(max_length=20)
    Description         = models.TextField(max_length=100)
    start               = models.DateTimeField()
    end                 = models.DateTimeField()
    allday              = models.BooleanField(default=False)
    status              = models.BooleanField(default=False)
    Notification_status = models.BooleanField(default=False)
    Notification_time   = models.DateTimeField()
    Location            = models.TextField(max_length=100)
    Location_lat        = models.DecimalField(max_digits=10,decimal_places=4)
    Location_long       = models.DecimalField(max_digits=10,decimal_places=4)
    Tagged_users        = models.ManyToManyField(User,related_name='tags')
    def __unicode__(self):
	return self.name
    
    