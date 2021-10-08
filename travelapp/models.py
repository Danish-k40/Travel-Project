from django.db import models


# Create your models here.

# create table using class (This is not actual method)
# class place:
#     id: int
#     name: str
#     price: int
#     desc: str
#     img: str
# data base table for place
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()
    price = models.IntegerField()   # edited
    offers = models.BooleanField(default=False)

# data base table for news post
class news_post(models.Model):
    # date = models.DateField()
    heading = models.CharField(max_length=100)
    sub_head = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(upload_to='pictures')
    day = models.IntegerField()
    month = models.CharField(max_length=10)

