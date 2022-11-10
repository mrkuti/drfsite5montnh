from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=500)

    @property
    def movie_count(self):
        return self.movie_set.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(null=True)
    duration = models.PositiveIntegerField(null=True)
    director = models.ForeignKey("Director", on_delete=models.CASCADE,null=True)




    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount


    def __str__(self):
        return self.title





class Review(models.Model):
    text = models.TextField(null=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(default=1, null=True)

    # stars = models

    def __str__(self):
        return self.text