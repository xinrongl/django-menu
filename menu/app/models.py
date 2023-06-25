from django.db import models


# Create your models here.
class Dish(models.Model):
    pub_date = models.DateField(verbose_name="Publish date",
                                auto_created=True,
                                auto_now_add=True)
    dish_id = models.AutoField(verbose_name="Dish ID", primary_key=True)
    dish_desc = models.CharField(verbose_name="Dish description",
                                 max_length=1000)
    dish_image = models.ImageField(verbose_name="Image path", blank=True, upload_to="media")

    def __str__(self):
        return self.dish_desc


class History(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order_timestamp = models.DateTimeField(verbose_name="Order timestamp",
                                           auto_now_add=True)
