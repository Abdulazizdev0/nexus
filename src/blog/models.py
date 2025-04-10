from django.db import models
from user.models import Profile



class BlogCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True, blank=True,related_name='subcategories')
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL, null=True, blank=False)
    image = models.ImageField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

class BlogView(models.Model):
    product = models.OneToOneField(Blog, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)


