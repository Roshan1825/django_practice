from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def was_recently_updated(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)  


