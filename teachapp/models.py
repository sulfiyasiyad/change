from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class usercreate(models.Model):
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    number=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to="image/", null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
