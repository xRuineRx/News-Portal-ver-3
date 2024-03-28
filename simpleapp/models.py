from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
class Product(models.Model):
    name = models.CharField(
        max_length = 50,
        unique = True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators = [MinValueValidator(0)]
    )
    category = models.ForeignKey(
        to = 'Category', on_delete=models.CASCADE,
        related_name='products'
    )
    price = models.FloatField(
        validators = [MinValueValidator(0.0)]
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


# class Material(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class ProductMaterial(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     material = models.ForeignKey(Material, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length= 100, unique = True)

    def __str__(self):
        return self.name.title()


class News_All(models.Model):

    news = 'Нов'
    article = 'Ст'

    CHOICE_MAIN = [
        (news, 'Новости'),
        (article, 'Статья'),
    ]

    news_or_art = models.CharField(max_length=3,choices = CHOICE_MAIN, default = news)

    name = models.CharField(max_length= 100, unique = True)
    text = models.TextField(max_length= 100)
    time_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name.title()}"

    def get_absolute_url(self):
        return reverse('news_or_art_detail', args=[str(self.id)])
