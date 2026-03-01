from django.contrib import admin
from testapp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['id','mdate','moviename','hero','heroine','ratings']
admin.site.register(Movie,MovieAdmin)