from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

       
class Quotes(models.Model):

    content = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank = True, null=True)
    author = models.CharField(max_length=30, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.content
