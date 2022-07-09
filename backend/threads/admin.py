from django.contrib import admin

from .models import ContentThread, Comment

class ContentModelAdmin(admin.ModelAdmin):
    list_display = ('short_body', 'author')

    def short_body(self, obj):
        return obj.body[:100]

    short_body.short_description = 'Shortened Body'
    
admin.site.register(Comment, ContentModelAdmin)
admin.site.register(ContentThread, ContentModelAdmin)