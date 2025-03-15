from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added')
    list_filter = ('author', 'date_added')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
