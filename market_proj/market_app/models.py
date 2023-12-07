from django.db import models
from django.urls import reverse

#Модель категорий
class Category(models.Model):
    #Имя категории
    name = models.CharField(max_length=200)
    #Слаг категории
    slug = models.SlugField(max_length=200,
                            unique=True)
    
    #В Meta-классе модели Product определен многопольный индекс по полям id и slug.
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('market_app:product_list_by_category',
                       args=[self.slug])

#Модель товара
class Product(models.Model):
    #Категория товара 
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    #Имя товара
    name = models.CharField(max_length=200)
    #Слаг товара
    slug = models.SlugField(max_length=200)
    #Изображения товара
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    #Описание товара
    description = models.TextField(blank=True)
    #Цена товара
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    #Наличие товара
    available = models.BooleanField(default=True)
    #Время создания товара
    created = models.DateTimeField(auto_now_add=True)
    #Время обновления товара
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['id', 'slug']),
        models.Index(fields=['name']),
        models.Index(fields=['-created']),]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('market_app:product_detail',
                       args=[self.id, self.slug])