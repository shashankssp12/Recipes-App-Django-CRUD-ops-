from django.db import models

# Create your models here.

class Recipe(models.Model):
    # id=models.AutoField()
    Rname=models.CharField(max_length=120)
    description=models.TextField()
    Rimage=models.ImageField(upload_to="RecipeImages")
    def __str__(self) -> str:
        return self.Rname