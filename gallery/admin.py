from django.contrib import admin
from .views import Photo, Topic


class PhotoInline(admin.TabularInline):
    fieldsets = [
        ('Basic Info', {'fields': ['description']}),
        ('Upload Image', {'fields': ['image']})
    ]
    model = Photo
    extra = 3


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [PhotoInline]


admin.site.register(Topic, TopicAdmin)
