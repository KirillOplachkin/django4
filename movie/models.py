from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.TextField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
