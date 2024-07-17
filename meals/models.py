from django.db import models


class MenuBannerModel(models.Model):
    image = models.ImageField(upload_to='menu_banners')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'menu banner'
        verbose_name_plural = 'menu banners'


class MealCategoryModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class MealModel(models.Model):
    image = models.ImageField(upload_to='meals_images')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(MealCategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='meals')
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'
