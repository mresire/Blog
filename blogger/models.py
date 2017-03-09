from django.db import models

# Create your models here.

class article(models.Model):
	Title = models.CharField(max_length=200)
	Body = models.TextField()
	Date = models.DateTimeField()
	Dislikes = models.IntegerField(default=0)
	Likes = models.IntegerField(default=0)
	Nbr_views = models.IntegerField(default=0)
	images = models.ImageField()
	Author = models.CharField(max_length=100, default='Your name')

	def __str__(self):
		return self.Title