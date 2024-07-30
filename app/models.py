from django.db import models

# Create your models here.


class Index(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=17)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.first_name
