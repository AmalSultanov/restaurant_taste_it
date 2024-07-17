from django.db import models


class HomeBannerModel(models.Model):
    image = models.ImageField(upload_to='home_banners')
    upper_title = models.CharField(max_length=100)
    middle_title = models.CharField(max_length=100)
    lower_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.upper_title

    class Meta:
        verbose_name = 'home banner'
        verbose_name_plural = 'home banners'


class CommentBannerModel(models.Model):
    image = models.ImageField(upload_to='comment_banners')
    upper_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.upper_title

    class Meta:
        verbose_name = 'comment banner'
        verbose_name_plural = 'comment banners'


class CommentModel(models.Model):
    image = models.ImageField(upload_to='user_comment_images')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class HomeInfoModel(models.Model):
    image1 = models.ImageField(upload_to='user_comment_images')
    image2 = models.ImageField(upload_to='user_comment_images')
    upper_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.upper_title

    class Meta:
        verbose_name = 'home info'
        verbose_name_plural = 'home info'


class ContactBannerModel(models.Model):
    image = models.ImageField(upload_to='contact_banners')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'contact banner'
        verbose_name_plural = 'contact banners'


class ContactInfoModel(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'contact info'
        verbose_name_plural = 'contact info'


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
