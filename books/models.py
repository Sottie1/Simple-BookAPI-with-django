from django.db import models
from ckeditor.fields import RichTextField

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=20)
    year = models.IntegerField()
    isbn = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')
    description = RichTextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Books'
