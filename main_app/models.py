from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profiles_list_by_category', args=[self.slug])


class Profile(models.Model):
    name = models.CharField('Имя', max_length=150)
    slug = models.SlugField("Слаг", max_length=150)
    category = models.ManyToManyField(Category, related_name='category')
    description = models.TextField('Описание')
    rating = models.DecimalField('Рейтинг', max_digits=10, decimal_places=2)
    img = models.ImageField("Аватар", upload_to="profile_pic/")
    amount = models.PositiveIntegerField('Ставка', default=0)
    free_time = models.ManyToManyField('Days', related_name='free_time')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile_detail', args=[self.slug])


class Days(models.Model):
    name = models.CharField('Дни недели', max_length=50)

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return self.name
