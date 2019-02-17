from django.db import models

# Create your models here.

class Userdetails(models.Model):
    first_name = models.CharField(default = '', max_length=50)
    last_name = models.CharField(blank='True',default = '', max_length=50)
    about_me = models.TextField(blank='True',default='',max_length=350)
    email_id =models.CharField(blank='True',default='',max_length=100)
    phone_number = models.CharField(blank='True',default='',max_length=13)

    class Meta:
       ordering = ('first_name',)

    def __str__(self):
        return self.first_name
