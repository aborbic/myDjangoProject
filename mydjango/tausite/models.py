from django.db import models


class Email(models.Model):
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address


class Picture(models.Model):
    name = models.CharField(max_length=50)
    picture_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Home(models.Model):
    homeTitle = models.CharField(max_length=200)
    homeDesc = models.TextField()
    homeDate = models.DateTimeField()

    def __str__(self):
        return self.homeDesc


class Announcements(models.Model):
    # created a space for the title, description, and date published
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.description
