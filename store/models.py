from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name    =   models.CharField(max_length=200, unique=True)
    slug            =   models.SlugField(max_length=200, unique=True)
    description     =   models.TextField(max_length=200, unique=True)
    price           =   models.IntegerField()
    images          =   models.ImageField(upload_to='photos/products')
    stock           =   models.IntegerField()
    is_available    =   models.BooleanField(default=True)
    category        =   models.ForeignKey(category, on_delete=models.CASCADE)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name 




#for_product_gallery_model_with_image_preview

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)
    
    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name = 'ProductGallery'
        verbose_name_plural = 'product gallery'