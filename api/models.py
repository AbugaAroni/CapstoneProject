from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import uuid

# Create your models here.
class education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    qualification = models.CharField(max_length=50)
    description = models.TextField()
    start = models.DateField(auto_now=False)
    finish = models.DateField(auto_now=False)

    def __str__(self):
        return self.title

class job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.TextField()
    start = models.DateField(auto_now=False)
    finish = models.DateField(auto_now=False)

    def __str__(self):
        return self.title

class pictures(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    alt_tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

class user(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    admin = models.BooleanField(default=False)
    about = models.TextField()
    picturez = models.ManyToManyField(pictures)
    educationz = models.ManyToManyField(education)
    career = models.ManyToManyField(job)

    def __str__(self):
        return self.first_name

class contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name

class project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    writer = models.ForeignKey(user,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    live_link = models.CharField(max_length=50)
    picturez = models.ManyToManyField(pictures)

    def __str__(self):
        return self.writer.first_name
