from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    """docstring for category."""
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField(max_length=100,blank=True)
    cat_img=models.ImageField(upload_to='photos/categories',blank=True)
    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"
    def get_url(self):
        # the pass value product_by_category is a view name,return the url
        print(str(reverse('product_by_category',args=[self.slug])))
        return reverse('product_by_category',args=[self.slug])
    def __str__(self):
        return self.category_name