from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
