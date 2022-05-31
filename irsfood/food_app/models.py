from django.db import models

# Create your models here.
class Food(models.Model):
	productId = models.CharField(max_length=15)
	userId = models.CharField(max_length=30)
	profileName = models.CharField(max_length=150)
	helpfulness = models.CharField(max_length=20)
	score = models.FloatField()
	time = models.PositiveBigIntegerField()
	summary = models.TextField()
	text = models.TextField()

class Meta(models.Model):
	idexes = [models.Index(fields=['text','score','helpfulness'])]

		
