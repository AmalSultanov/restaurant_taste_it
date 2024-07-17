from django.db import models


class ReservationBannerModel(models.Model):
    image = models.ImageField(upload_to='reservation_banners')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'home banner'
        verbose_name_plural = 'home banners'


class ReservationModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    number_of_people = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'
