from django.db import models
import datetime

# Create your models here.
class RegisterData(models.Model):
    member_name = models.CharField(max_length=20)
    doc_title = models.CharField(max_length=50)
    deadline_date= models.DateField(default=datetime.date.today)

    def DataList(self):
        list = [self.member_name , self.doc_title , self.deadline_date]
        return list

