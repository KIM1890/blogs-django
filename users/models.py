from django.db import models

# Create your models here.
class UploadImg(models.Model):
    captions = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.captions}"
