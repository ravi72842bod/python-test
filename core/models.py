from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

class SongModel(models.Model):
	# id is created default in django model
	name = models.CharField(max_length=100)
	duration = models.PositiveIntegerField()
	uploaded = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.name


class PodcastModel(models.Model):
	# id is created default in django model
	name = models.CharField(max_length=100)
	duration = models.PositiveIntegerField()
	uploaded = models.DateTimeField(null=True, blank=True)
	host = models.CharField(max_length=100)
	participants = ArrayField(models.CharField(max_length = 100, default = " "), null=True, blank=True)

	def __str__(self):
		return self.name

class AudiobookModel(models.Model):
	# id is created default in django model
	title_audiobook = models.CharField(max_length=100)
	author_title = models.CharField(max_length=100)
	narrator = models.CharField(max_length=100)
	duration = models.PositiveIntegerField()
	uploaded = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title_audiobook