from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    class Meta:
        db_table = 'accounts'


class Article(TimestampedModel):
    class Meta:
        db_table = 'articles'

    category_choices = (
        ('sp', 'Sports'),
        ('te', 'Technology'),
        ('bu', 'Business'),
        ('po', 'Politics'),
        ('ot', 'Other')
    )

    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    category = models.CharField(choices=category_choices, max_length=50)





