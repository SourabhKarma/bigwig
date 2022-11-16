from django.db import models

# Create your models here.



class AdvertismentCategory(models.Model):
    ads_category = models.TextField()
    ads_category_discription = models.TextField()


    def __str__(self):
        return self.ads_category


class AdvertisementSubCategory(models.Model):
    ads_category_id = models.ForeignKey(AdvertismentCategory,null=True,blank=True,on_delete=models.CASCADE)
    ads_subcategory = models.TextField()
    ads_subcategory_discription = models.TextField()

    def __str__(self):
        return self.ads_subcategory

class Advertisement(models.Model):
    ads_category_id = models.ForeignKey(AdvertismentCategory,null=True,blank=True,on_delete=models.CASCADE)
    ads_subcategory_id = models.ForeignKey(AdvertisementSubCategory,null=True,blank=True,on_delete=models.CASCADE)
    ad_name = models.TextField()

    def __str__(self):
        return self.ad_name