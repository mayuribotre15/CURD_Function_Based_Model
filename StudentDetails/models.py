from django.db import models

# Create your models here.
class StudentDetails (models.Model):
    id = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile_no = models.IntegerField()
    