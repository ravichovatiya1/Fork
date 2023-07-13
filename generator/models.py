from django.db import models

# Create your models here.
class MemeImage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=225, default="Meme Images")
    
    def __str__(self):
        return str(self.id)
