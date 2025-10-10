from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Books(models.Model):
    title =         models.CharField(max_length=200)
    description = models.TextField(blank= True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='Author')
    publish_date = models.DateTimeField()
    
    def __str__(self):
        return self.title