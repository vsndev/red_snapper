from django.db import models
import datetime


class BaseManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get_queryset().get(**kwargs)
        except self.model.DoesNotExist:
            return None


# Create your models here.
class RegisterData(models.Model):
    member_name = models.CharField(max_length=20)
    doc_title = models.CharField(max_length=50)
    deadline_date= models.DateField(default=datetime.date.today)

    def DataList(self):
        list = [self.member_name , self.doc_title , self.deadline_date]
        return list


class User(models.Model):
    objects = BaseManager()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'username: {}, password: {}'.format(self.username, self.password)

