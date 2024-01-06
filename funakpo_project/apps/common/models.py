from django.db import models

# Create your models here.

class Slider(models.Model):
    slideImg=models.ImageField(upload_to='slideImage/')


class Gallery(models.Model):
    slideImg=models.ImageField(upload_to='gallery/')

class News(models.Model):
    newsImage=models.ImageField(upload_to='news/')
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=60)
    date=models.CharField(max_length=20)
    info=models.TextField()
    postDate=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Staff(models.Model):
    staffImage=models.ImageField(upload_to='staff/')
    name=models.CharField(max_length=45)
    position=models.CharField(max_length=45)


    def __str__(self):
        return self.name

