from django.db import models


class AboutBannerModel(models.Model):
    image = models.ImageField(upload_to='about_banners')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about banner'
        verbose_name_plural = 'about banners'


class AboutInfoModel(models.Model):
    image = models.ImageField(upload_to='about_info_images')
    upper_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about info'
        verbose_name_plural = 'about info'


class AboutStatisticsPhotoModel(models.Model):
    image = models.ImageField(upload_to='about_statistics')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'photo'

    class Meta:
        verbose_name = 'statistics photo'
        verbose_name_plural = 'statistics photos'


class AboutStatisticsModel(models.Model):
    stat_number = models.PositiveIntegerField()
    stat_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stat_title

    class Meta:
        verbose_name = 'statistics'
        verbose_name_plural = 'statistics'


class StaffBannerModel(models.Model):
    image = models.ImageField(upload_to='staff_banners')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'staff banner'
        verbose_name_plural = 'staff banners'


class StaffModel(models.Model):
    image = models.ImageField(upload_to='staff_images')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'
