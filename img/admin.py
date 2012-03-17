__author__ = 'Leon'
from img.models import Image
from django.contrib import admin


#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['urlname', 'filename', 'pub_date', 'pub_ip', 'content_type']}),
    ]
    # inlines = [ChoiceInline]
    list_display = ('urlname', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['image']
    date_hierarchy = 'pub_date'


admin.site.register(Image, ImageAdmin)

