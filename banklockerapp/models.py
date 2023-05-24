from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subbanker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Lockertype(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class Assignlocker(models.Model):
    type = models.ForeignKey(Lockertype, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    lockernumber = models.CharField(max_length=100, null=True, blank=True)
    keynumber = models.CharField(max_length=100, null=True, blank=True)
    instruction = models.CharField(max_length=100, null=True, blank=True)
    nominee = models.CharField(max_length=100, null=True, blank=True)
    relnominee = models.CharField(max_length=100, null=True, blank=True)
    valuable = models.CharField(max_length=100, null=True, blank=True)
    idproof = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=200, default='Inactive', null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class About(models.Model):
    pagetitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.pagetitle

class Contact(models.Model):
    pagetitle = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    timing = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.pagetitle
