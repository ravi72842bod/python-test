from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register(SongModel)
admin.site.register(PodcastModel)
admin.site.register(AudiobookModel)