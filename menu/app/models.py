from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Dish(models.Model):
    pub_date = models.DateField(verbose_name="Publish date",
                                auto_created=True,
                                auto_now_add=True)
    dish_id = models.AutoField(verbose_name="Dish ID", primary_key=True)
    name = models.CharField(verbose_name="Dish name", max_length=1000)
    desc = models.CharField(verbose_name="Dish description", max_length=1000)
    image = models.ImageField(verbose_name="Image path",
                              blank=True,
                              upload_to="media")
    tags = TaggableManager()

    def __str__(self):
        return self.name


class History(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order_timestamp = models.DateTimeField(verbose_name="Order timestamp",
                                           auto_now_add=True)
