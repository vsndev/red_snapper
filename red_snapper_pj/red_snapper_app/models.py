from django.db import models

# Create your models here.
class RegisterData(models.Model):
    member_name = models.CharField(max_length=20)
    doc_title = models.CharField(max_length=50)
    deadline_date= models.DateField()


