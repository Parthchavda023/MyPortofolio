from django.db import models

# Create your models here.
class SendModel(models.Model):
    created = models.DateTimeField(auto_now_add= True)

    name = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=108)
    msg = models.CharField(max_length=99999)
    