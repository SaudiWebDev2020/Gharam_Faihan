from django.db import models

# Create your models here.
class tvshow(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    releasedate=models.DateTimeField()
    descrption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"<tvshpw object: Title: {self.title}  NetWork : {self.network} Release Date: {self.releasedate} Descrption: {self.descrption} ({self.id})>\n"
