from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=35)
    @property
    def count_movies(self):
        return self.movies.all().count()


    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, related_name='movies', null=True)

    @property
    def rating_average(self):
        return self.reviews.aggregate(models.Avg('stars')).get('stars__avg')


    def __str__(self):
        return self.title

CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class Review(models.Model):
    text = models.TextField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True,
                              related_name='reviews')
    stars = models.IntegerField(default=1, choices=CHOICES)


    def __str__(self):
        return self.text