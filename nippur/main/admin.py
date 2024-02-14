from django.contrib import admin
from .models import User
from .models import Song
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SongResource(resources.ModelResource):

    class Meta:
        model = Song


class SongAdmin(ImportExportModelAdmin):
    resource_classes = [SongResource]

admin.site.register(User)
admin.site.register(Song, SongAdmin)
