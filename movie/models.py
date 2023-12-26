from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.FloatField()
    tags = models.ManyToManyField('Tag', blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movie_type')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(choices=(
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *'),
    ), default=5)

    def __str__(self):
        return self.text