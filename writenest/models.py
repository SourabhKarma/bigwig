from django.db import models

# Create your models here.



class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()







    



# 2



class CountryName1(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class TeslaModel1(models.Model):
    model_name = models.CharField(max_length=30)
    price = models.IntegerField()
    origin = models.ForeignKey(CountryName1, on_delete=models.CASCADE, 
    related_name='teslamodels')

    def __str__(self):
        return self.model_name