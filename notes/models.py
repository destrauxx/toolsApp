from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL



class Collection(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, default='Collection')

    def __str__(self):
        return self.name
    
    

class Note(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey(Collection, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length = 30)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length = 160)
    is_important = models.BooleanField(null=True, default=False)

    class Meta:
        ordering = ['-date', 'is_important']

    def __str__(self):
        return self.header
