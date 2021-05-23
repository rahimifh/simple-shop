from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo (models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user =models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
# Create your models here.
class order (models.Model):
    item = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.item
class userdetail (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank = True)
    order = models.TextField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class stuff (models.Model):
    image = models.ImageField(upload_to='shop/images/')
    title =  models.CharField(max_length=100)
    text = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
